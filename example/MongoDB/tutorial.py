from pymongo import MongoClient
#client = MongoClient()
client = MongoClient('localhost', 27017)
#db = client.MyLibs
db = client.MyTestLibs
collection = db.EleDeviceLib

Item =  {
           "DeviceName": "1N2008",
           "Umax(V)": "20",
        }
#collection.insert(post)
collection.save(Item)
#db.posts.find_one()
for Item in client.MyLibs.EleDeviceLib.find():
    print(Item)
