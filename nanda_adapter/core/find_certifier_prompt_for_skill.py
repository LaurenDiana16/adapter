from pymongo import MongoClient
import os

def find_certifier_prompt_for_skill(skill):

    # Establish a connection to MongoDB
    client = MongoClient(os.getenv("MONGODB_CONNECTION_STRING")) # Replace with your connection string
    db = client.Agents  # Replace with your database name
    collection = db.CertifierPrompts  # Replace with your collection name

    # Define the query criteria
    field_name = "skill"  # The field to filter by
    field_value = skill  # The value to match
    field_extract = "prompt" # The field you wish to extract

    # Query for documents and project only the field_extract field
    # The first argument to find() is the query filter.
    # The second argument to find() is the projection, where 1 means include and 0 means exclude.
    # We include field extract and exclude all other fields implicitly by not specifying them.
    cursor = collection.find({field_name: field_value}, {field_extract: 1})

    # Extract the documents
    ids = [doc[field_extract] for doc in cursor]

    # Close the MongoDB connection
    client.close()

    return ids[0]