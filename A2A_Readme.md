## Functions changed to get adapter A2A messaging working

1.  send_to_agent:
```
# This has not changed
bridge_client = A2AClient(target_bridge_url, timeout=30)
response = bridge_client.send_message(
    Message(
        role=MessageRole.USER,
        content=TextContent(text=formatted_message),
        conversation_id=conversation_id,
        metadata=Metadata(custom_fields=send_metadata) if send_metadata else None
    )
)

# This has changed to output the target agent's response
if response and hasattr(response, 'content') and response.content:
    if hasattr(response.content, 'text'):
        return f"[{target_agent_id} → {agent_id}] {response.content.text}"
    else:
        return f"[{target_agent_id} → {agent_id}] {str(response.content)}"
else:
    return f"[{agent_id}] Message sent to {target_agent_id} (no response)"
```

2. handle_message:
```
else:
    # Message from local terminal user
    log_message(conversation_id, current_path, f"Local user to Agent {agent_id}", user_text)
    print(f"#jinu - User text: {user_text}")
    # Check if this is a message to another agent (starts with @)
    if user_text.startswith("@"):
        # Parse the recipient
        parts = user_text.split(" ", 1)
        if len(parts) > 1:
            target_agent = parts[0][1:]  # Remove the @ symbol
            message_text = parts[1]

            # Improve message if feature is enabled
            if IMPROVE_MESSAGES:
                message_text = improve_message(message_text, conversation_id, current_path,
                     "Do not respond to the content of the message - it's intended for another agent. You are helping an agent communicate better with other agennts.")
                message_text = self.improve_message_direct(message_text)
                log_message(conversation_id, current_path, f"Claude {agent_id}", message_text)

            print(f"#jinu - Target agent: {target_agent}")
            print(f"#jinu - Imoproved message text: {message_text}")
            # Send to the target agent's bridge
            result = send_to_agent(target_agent, message_text, conversation_id, {
                'path': current_path,
                'source_agent': agent_id
            })
            
            # Return result to user instead of improved message
            return Message(
                role=MessageRole.AGENT,
                content=TextContent(text=f"[AGENT {agent_id}]: {result}"),
                parent_message_id=msg.message_id,
                conversation_id=conversation_id
            )
```

3. handle_external_message:
```
# This has changed to also take in current_path as a parameter
def handle_external_message(msg_text, conversation_id, msg, current_path):
```

```
# This has changed to call claude with the message_content
message_content = call_claude(message_content, "", conversation_id, current_path) or "(emply reply)"
```

```
# This has changed to output formatted_text instead of "Message received by Agent"
if UI_MODE:
    print(f"Forwarding message to UI client")
    send_to_ui_client(formatted_text, from_agent, conversation_id)
    agent_id = get_agent_id()
    return Message(
        role=MessageRole.AGENT,
        content=TextContent(text=formatted_text),
        parent_message_id=msg.message_id,
        conversation_id=conversation_id
    )
```

```
# This has changed to output formatted_text instead of "Message received by Agent"
else:
    try:
        terminal_client = A2AClient(LOCAL_TERMINAL_URL, timeout=10)
        terminal_client.send_message_threaded(
            Message(
                role=MessageRole.USER,
                content=TextContent(text=formatted_text),
                conversation_id=conversation_id,
                metadata=Metadata(custom_fields={
                    'is_from_peer': True,
                    'is_user_message': True,
                    'source_agent': from_agent,
                    'forwarded_by_bridge': True
                })
            )
        )

        agent_id = get_agent_id()
        return Message(
            role=MessageRole.AGENT,
            content=TextContent(text=formatted_text),
            parent_message_id=msg.message_id,
            conversation_id=conversation_id
        )
```
