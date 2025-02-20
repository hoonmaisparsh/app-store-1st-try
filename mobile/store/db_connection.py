import pymongo 
import pymongo.mongo_client
url ="mongodb+srv://singhsparsh2004:FfrFEVwZ90DFVyKv@sparsh.ug3fb.mongodb.net/?retryWrites=true&w=majority&appName=sPARSH"

client=pymongo.MongoClient(url)

db=client["store"]

