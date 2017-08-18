#get c to f function
import main

#exercise's temperature list
temperatures=[10,-20,-289,100]
file = open("example5.txt", 'w')

for temp in temperatures:
    result = main.c_to_f(temp)
    if result is not None:
        file.write(str(result) + '\n')

file.close()
