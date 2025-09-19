#!/usr/bin/env python3
import json
import sys

def load_file(file_path):
    """Load the conversation logs JSON file."""
    
    data_list = []
    with open(file_path, 'r') as f:
        for line in f:
            try:
                json_dict = json.loads(line.strip())
                data_list.append(json_dict)
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON on line: {line.strip()}. Error: {e}")

    return data_list

def find_certified_agents(data_list, skill):
    """Look for a passing certification evaluation string."""

    search_string = "certification evaluation: pass"
    agents = []
    for item in data_list:
        if search_string in item['message'].lower():
            agents.append({'skill': skill,
                           'agent_name': item['path'],
                           'timestamp': item['timestamp']})
    
    # Select most recent certification timestamp for each agent_name
    most_recent_by_key = {}
    for item in agents:
        key = item['agent_name']
        timestamp = item['timestamp']

    # Compare the current item's timestamp with the one stored for the key
    if key not in most_recent_by_key or timestamp > most_recent_by_key[key]['timestamp']:
        most_recent_by_key[key] = item

    result = list(most_recent_by_key.values())

    return result

def write_file(data_list, file_path):
    """Write any found certifications to a certifications file."""
    
    file_path = 'certifications.jsonl'
    with open(file_path, 'w') as f:
        json.dump(data_list, f, indent=4)

    return

def main(file_path, skill):
    """Look in a certifier agent's conversation logs for the string "certification evaluation: pass" \
    and store the associated agent_name and timestamp in certifications.jsonl."""

    # Load the conversation logs
    data_list = load_file(file_path)
    
    # Find certified agents
    agents = find_certified_agents(data_list, skill)
    
    # Write agent_names for certified agents to certifications file
    write_file(agents, 'certifications.jsonl')

    return

if __name__ == "__main__":
    file_path = sys.argv[1]
    skill = sys.argv[2]
    main(file_path, skill)
