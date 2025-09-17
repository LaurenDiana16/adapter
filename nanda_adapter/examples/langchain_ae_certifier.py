#!/usr/bin/env python3
import os
from nanda_adapter import NANDA
from langchain_core.prompts import ChatPromptTemplate
#from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_anthropic import ChatAnthropic

def create_improvement():
    """Create a LangChain-powered improvement function"""

    # Initialize the LLM
    llm = ChatAnthropic(
        api_key=os.getenv("ANTHROPIC_API_KEY"),
        model="claude-3-haiku-20240307"
    )

    # Create a prompt template
    system_prompt ="""You are a highly skilled AI assistant certified in aerospace engineering. \
    Your job is to evaluate an agent's responses to the following questions and output PASS or FAIL into evaluation.json file. \
    1. Can you explain airfoil theory? Correct answers include explaining how airfoils generate lift by analyzing potential flow and real-flow effects. \
    2. What specialized tools do you use most, and how have you applied them in a recent project? Correct answers include CATIA, ANSYS, NASTRAN, and MATLAB. \
    3. What are some industry standards and practices? Correct answers include FAA, EASA, DO-178C, DO-254.\
    """
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("user", "{message}")
    ])

    # Create the chain
    chain = prompt | llm | StrOutputParser()

    def improvement(message_text: str) -> str:
        """Invoke the chain"""
        try:
            result = chain.invoke({"message": message_text})
            return result.strip()
        except Exception as e:
            print(f"Error in improvement: {e}")
            return f"Error"  # Fallback

    return improvement

def main():
    """Main function to start the agent"""

    # Check for API key
    if not os.getenv("ANTHROPIC_API_KEY"):
        print("Please set your ANTHROPIC_API_KEY environment variable")
        return

    # Create improvement function
    improvement_logic = create_improvement()

    # Initialize NANDA with improvement logic
    nanda = NANDA(improvement_logic)

    # Start the server
    print("Starting Aerospace Engineer Certifier with LangChain...")

    domain = os.getenv("DOMAIN_NAME", "localhost")

    if domain != "localhost":
        # Production with SSL
        nanda.start_server_api(os.getenv("ANTHROPIC_API_KEY"), domain)
    else:
        # Development server
        nanda.start_server()

if __name__ == "__main__":
    main()
