## Certifier agent for skill

This implementation adds /certify as a special command to adapter/nanda_adapter/core/agent_bridge.py. For each skill (currently only supports aerospace engineering, systems engineering, and safety and risk management), the certify test prompts have been stored in a MongoDB database. Additionally, the agent names for the certifier agents for the 3 skills have been stored in a MongoDB database. Before running the /certify command a user has to export the MongoDB credentials needed to look up the test prompts and certifier agent names.
```
export MONGODB_CONNECTION_STRING=<your-connection-string>
```

1. From the UI, issue /certify @<agent-to-certify> <skill-to-certify> as a command
```
/certify @agents123 aerospace_engineering
```

2. The skill test prompts are stored in a MongoDB database and a query is used to retrieve the test prompt for the specified skill. The test prompt is sent to the agent being certified.
```
# Get the target agent to certify
parts = user_text.split(" ")
target_agent = parts[1][1:]

# Use the skill to look up the test prompt and certifier prompt
skill = parts[2]
message_text = find_certifier_prompt_for_skill(skill)

# Send the test prompt to target agent
result = send_to_agent(target_agent, message_text, conversation_id, {
        'path': current_path,
        'source_agent': agent_id
        })
```
You can see the response message in the target agent's out.log file. It is not displayed in the UI currently but we could add it there if we want to see the full chain of conversation.
<img width="983" height="664" alt="Screenshot 2025-10-13 at 10 59 16 AM" src="https://github.com/user-attachments/assets/4dce1c01-7c39-4f8e-8a02-3d48dd82060e" />

3. The target agent's response is then passed to a certifier agent. The certifier agents are already running and a MongoDB database is used to look up the agent name for the certifier for the specified skill.
```
# Send target agent's response to certifier agent
certifier_agent = 'agents619762' # replace this with a query to MongoDB database
claude_response = send_to_agent(certifier_agent, result, conversation_id, {
    'path': current_path,
    'source_agent': target_agent
})
```
You can see the certifier's response message in the sender agent's out.log file.
<img width="972" height="307" alt="Screenshot 2025-10-13 at 10 59 56 AM" src="https://github.com/user-attachments/assets/5c102fc0-4562-449b-a01a-40614d855cb1" />

The certifier's response message is also displayed in the UI with a PASS/FAIL and reasoning.
<img width="933" height="901" alt="Screenshot 2025-10-13 at 10 58 14 AM" src="https://github.com/user-attachments/assets/9d3b4540-8a3d-4139-9457-0110db30659d" />

## Next steps
1. Remove the hardcoded agent name for the certifier agent and have it queried from a MongoDB database
