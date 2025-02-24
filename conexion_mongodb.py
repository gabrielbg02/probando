from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient ('localhost',27017)

database = client.prueba

persona = database.persona

#persona.insert_one ({"nombre" : "raul" , "edad" : 55})

#persona.insert_one ({"nombre" : "luis" , "edad" : 55})

#persona.update_one ({"_id": ObjectId ("67bcc0216e59e9327ba087f9") } , {"$set" : {"edad" : 22}})

#persona.update_many ({"edad" : 66} , {"$set" : {"edad" : 44}})


#persona.delete_one ({"edad" : 22})

#persona.delete_many ({ "edad" : 55})

#for nombre in persona.find():
#    print (nombre)

for persona in persona.find():
    print (persona)