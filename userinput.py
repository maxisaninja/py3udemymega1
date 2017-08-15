# user input
def currency_convert(rate, euros):
    dollars = rate * euros
    return dollars

r=input("Enter rate: ")
e=input("Enter number of euro: ")
print(currency_convert(float(r), float(e)))
