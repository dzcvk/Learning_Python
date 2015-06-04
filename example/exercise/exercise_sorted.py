friends = [199,200,158,165,201,180,170,160,140,199]
friends = sorted(friends)
print('reverse:false\n'+str(friends))
friends = sorted(friends,reverse=True)
print('reverse:true\n'+str(friends))
#------------------------------------------------------------
print('-----------------------------------------------------')
def heightClass(val):
    if val>180:
        return 'tall'
    elif val<160:
        return 'short'
    else:
        return 'middle'


friends = [199,200,158,165,201,180,170,160,140,199]
friends = sorted(friends,key=heightClass)
print(type(friends))
print(friends)
#------------------------------------------------------------
print('-----------------------------------------------------')
friends = {1:'a',3:'b',2:'c',4:'d'}
print('before:type of friends is '+str(type(friends)))
print(friends)
friends = sorted(friends.items(),key=lambda field:field[0],reverse=True)
print('after: type of friends is '+str(type(friends)))
print(friends)
