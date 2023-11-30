while True:
    csv1 = float(input("Press 1 for Addition\nPress 2 for Subtraction\nPress 3 for Multiplication\nPress 4 for Division\nPress 5 for Power function\nPress 6 for Exit: "))
    
    if csv1 == 1:
        num1 = float(input("Enter the first Number: "))
        num2 = float(input("Enter the second Number: "))
        result = num1 + num2
        print("Answer:", result)
    elif csv1 == 2:
        num1 = float(input("Enter the first Number: "))
        num2 = float(input("Enter the second Number: "))
        result = num1 - num2
        print("Answer:", result)
    elif csv1 == 3:
        num1 = float(input("Enter the first Number: "))
        num2 = float(input("Enter the second Number: "))
        result = num1 * num2
        print("Answer:", result)
    elif csv1 == 4:
        num1 = float(input("Enter the first Number: "))
        num2 = float(input("Enter the second Number: "))
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
            print("Answer:", result)
    elif csv1 == 5:
        base = float(input("Enter the base: "))
        exponent = float(input("Enter the exponent: "))
        result = base ** exponent
        print("Answer:", result)
    elif csv1 == 6:
        print("Exiting the calculator.")
        break
    else:
        print("Invalid choice, please select a valid option (1/2/3/4/5/6).")
