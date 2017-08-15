password=''
correctpass='python987'
while password != correctpass:
    password = input("Enter password: ")
    if password == correctpass:
        print("Success.")
    else:
        print("Sorry, try again.")
