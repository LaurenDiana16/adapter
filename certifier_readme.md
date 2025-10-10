## Certifier agent for skill

1. Added /certify as a command, example usage is as follows
```
/certify @agents123 aerospace_engineering
```

2. Currently, the test prompt for aerospace_engineering is hardcoded, this would be moved to a MongoDB database and a query would be used to retrieve the test prompt for the specified skill. The test prompt is sent to the agent being certified.
```
message_text = "Please provide answers to the following 3 questions. \
                    1. Can you explain airfoil theory? \
                    2. What specialized tools are being used in the field right now? \
                    3. What are some industry standards and practices? \
                    "
# Send the test prompt to target agent
result = send_to_agent(target_agent, message_text, conversation_id, {
        'path': current_path,
        'source_agent': agent_id
        })
```
3. The target agent's response is then passed to a certifier agent. Currently, the certifier agent is created inline using call_claude and a system_prompt. Ideally, the certifier agent would be running already externally and the response would be send across the A2A bridge to the certifier agent.
```
# Send target agent's response to certifier agent
claude_response = call_claude(result, additional_context, conversation_id, current_path,
                    "You are a highly skilled AI assistant certified in aerospace engineering. \
                    Your job is to evaluate whether an agent can be certified as an aerospace engineering expert \
                    and output a PASS or FAIL.\
                    ")
```

## Next steps
1. Move the test prompts to a MongoDB database and use a query to call them in
2. Move the certifier agents to run externally
