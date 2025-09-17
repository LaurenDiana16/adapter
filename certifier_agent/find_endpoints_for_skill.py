from pymongo import MongoClient
from bson.objectid import ObjectId

# Establish a connection to MongoDB
client = MongoClient('mongodb://18.206.173.193:27017/') # Replace with your MongoDB connection string
db = client.Agents  # Replace with your database name
collection = db.AgentFacts  # Replace with your collection name

# Define the query criteria
field_name = "skills.id"  # The field to filter by
field_value = "10th grade mathematics"  # The value to match
field_extract = "endpoints"

# Query for documents and project only the field_extract field
# The first argument to find() is the query filter.
# The second argument to find() is the projection, where 1 means include and 0 means exclude.
# We include field extract and exclude all other fields implicitly by not specifying them.
cursor = collection.find({field_name: field_value}, {field_extract: 1})

# Extract the documents
ids = [doc[field_extract] for doc in cursor]

# Save the retrieved values
file_name = 'urls.txt'
with open(file_name, 'w') as file_object:
    for doc_id in ids:
        file_object.write(doc_id['static'][0]+'\n')

# Close the MongoDB connection
client.close()