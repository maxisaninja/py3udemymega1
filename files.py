m = ["Line " + str(x) for x in range(1,6)]

with open('example.txt', 'a+') as file:
    file.seek(0)
    content = file.read()
    for line in m:
        file.write(line + '\n')
