#!/usr/bin/env python3
import os
from nanda_adapter import NANDA
from langchain_core.prompts import ChatPromptTemplate
#from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_anthropic import ChatAnthropic

def create_improvement():
    """Create a LangChain-powered 10th grade math improvement function"""

    # Initialize the LLM
    llm = ChatAnthropic(
        api_key=os.getenv("ANTHROPIC_API_KEY"),
        model="claude-3-haiku-20240307"
    )

    # Create a prompt template
    question ="""Please provide answers to the following 5 questions. \
1. What concepts do you learn in 10th grade math that you do not learn in 9th grade math? \
2. Can you teach me a small part of 10th grade math? \
3. One number is 2.5 times as much as another number. What could the numbers be? \
4. If you give me any right triangle with one angle 30 degrees can you predict the ratio of sides? \
5. What is function notation? What is the domain in a math problem?
    """

    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a AI assistant who knows up to 10th grade mathematics."),
        ("human", question)
    ])

    # Create the chain
    chain = prompt | llm | StrOutputParser()

    def improvement(message_text: str) -> str:
        """Ask about 10th grade math"""
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

    # Create pirate improvement function
    improvement_logic = create_improvement()

    # Initialize NANDA with pirate logic
    nanda = NANDA(improvement_logic)

    # Start the server
    print("Starting 10th Grade Math Agent with LangChain...")

    domain = os.getenv("DOMAIN_NAME", "localhost")

    if domain != "localhost":
        # Production with SSL
        nanda.start_server_api(os.getenv("ANTHROPIC_API_KEY"), domain)
    else:
        # Development server
        nanda.start_server()

if __name__ == "__main__":
    main()
