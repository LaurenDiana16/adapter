# Import packages
from datetime import date
from dateutil.relativedelta import relativedelta
from pymongo import MongoClient

# Pretend this agent needs to get a certification added for their skill
agent_id="ENTERPRISE_13"

# Connect to MongoDB
client = MongoClient('mongodb+srv://adityasharmasrt_db_user:V4036f6X0xO4qJ0W@nanda.wui3ygq.mongodb.net/')
db = client.agent_facts  # Replace with your database name
collection = db.facts  # Replace with your collection name

# Define the query to find the document
myquery = { "id": agent_id }

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