# test file

def celsius_to_farenheit(c):
    return c * 9/5 + 32

temp = float(input("Enter temp in C: "))
if temp < -273.15:
    print("This is an impossible temperature, less than absolute zero.")
else:
    print(celsius_to_farenheit(temp))
