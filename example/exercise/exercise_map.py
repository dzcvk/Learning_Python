def func(val):
    ret=val*5+10
    return ret

ret = map(func,[1,2,5])
print(type(ret))
print(list(ret))
