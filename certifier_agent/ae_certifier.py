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
    system_prompt_certifier = "You are a highly skilled AI assistant certified in aerospace engineering. \
    Your job is to evaluate whether an agent can be certified as an aerospace engineering expert \
    and output into JSON file format with just one key value pair, certification_evaluation as key and PASS or FAIL as value. \
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
1. Can you explain airfoil theory? \
2. What specialized tools are being used in the field right now? \
3. What are some industry standards and practices? \
"

# Define a expert agent
system_prompt = "You are a AI assistant who knows aerospace engineering."
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
system_prompt = "You are a AI assistant who does not know aerospace engineering."
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