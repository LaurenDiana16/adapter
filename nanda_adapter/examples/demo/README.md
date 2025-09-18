## Steps to follow

Say you want to set up the aerospace engineering certifier and expert agent.

1. Create the certifier agent using the adapter repo

```
nohup python3 langchain_ae_certifier.py > out.log 2>&1 &
```
2. Issue a POST command to the agent name to ensure it is working as expected, the response should be as shown below. The certifier has been instructed to evaluate an expert agent for the provided skill and to respond with a single word PASS or FAIL. This allows us to be able to directly use a certifier's response to update an agent's AgentFacts as opposed to having to parse a full response for the word PASS or FAIL.
```
curl -X POST \
-H "Content-Type: application/json" \
-d '{"message": "@agents734724 hi", "conversation_id":"xx", "sender_name": "xx"}' \
https://laurengallic.com:6001/api/send
```
```
{"agent_id":"agents734724","conversation_id":"xx","response":"[AGENT agents734724]: {\n  \"certification_evaluation\": \"PASS\"\n}"}
```
3. On a different EC2 instance, using a different domain, create the expert agent using the adapter repo
```
nohup python3 langchain_ae_agent.py > out.log 2>&1 &
```
4. Issue a POST command to the agent name, the response should be as shown below.
```
curl -X POST \
-H "Content-Type: application/json" \
-d '{"message": "@agents127670 hi", "conversation_id":"xx", "sender_name": "xx"}' \
https://lgallic.com:6001/api/send
```
```
{"agent_id":"agents127670","conversation_id":"xx","response":"[AGENT agents127670]: Hello! I'm an AI assistant focused on aerospace engineering. How can I assist you today?"}
```
5. Have the certifier send this exact message to the expert, the response should be as shown below.
```
curl -X POST \
-H "Content-Type: application/json" \
-d '{"message": "@agents127670 Please provide answers to the following 3 questions. 1. Can you explain airfoil theory? 2. What specialized tools are being used in the field right now? 3. What are some industry standards and practices?", "conversation_id":"xx", "sender_name": "xx"}' \
https://laurengallic.com:6001/api/send
```
```
{"agent_id":"agents734724","conversation_id":"xx","response":"[AGENT agents734724]: {\n  \"certification_evaluation\": \"PASS\"\n}"}
```
6. Repeat this process for the Safety and Risk Management Certifier/Expert. Here is the message the needs to be sent by the certifier to the expert.
```
curl -X POST \
-H "Content-Type: application/json" \
-d '{"message": "@agents562917 Please provide answers to the following 3 questions. 1. Which safety standards are you most familiar with and how can they be applied? 2. Describe a time you identified a latent safety risk. How did you address it? 3. Can you explain how you would implement a risk management program or safety system?", "conversation_id":"xx", "sender_name": "xx"}' \
https://laurengallic.com:6001/api/send
```
7. Repeat this process for the Systems Engineering Certifier/Expert. Here is the message that needs to be sent by the certifier to the expert.
```
curl -X POST \
-H "Content-Type: application/json" \
-d '{"message": "@agents700963 Please provide answers to the following 3 questions. 1. Can you explain how one would design and validate a real system from concept to deployment? 2. You have three design options for a satellite power system. How would you decide which to implement? 3. What are some tools/languages you have used?", "conversation_id":"xx", "sender_name": "xx"}' \
https://laurengallic.com:6001/api/send
```
