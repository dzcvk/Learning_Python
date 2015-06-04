print('---------slice-------------')
numList=[0,1,2,3,4,5,6,7,8,9]
#[start:stop]
print(numList[2:5])
#[start:stop:step]
print(numList[1:10:2])
print(numList[1:-1:2])
#-------------------------------------
# in [roller:range,iter...]
print('----------for--------------')
for index in range(10):
    print(index)
#-------------------------------------
print('----------print------------')
val=10
print('the val is %d'%val)
print('the val is',val)
