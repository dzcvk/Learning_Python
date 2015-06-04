from pymongo import MongoClient
client = MongoClient('localhost', 27017)

database = "MyLibs"
collection = "EleDeviceLib"


for Items in client[database][collection].find():
    print(Items)
