import math  # Import the math module for square root function

print("This is a Simple calculator.")
print("To perform the function of what you want, type the respective numbers of the function given below.")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Square")
print("6. Power")
print("7. Square Root")
print("8. Absolute Value")

operation = input("What operation would you like to perform? (Enter the corresponding number of the function): ")
num1 = float(input("Type in the first number: "))
num2 = float(input("Type in the second number: "))

# ADDITION
if operation == "1":
    result = num1 + num2
    print("The ADDITION of the two numbers is:", result)

# SUBTRACTION
elif operation == "2":
    result = num1 - num2
    print("The SUBTRACTION of the two numbers is:", result)

# MULTIPLICATION
elif operation == "3":
    result = num1 * num2
    print("The MULTIPLICATION of the two numbers is:", result)

# DIVISION
elif operation == "4":
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = num1 / num2
        print("The DIVISION of the two numbers is:", result)

# SQUARE
elif operation == "5":
    result = num1 ** 2
    print("The SQUARE of the number is:", result)

# POWER
elif operation == "6":
    expNo = int(input("Type in the exponential number (only integers allowed): "))
    result = num1 ** expNo
    print(f"The POWER of the number {num1} is:", result)

# SQUARE ROOT
elif operation == "7":
    if num1 < 0:
        print("Error: Cannot calculate square root of a negative number.")
    else:
        result = math.sqrt(num1)
        print(f"The SQUARE ROOT of the number {num1} is:", result)

# ABSOLUTE VALUE
elif operation == "8":
    result = abs(num1)
    print(f"The ABSOLUTE VALUE of the number {num1} is:", result)

else:
    print("Invalid Value!")
    print("Try again......")

