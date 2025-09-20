## Index

1. Search MongoDB database AgentFacts collection for agents with a skill: find_endpoints_for_skill.py
```
python find_endpoints_for_skill.py "aerospace engineering" "urls.txt"
```

2. Langchain aerospace engineering expert agent and certifier: adapter/nanda_adapter/examples/demo/langchain_ae_agent.py and langchain_ae_certifier.py (instructions for how to run are in associated README.md)

3. Langchain systems engineering expert agent and certifier: adapter/nanda_adapter/examples/demo/langchain_se_agent.py and langchain_se_certifier.py (instructions for how to run are in associated README.md)

4. Langchain safety and risk management expert agent and certifier: adapter/nanda_adapter/examples/demo/langchain_srm_agent.py and langchain_srm_certifier.py (instructions for how to run are in associated README.md)

5. Search certifier agent's conversation logs for agents that have passed: adapter/nanda_adapter/examples/demo/find_certification_evaluation.py
```
python find_certification_evaluation.py "conversations_xx.log" "aerospace engineering"
```

6. Update AgentFacts records for newly certified agents: update_agent_facts.py
```
python update_agent_facts.py "certifications.jsonl"
```