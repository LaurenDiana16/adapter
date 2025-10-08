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
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a AI assistant who does not know aerospace engineering."),
        ("human", "{message}")
    ])

    print('prompt', prompt)

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
    print("Starting Non-Aerospace Engineering Agent with LangChain...")

    domain = os.getenv("DOMAIN_NAME", "localhost")

    if domain != "localhost":
        # Production with SSL
        nanda.start_server_api(os.getenv("ANTHROPIC_API_KEY"), domain)
    else:
        # Development server
        nanda.start_server()

if __name__ == "__main__":
    main()
