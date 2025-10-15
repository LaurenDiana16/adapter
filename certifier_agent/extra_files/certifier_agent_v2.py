# Import packages
from tkinter.font import _MetricsDict
import requests
from bs4 import BeautifulSoup
from langchain_core.documents import Document
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
import os

# Scrape the main page to find all of the individual dataset entries
url = 'https://visualization.osdr.nasa.gov/biodata/api/v2/datasets/'
response = requests.get(url)
html_content = eval(response.text)
all_values = []
for inner_dict in html_content.values():
    for value in inner_dict.values():
        all_values.append(value)

# Use a subset of the data
sample_data = all_values[0:5]

# Prepare the data/choose the data we care about
data_dict = {}
for dataset_url in sample_data:
    response = requests.get(dataset_url)
    html_content = eval(response.text)
    #flatten the content one level
    key = dataset_url.split('/dataset/')[1].split('/')[0]
    html_content = html_content[key]
    data_dict[key] = {}
    data_dict[key]['metadata'] = {"mission_name":html_content['metadata']['mission']['name']}
    data_dict[key]['value'] = html_content['metadata']['study description']

# Transform the data into a format compatible with RAG
documents = []
for key, item in data_dict.items():
    doc_content = item["value"]
    doc_metadata = item["metadata"]
    doc_metadata["original_key"] = key  # Add original key to metadata for reference
    documents.append(Document(page_content=doc_content, metadata=doc_metadata))

# Initialize embedding model
embeddings = OpenAIEmbeddings() # Replace with your chosen embedding model

# Create a vector store from the documents
vectorstore = Chroma.from_documents(documents, embeddings)

# Create a retriever from vector store
retriever = vectorstore.as_retriever()

# Initialize LLM
llm = ChatAnthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY"),
    model="claude-3-haiku-20240307"
) # Replace with your chosen LLM

# Define a prompt template
prompt = ChatPromptTemplate.from_template("""Answer the question based only on the following context:
{context}

Question: {question}
""")

# Construct the RAG chain
rag_chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

# Generate synthetic questions and answers to test the expert agent against
query = "Which mission names studied Drosophila?"
response = rag_chain.invoke(query)
print(response)

# Aerospace engineering -> using unclass NASA dataset as simulated "knowledge base"
# Ahead of time, you generate a RAG over the dataset for the certifier agent

# Evaluation process
# The certifier agent conducts its assessment in a structured, multi-step process.
# 1. Generate a test query: The certifier agent autonomously generates a test query from its ground-truth dataset.\
#    This could be hand-picked examples or Q/A generated using the RAG.
# 2. Send query to candidate agent: The test query is passed to the agent under evaluation.
# 3. Candidate agent provides output: The candidate agent processes the query and generates a response.
# 4. Certifier agent evaluates response: The certifier uses its RAG pipeline and LLM-as-a-judge capabilities to \
#    evaluate the candidate's response against the ground-truth data from its knowledge base.
# 5. Score and report: The certifier generates a report based on several key metrics. 

# Evaluation metrics
# 1. Context relevance: Measures if the retrieved context is relevant to the user query.
# 2. Faithfulness/Correctness: Evaluates if the generated answer is factually supported by the retrieved context.
# 3. Answer relevance: Measures if the generated answer directly addresses the user's query.
# 4. Answer similarity: Compares the expert agent's answer to the "golden" answer using an embedding-based \
#    approach to determine semantic similarity. 