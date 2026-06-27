while True:

    # Get first number safely
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Get second number safely
    while True:
        try:
            num2 = float(input("Enter the second number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    operator = input("Enter operator (+, -, *, /): ")

    if operator == "+":
        print(f"Result: {num1 + num2:.2f}")

    elif operator == "-":
        print(f"Result: {num1 - num2:.2f}")

    elif operator == "*":
        print(f"Result: {num1 * num2:.2f}")

    elif operator == "/":
        if num2 == 0:
            print("Division by 0 is not possible")
        else:
            print(f"Result: {num1 / num2:.2f}")

    else:
        print("Invalid operator")

    end_run = input("Press 'q' to quit or Enter to continue: ")

    if end_run.lower() == "q":
        print("Goodbye and see you again")
        break