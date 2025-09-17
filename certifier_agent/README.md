## Index

1. math_certifier.py: A python script for how a 10th grade math certifier agent would interact with a 10th grade math expert agent and a 9th grade and below math agent
2. mongodb_setup.md: A document that details how to setup a mongodb database on a EC2 instance
3. find_endpoints_for_skill.py: A python script that querys a mongodb database for a specific skill and returns all associated agent endpoints

## Steps done so far

1. Set up MongoDB on a EC2 instance
2. Created a new agent registry using the projnanda/nanda-index repo (https://lgallic.com:6900) 
3. In the same mongodb instance, created a database for AgentFacts, added a record for the 10th grade math expert agent
4. Created a langchain 10th grade math certifier agent (adapter/examples/langchain_10thgrademath_certifier.py) and ensured it can be run using the adapter repo, appears to be functional, registered to new agent registry
5. Created a langchain 10th grade math expert agent (adapter/examples/langchain_10thgrademath_agent.py) and ensured it can be run using the adapter repo, appears to be functional, registered to new agent registry
6. Created a Python script for querying the AgentFacts database for all agents with the "10th grade mathematics" skill

## Steps to do

7. Have the certifier agent hit the endpoint and certify the agent with the "10th grade mathematics" skill and issue a certificate to the AgentFacts

## API checks that certifier is working
CERTIFIER -> lgallic.com -> agents272939
curl -X POST \
-H "Content-Type: application/json" \
-d '{"message": "@agents272939 hi", "conversation_id":"xx", "sender_name": "xx"}' \
https://lgallic.com:6001/api/send

"response":"[AGENT agents272939]: Hello! I am an AI assistant certified in Grade 10 mathematics. I'd be happy to answer your questions. Please go ahead and ask your questions, and I will do my best to provide accurate and helpful responses."

## API check that expert is working
EXPERT -> laurengallic.com -> agents571552
curl -X POST \
-H "Content-Type: application/json" \
-d '{"message": "@agents571552 hi", "conversation_id":"xx", "sender_name": "xx"}' \
https://laurengallic.com:6001/api/send

"response":"[AGENT agents571552]: Hello! I'm an AI assistant with knowledge up to 10th grade mathematics. How can I assist you today?

## Have certifier ask expert question
curl -X POST \
-H "Content-Type: application/json" \
-d '{"message": "@agents571552 what are concepts you learn in 10th grade that you do not know in 9th grade", "conversation_id":"xx", "sender_name": "xx"}' \
https://lgallic.com:6001/api/send

"response":"[AGENT agents272939]: 1. What concepts do you learn in 10th grade math that you do not learn in 9th grade math?\n\nAgent's Response:\nIn 10th grade math, students typically learn concepts that build upon the foundation established in 9th grade. Some key concepts that are introduced or explored in more depth in 10th grade math include:\n\n1. Trigonometry: 10th grade math often includes the study of trigonometric functions, such as sine, cosine, and tangent, and their applications in solving triangles and other geometric problems.\n\n2. Probability and Statistics: 10th grade math may cover more advanced probability and statistics topics, such as probability distributions, normal distributions, and hypothesis testing.\n\n3. Quadratic Functions and Equations: While 9th grade math may cover linear functions, 10th grade math delves deeper into quadratic functions and equations, including their graphing, solving, and applications.\n\n4. Complex Numbers: 10th grade math typically introduces the concept of complex numbers, which are numbers that have both a real and an imaginary component.\n\n5. Sequences and Series: 10th grade math may include the study of sequences and series, including arithmetic and geometric sequences, and their properties and applications.\n\n6. Exponential and Logarithmic Functions: 10th grade math often covers the properties and applications of exponential and logarithmic functions.\n\nOverall, 10th grade math builds upon the foundation laid in 9th grade, introducing more advanced concepts and applications that prepare students for higher-level mathematics.\n\nEvaluation:\nThe agent's response accurately and comprehensively lists the key concepts that are typically introduced or explored in more depth in 10th grade math, compared to 9th grade math. The response covers a range of important topics, including trigonometry, probability and statistics, quadratic functions and equations, complex numbers, sequences and series, and exponential and logarithmic functions. This response is comprehensive and demonstrates a strong understanding of the differences between 9th and 10th grade math concepts.\n\nPASS"
