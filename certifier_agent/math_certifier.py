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
    system_prompt_certifier = "You are a highly skilled AI assistant certified in Grade 10 mathematics. \
    Please evaluate the agent's answers to the following 5 questions and output pass or fail. \
    1. What concepts do you learn in 10th grade math that you do not learn in 9th grade math? \
    2. Can you teach me a small part of 10th grade math? \
    3. One number is 2.5 times as much as another number. What could the numbers be? \
    4. If you give me any right triangle with one angle 30 degrees can you predict the ratio of sides? \
    5. What is function notation? What is the domain in a math problem?"

    # Run certifier agent
    resp = anthropic.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=512,
                messages=[{"role":"user","content":agent_response}],
                system=system_prompt_certifier)
            
    response_text = resp.content[0].text
    
    return response_text


# Create a test for 10th grade mathematics, this matches what the certifier will evaluate for
full_prompt = "Please provide answers to the following 5 questions. \
1. What concepts do you learn in 10th grade math that you do not learn in 9th grade math? \
2. Can you teach me a small part of 10th grade math? \
3. One number is 2.5 times as much as another number. What could the numbers be? \
4. If you give me any right triangle with one angle 30 degrees can you predict the ratio of sides? \
5. What is function notation? What is the domain in a math problem?"


# Define an agent that only knows up to 9th grade math
system_prompt_9th = "You are a AI assistant who only knows up to 9th grade mathematics."

# Run the non-expert agent
resp = anthropic.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=512,
            messages=[{"role":"user","content":full_prompt}],
            system=system_prompt_9th)

agent_response = resp.content[0].text
print("\n")
print('agent_response_9th', agent_response)
print("\n")

certifier_response = run_certifier_agent(agent_response)
print("\n")
print('certifier_response_9th', certifier_response)
print("\n")

# Define an agent that knows 10th grade math
system_prompt_10th = "You are a AI assistant who knows up to 10th grade mathematics."

# Run the expert agent
resp = anthropic.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=512,
            messages=[{"role":"user","content":full_prompt}],
            system=system_prompt_10th)

agent_response = resp.content[0].text
print("\n")
print('agent_response_10th', agent_response)
print("\n")

certifier_response = run_certifier_agent(agent_response)
print("\n")
print('certifier_response_10th', certifier_response)
print("\n")