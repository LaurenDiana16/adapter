## Index

1. math_certifier.py: A python script for how a 10th grade math certifier agent would interact with a 10th grade math expert agent and a 9th grade and below math agent
2. mongodb_setup.md: A document that details how to setup a mongodb database on a EC2 instance
3. find_endpoints_for_skill.py: A python script that querys a mongodb database for a specific skill and returns all associated agent endpoints

## Steps done so far

1. Set up MongoDB on a EC2 instance
2. Created a new agent registry using the projnanda/nanda-index repo (https://lgallic.com:6900) 
3. Created a langchain 10th grade math certifier agent (adapter/examples/langchain_10thgrademath_certifier.py) and ensured it can be run using the adapter repo, appears to be functional, registered to new agent registry
4. Created a langchain 10th grade math expert agent (adapter/examples/langchain_10thgrademath_agent.py) and ensured it can be run using the adapter repo, appears to be functional, registered to new agent registry
5. Created a Python script for finding all agents with the "10th grade mathematics" skill

## Steps to do

6. Have the certifier agent use the endpoint to "certify" the agent with the "10th grade mathematics" skill and issue a certificate to the AgentFacts
