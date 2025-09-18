# SETUP
# python3 -m venv venv && source venv/bin/activate
# pip install anthropic

# import packagees
from anthropic import Anthropic
import os

# Set API key through environment variable or directly in the code
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

# Create Anthropic client with explicit API key
anthropic = Anthropic(api_key=ANTHROPIC_API_KEY)

# Define a 10th grade math certifier agent
def run_certifier_agent(agent_response):

    # Create the system prompt
    system_prompt_certifier = "You are a highly skilled AI assistant certified in systems engineering. \
    Your job is to evaluate whether an agent can be certified as a systems engineering expert \
    and output PASS or FAIL into JSON file format. \
    "

    # Run certifier agent
    resp = anthropic.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=512,
                messages=[{"role":"user","content":agent_response}],
                system=system_prompt_certifier)
            
    response_text = resp.content[0].text
    
    return response_text


# Create the expert prompt
full_prompt = "Please provide answers to the following 3 questions. \
1. Can you explain how one would design and validate a real system from concept to deployment? \
2. You have three design options for a satellite power system. How would you decide which to implement? \
3. What are some tools/languages you have used? \
"

# Define a expert agent
system_prompt = "You are a AI assistant who knows systems engineering."
# Run the expert agent
resp = anthropic.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=512,
            messages=[{"role":"user","content":full_prompt}],
            system=system_prompt)

agent_response = resp.content[0].text
print("\n")
print('expert_response', agent_response)
print("\n")

certifier_response = run_certifier_agent(agent_response)
print("\n")
print('certifier_response', certifier_response)
print("\n")

# Define a nonexpert agent
system_prompt = "You are a AI assistant who does not know systems engineering."
# Run the nonexpert agent
resp = anthropic.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=512,
            messages=[{"role":"user","content":full_prompt}],
            system=system_prompt)

agent_response = resp.content[0].text
print("\n")
print('nonexpert_response', agent_response)
print("\n")

certifier_response = run_certifier_agent(agent_response)
print("\n")
print('certifier_response', certifier_response)
print("\n")