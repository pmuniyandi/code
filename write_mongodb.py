def get_database():
    from pymongo import MongoClient
    import pymongo
    CONNECTION_STRING = "mongodb+srv://pmuniyandi:muni0303@cluster0.ije3c.gcp.mongodb.net/hospital?retryWrites=true&w=majority"
             #let url = `mongodb://pmuniyandi:muni0303@cluster0-shard-00-00-ije3c.gcp.mongodb.net:27017/hospital?authSource=admin&compressors=disabled&gssapiServiceName=mongodb&replicaSet=Cluster0-shard-0&ssl=true`;

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    from pymongo import MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database for our example (we will use the same database throughout the tutorial
    return client #client['networkHospital']
    
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":    
    
    # Get the database
    dbname = get_database()
    cursor = dbname["hospital"]
    rec = cursor["networkHospital"]
    x = rec.find_one()
    #for document in rec:
    print(x)