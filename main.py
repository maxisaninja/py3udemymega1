"""

The function c_to_f(c) converts a valid (absolute zero or greater) temperature
to farenheit from celsius, returning the float value.

Excessively cold temperatures return None.

"""
def c_to_f(c):
    if c < -273.15:
        return None
    else:
        return c * 9/5 + 32

def main():
    temp = float(input("Enter temp in C: "))
    print(c_to_f(temp))

if __name__ == '__main__':
    main()
