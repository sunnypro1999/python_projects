password = input("Create your password ")
login = input("To login please enter your password ")

if password == login:
    print("Login sucessful")
else:
    print("password did not match, please change your password")

    password = input("Please enter your new password ")
    check = input("Please renter your password ")

    if password == check:
        print("login successful")

    else:
        print("password keyed was wrong")
        print("Maximum number of tried keyed in, Goodbye")