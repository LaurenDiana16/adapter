## Certifier Agent for Skill

This implementation adds /certify as a special command to adapter/nanda_adapter/core/agent_bridge.py. For each skill (currently only supports aerospace engineering), certify test prompts and certifier agent names are stored in a MongoDB database.

Before running the /certify command a user has to export the MongoDB credentials needed to look up the test prompts and certifier agent names.
```
export MONGODB_CONNECTION_STRING=<your-connection-string>
```

1. Make sure the agent you wish to certify is running. For demonstration purposes, agents945000 was created as an aerospace engineering expert by issuing the following commands from this repo.
```
cd adapter/nanda_adapter/examples
nohup python3 demo/langchain_ae_agent.py > out.log 2>&1 &
```
2.  From the UI associated with that agent or another agent, issue the following command to certify that agent.
```
# certify agents945000 in aerospace_engineering
/certify @agents945000 aerospace_engineering
```
3. The skill test prompts are stored in a MongoDB database and a query is used to retrieve the test prompt for the specified skill. The test prompt is sent to the agent being certified.
```
# Get the target agent to certify
parts = user_text.split(" ")
target_agent = parts[1][1:]

# Use the skill to look up the test prompt and certifier prompt
skill = parts[2]

# Send the test prompt to target agent
message_text = find_certifier_prompt_for_skill(skill)
result = send_to_agent(target_agent, message_text, conversation_id, {
        'path': current_path,
        'source_agent': agent_id
        })
```
You can see the target agent's response message in the sender agent's out.log file. It is not displayed in the UI currently but we could add it there if we want to see the full chain of conversation.
<img width="1001" height="588" alt="Screenshot 2025-10-13 at 12 11 19 PM" src="https://github.com/user-attachments/assets/ae8c20bf-5b5e-4bc1-bb2e-cf79cc2c30de" />

4. The target agent's response is then passed to a certifier agent. The certifier agents are already running and a MongoDB database is used to look up the agent name for the certifier for the specified skill.
```
# Send target agent's response to certifier agent
certifier_agent = find_certifier_agent_for_skill(skill)
claude_response = send_to_agent(certifier_agent, result, conversation_id, {
    'path': current_path,
    'source_agent': target_agent
})
```
You can see the certifier's response message in the sender agent's out.log file.
<img width="989" height="334" alt="Screenshot 2025-10-13 at 12 11 44 PM" src="https://github.com/user-attachments/assets/c7599d8a-1cba-4e08-80a9-6572fdad028a" />

The certifier's response message is also displayed in the UI.
<img width="1412" height="819" alt="Screenshot 2025-10-13 at 12 11 02 PM" src="https://github.com/user-attachments/assets/35aaa072-e815-41fb-ae9c-3b96c440fc8d" />

## Next steps
1. Create a more sophisticated certifier agent: one that utilizes a RAG/specialized knowledge base to assess other agents
