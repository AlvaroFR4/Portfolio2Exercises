# Write a program that asks for two numbers and then asks for the operation to perform (+, -, * or /).
# Print the result, and print an error message if the operation is not valid or if the user tries to divide by
# zero.

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ").strip()

if operation == "+":
    print(f"Result: {num1 + num2}")
elif operation == "-":
    print(f"Result: {num1 - num2}")
elif operation == "*":
    print(f"Result: {num1 * num2}")
elif operation == "/":
    if num2 == 0:
        print("Error: Cannot divide by zero.")
    else:
        print(f"Result: {num1 / num2}")
else:
    print("Error")