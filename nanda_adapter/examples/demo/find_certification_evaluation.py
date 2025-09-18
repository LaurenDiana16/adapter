import json

def load_file(file_path):
    data_list = []
    with open(file_path, 'r') as f:
        for line in f:
            try:
                json_dict = json.loads(line.strip())
                data_list.append(json_dict)
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON on line: {line.strip()}. Error: {e}")

    return data_list

def find_certified_agents(data_list):
    search_string = '"certification_evaluation": "PASS"'
    agents = []
    for item in data_list:
        if search_string in item['message']:
            agents.append({'skill': 'aerospace_engineering',
                                    'agent_name': item['path'],
                                    'timestamp': item['timestamp']})
    return agents

def write_file(data_list, file_path):
    """ write to certifications file """
    file_path = 'certifications.jsonl'
    with open(file_path, 'w') as f:
        json.dump(data_list, f, indent=4)

    return

def find_certifications(file_path):
    data_list = load_file(file_path)
    agents = find_certified_agents(data_list)
    write_file(agents, 'certifications.jsonl')

    return

file_path = "../conversation_logs/conversation_xx.jsonl"
find_certifications(file_path)
