y = True

while y == True:

    x = input("enter a number ")

    try:
       #x = float(x); # converting the data type of the input into a number
        x = int(x)       #if a number is entered, it can be converted and the code will continue to run 
        y = False  
    except: 
        print("Invalid input. Please enter a valid number.")
print(f" thanks for entering a number, you keyed in {x} and the data type is {type(x)}")
