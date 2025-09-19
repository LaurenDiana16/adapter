from pymongo import MongoClient

# Establish a connection to MongoDB
client = MongoClient('your-connection-string') # Replace with your connection string
db = client.Agents  # Replace with your database name
collection = db.AgentFacts  # Replace with your collection name

# Define the query criteria
field_name = "skills.description"  # The field to filter by
field_value = "aerospace engineering"  # The value to match
field_extract = "endpoints" # The field you wish to extract

# Query for documents and project only the field_extract field
# The first argument to find() is the query filter.
# The second argument to find() is the projection, where 1 means include and 0 means exclude.
# We include field extract and exclude all other fields implicitly by not specifying them.
cursor = collection.find({field_name: field_value}, {field_extract: 1})

# Extract the documents
ids = [doc[field_extract] for doc in cursor]

# Save the retrieved values to a file called urls.txt
file_name = 'urls.txt'
with open(file_name, 'w') as file_object:
    for doc_id in ids:
        file_object.write(doc_id['static'][0]+'\n')

# Close the MongoDB connection
client.close()