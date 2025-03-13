import pymongo 
import pymongo.mongo_client
url ="mongodb+srv://singhsparsh2004:FfrFEVwZ90DFVyKv@sparsh.ug3fb.mongodb.net/"

client=pymongo.MongoClient(url)

db=client["store"]
db.create_collection('db_connectionṇ')

