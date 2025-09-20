## Index

1. find_endpoints_for_skill.py: A python script that searches an AgentFacts collection in a MongoDB database for all agent names that possess a particular skill. It outputs their associated endpoints to the specified filepath.

> python find_endpoints_for_skill.py "aerospace engineering" "urls.txt"

2. adapter/nanda_adapter/examples/demo/langchain_ae_agent.py and langchain_ae_certifier.py: Langchain aerospace engineering expert agent and certifier. Refer to adapter/nanda_adapter/examples/demo/README.md for instructions on how to run them.

3. adapter/nanda_adapter/examples/demo/langchain_se_agent.py and langchain_se_certifier.py: Langchain systems engineering expert agent and certifier. Refer to adapter/nanda_adapter/examples/demo/README.md for instructions on how to run them.

4. adapter/nanda_adapter/examples/demo/langchain_srm_agent.py and langchain_srm_certifier.py: Langchain safety and risk management expert agent and certifier. Refer to adapter/nanda_adapter/examples/demo/README.md for instructions on how to run them.

5. adapter/nanda_adapter/examples/demo/find_certification_evaluation.py: A python script that searches through the conversation logs from a certifier agent and extracts information regarding newly certified agents into a "certifications.jsonl" file.

> python find_certification_evaluation.py "conversations_xx.log" "aerospace engineering"

6. update_agent_facts.py: A python script that uses a "certifications.jsonl" file to update the records for newly certified agents in the AgentFacts collection in a MongoDB database with the certifications.

> python update_agent_facts.py "certifications.jsonl"