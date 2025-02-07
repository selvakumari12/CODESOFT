def calculator():
    print("Simple Calculator")
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    # Prompt the user for input
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter the operation (+, -, *, /): ")

        # Perform the calculation
        if operation == "+":
            result = num1 + num2
            print(f"The result of {num1} + {num2} is: {result}")
        elif operation == "-":
            result = num1 - num2
            print(f"The result of {num1} - {num2} is: {result}")
        elif operation == "*":
            result = num1 * num2
            print(f"The result of {num1} * {num2} is: {result}")
        elif operation == "/":
            if num2 != 0:
                result = num1 / num2
                print(f"The result of {num1} / {num2} is: {result}")
            else:
                print("Error: Division by zero is not allowed.")
        else:
            print("Invalid operation. Please choose +, -, *, or /.")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

# Run the calculator
calculator()
