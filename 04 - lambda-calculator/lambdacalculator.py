# OBJECTIVE: Using Lambda functions, create a script that will
# take 2 numbers and an operator from the user,
#  then calculate and state the result.


print("- START -")
print("Welcome to the Lambda Calculator.")
first_number = int(input("Please enter the first number: "))
second_number = int(input("Please enter the second number: "))
operator = input("Please enter the operator for the two numbers [ + | - | / | * ]: ")
if operator == "+":
    result = lambda a, b: a + b
    print(f"The total is: {result(first_number, second_number)}")
elif operator == "-":
    result = lambda a, b: a - b
    print(f"The total is: {result(first_number, second_number)}")
elif operator == "/":
    result = lambda a, b: a / b
    print(f"The total is: {result(first_number, second_number)}")
elif operator == "*":
    result = lambda a, b: a * b
    print(f"The total is: {result(first_number, second_number)}")
else:
    print("That is an invalid operator. Please try again.")

print("- END -")
