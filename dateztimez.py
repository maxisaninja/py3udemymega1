import datetime

# current time in pretty string:
filename = datetime.datetime.now().strftime("%a %d %b %Y %H %M")

with open(filename + '.txt', 'a+') as file:
    file.seek(0)
    content = file.read()
    file.write('')
