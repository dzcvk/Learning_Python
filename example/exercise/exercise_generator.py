def generator():
    ret=1
    yield ret
    ret=ret+1
    yield ret
    for index in range(4):
        ret=ret+index
        yield ret


print(list(generator()))
for index in generator():
    print(index)
