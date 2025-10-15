from pymongo import MongoClient
import sys

def find_agents_with_skill(skill):
    """Connect to the MongoDB database AgentFacts collection and find agents with a specific skill."""

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

    # Close the MongoDB connection
    client.close()

    return ids

def write_endpoints_file(ids, file_path):
    """Write the agents endpoints to a file."""

    with open(file_path, 'w') as file_object:
        for doc_id in ids:
            file_object.write(doc_id['static'][0]+'\n')

    return

def main(skill, file_path):
    """Find agents with a particular skill and write their associated endpoints to a file."""

    # Find the agent names that have the skill
    ids = find_agents_with_skill(skill)

    # Write their associated endpoints to a file
    write_endpoints_file(ids, file_path)

    return

if __name__ == "__main__":
    skill = sys.argv[1]
    file_path = sys.argv[2]
    main(skill, file_path)