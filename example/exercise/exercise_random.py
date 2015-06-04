import random

lines=input('please type in the number of lines \n>>')
raws=input('please type in the number of raws \n>>')

weishu=input('please type in the weishu of number \n>>')
pointpos=input('please type in the point position \n>>')

Bweishu=10**int(weishu)
Bpointpos=10**int(pointpos)

rnd=random.Random()

for line in range(int(lines)):
    for raw in range(int(raws)):
        print(rnd.randint(0,Bweishu)/Bpointpos,'  ',end='')
    print('\n')

print('\n','this is the end of random number generator')
