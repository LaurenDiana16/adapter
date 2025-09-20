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

# Define a certifier agent
def run_certifier_agent(agent_response):

    # Create the system prompt
    system_prompt_certifier = "You are a highly skilled AI assistant certified in safety and risk management. \
    Your job is to evaluate whether an agent can be certified as a safety and risk management expert \
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
1. Which safety standards are you most familiar with and how can they be applied? \
2. Describe a time you identified a latent safety risk. How did you address it? \
3. Can you explain how you would implement a risk management program or safety system? \
"

# Define a expert agent
system_prompt = "You are a AI assistant who knows safety and risk management."
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
system_prompt = "You are a AI assistant who does not know safety and risk management."
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