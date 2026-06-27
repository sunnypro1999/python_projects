#get first number, second number and mathematical operator 

while(1):

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operator = input("can u give me your mathematical operator (+,-,*,/) : ")

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
    else:
        print("Invalid operator ")
    end_run=input("press 'q' if you would like to exit or press 'enter' if you would like to continue")

    if end_run == "q":
        print("Good bye and see you again")
        break
    


 