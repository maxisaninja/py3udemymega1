# test file

def c_to_f(c):
    if c < -273.15:
        return "This is an impossible temperature, less than absolute zero."
    else:
        return c * 9/5 + 32

def main():
    temp = float(input("Enter temp in C: "))
    print(c_to_f(temp))

if __name__ == '__main__':
    main()
