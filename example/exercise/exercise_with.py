with open('exercise_with.txt',mode='r+') as file:
    file.write('first line\n')
    line=file.readlines()
print(line)
