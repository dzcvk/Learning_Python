re=iter(range(10))
try:
    for index in range(20):
        print(re.__next__())
except StopIteration as e:
    print('ended when index =',index)
