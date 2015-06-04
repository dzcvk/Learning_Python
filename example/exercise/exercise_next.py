file=open('exercise_next.txt')
print(type(file))
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print('-------------------')
for line in open('exercise_next.txt'):
    print(line)

