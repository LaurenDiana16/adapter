# Import packages
from datetime import date
from dateutil.relativedelta import relativedelta
from pymongo import MongoClient
import json

def update_agent_facts(agent_name):
    """Function that adds a certification to a AgentFacts record in the MongoDB database."""

    # Connect to MongoDB
    client = MongoClient('your-connection-string') # Replace with your connection string
    db = client.Agents  # Replace with your database name
    collection = db.AgentFacts # Replace with your collection name

    # Define the query to find the document
    myquery = {"agent_name": agent_name}

    # Get today's date and calculate one year forward
    today = date.today()
    today_string = today.strftime("%Y-%m-%d")
    one_year = today + relativedelta(years=1)
    one_year_string = one_year.strftime("%Y-%m-%d")

    # Define the new values using the $set operator
    newvalues = { "$set": { "certification": 
                            {"level": "certified",
                            "issuer": "NANDA Certification Authority",
                            "issuanceDate": today_string,
                            "expirationDate": one_year_string,
                            "_id":""}}}

    # Perform the update
    collection.update_one(myquery, newvalues)

    return

def load_file(file_path):
    """Load the certifications JSON file."""
    
    with open(file_path, 'r') as f:
        data_list = json.load(f)

    return data_list


# Load in certifications JSON file
file_path = "certifications.jsonl"
data_list = load_file(file_path)

# Update each agent
for item in data_list:
    update_agent_facts(item['agent_name'])