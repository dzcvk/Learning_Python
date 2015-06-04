def add(param1,param2):
	ret=param1+param2
	return ret

print(add(1,2))
print('--------------------------------')
#-----------------------
def selfReduce(param):
	param[0]=param[0]-1
	print(param)
val=[10,1]
selfReduce(val)
print(val)
print('--------------------------------')
#-----------------------
def func1(*param):
	print(type(param))
	print(param)
func1(1,2,3,4)
print('--------------------------------')
#-----------------------
def func2(**param):
	print(type(param))
	print(param)
func2(param1=1,param2='ok')



