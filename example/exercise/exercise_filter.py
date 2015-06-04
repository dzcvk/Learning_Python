def func(val):
    if val>10:
        return True
    else:
        return False
#filter return a iterators type data
ret=filter(func,[1,2,10,11,12])
print(type(ret))
#turn iterators data into list type data
print(list(ret))
