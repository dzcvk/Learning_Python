re=iter(range(10))
try:
    for index in range(20):
        print(re.__next__())
        print(haha)
except:
    print('error',index)
