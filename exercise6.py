import os
import datetime

#with (os.g
inputfiledir = "Sample-Files"
newfilename = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f") + ".txt"

samplefiles = []

for root, dirs, files in os.walk(os.path.join(os.getcwd(),inputfiledir)):
    samplefiles = files
    print(files)
    print(type(files))
    for i in files:
        print(i)

with open(os.path.join(os.getcwd(), newfilename), 'w') as outfile:
    for name in samplefiles:
        with open(os.path.join(os.getcwd(),inputfiledir,name)) as infile:
            outfile.write(infile.read())
            outfile.write("\n")
