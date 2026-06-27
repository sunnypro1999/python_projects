#going to have a limit on the number of tries u get 

password = input("Create your password ")
attempt=0

while attempt<3:
    login = input("To login please enter your password ")
    if password == login:
        print("Login successful")
        break
    else:
        attempt+=1
        print("attempt number ", attempt)

if attempt==3 and password !=login:   
    print("too many attempts,sorry but no more tries")



