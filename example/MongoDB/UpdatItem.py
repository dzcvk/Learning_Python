from pymongo import MongoClient
client = MongoClient('localhost', 27017)

print("-------------Previous------------------------------")
for Items in client.MyLibs.EleDeviceLib.find({},{"_id": False}):
    print(Items)


Item =  { "DeviceName": "1N2008" }
#ChangeVal = { "DeviceName": "1N2010", "Umax(V)": "90" }
ChangeVal = { "DeviceName": "1N2016" }

client.MyLibs.EleDeviceLib.update( Item, {"$set":ChangeVal}, multi = True, upsert = False )
print("-------------Afterwards----------------------------")
for Items in client.MyLibs.EleDeviceLib.find({},{"Umax(V)":True, "DeviceName":True, "_id":False}):
    print(Items)
