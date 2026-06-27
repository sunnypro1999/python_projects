#get first number, second number and mathematical operator 

while(True):
#Multiple tries for getting the first number from the user
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            break#was not inside the program they i typed out and this cause the loop to not end
        # as such this loop does not end hence the following code after this while loop will never run
        except ValueError:
            print("I need you to enter a number")
        
    
    while True:

        try:
            num2 = float(input("Enter the second number: "))
            break
        except ValueError:
            print("Inputted variable was not a number, please retry")     
    
    
    operator = input("Choose your mathematical operator ( + , - , * , / , % , **) : ")

    if operator == "+":
        print(f"Result: {num1 + num2:.2f}")

    elif operator == "-":
        print(f"Result: {num1-num2:.2f}")

    elif operator == "*":
        print(f"Result: {num1*num2:.2f}")

    elif operator == "/":
        '''
    this print statement will cause an 
    print(f"{num1/num2:.2f}")
        '''
    #did not think about division by 0, when anything division by 0 an error will prompt
        if num2==0 :
            print("divison by 0 is not possible")
    
        else:
            print(f"Result: {num1/num2:.2f}")

    #making a program to take the "**" , "%"
    elif operator == "**":
        print(f"Results: {num1 ** num2:.2f}")
    
    elif operator == "%":
        if num2==0:
            print("Modular by '0' is not possible")
        else:
            print(f"Results: {num1 % num2:.2f}")
    
    else: #if the inputed operator is not any of the selected ones that we programed
        print("Invalid operator ")
    end_run=input("press 'q' if you would like to exit or press 'enter' if you would like to continue")

    if end_run.lower() == "q": #converts the input to lower case, "Q" will still read as "q"
        print("Good bye and see you again ")
        break
    


 