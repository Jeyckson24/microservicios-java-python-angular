import pymongo
import certifi

ca = certifi.where()

client = pymongo.MongoClient("mongodb+srv://votingsystem:123456a*@votingsystem.zsoamye.mongodb.net/?retryWrites=true&w=majority", tlsCAFile = ca)
db = client["app_votingsystem"]

print(db.list_collection_names())

#Crud Mesa

_mesa_colleccion = db.mesas


print (_mesa_colleccion.find())