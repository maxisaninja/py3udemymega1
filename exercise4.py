import main

temperatures=[10,-20,-289,100]

for temp in temperatures:
    if main.c_to_f(temp) is not None:
        print(main.c_to_f(temp))
    else:
        print("This is an impossible temperature, less than absolute zero.")
