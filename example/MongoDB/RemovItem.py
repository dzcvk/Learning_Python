from pymongo import MongoClient
client = MongoClient('localhost', 27017)

print("-------------previous------------------------------")
for Items in client.MyLibs.EleDeviceLib.find({},{"_id":False}):
    print(Items)


Item =  {
            "DeviceName": "1N2016",
            #"Umax(V)": "100"
        }

client.MyLibs.EleDeviceLib.remove(Item)
print("-------------afterwards-----------------------------")
for Items in client.MyLibs.EleDeviceLib.find({},{"_id":False}):
    print(Items)
