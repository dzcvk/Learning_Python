def InsrtItem():
    from pymongo import MongoClient
    client = MongoClient('localhost', 27017)

    print("-------------Previous------------------------------")
    for Items in client.MyLibs.EleDeviceLib.find({},{"_id": False}):
        print(Items)

    DeviceName = input("Please type in the Device Name: ")
    Umax = input("Please type in the maximum voltage: ")

    Item =  {
               "DeviceName": DeviceName,
               "Umax(V)": Umax,
            }

    client.MyLibs.EleDeviceLib.insert(Item)

    print("-------------Afterwards----------------------------")
    for Items in client.MyLibs.EleDeviceLib.find({},{"_id":False}):
        print(Items)
