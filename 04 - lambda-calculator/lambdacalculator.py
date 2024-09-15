# OBJECTIVE: Using Lambda functions, create a script that will
# take 2 numbers and an operator from the user,
#  then calculate and state the result.
import operator

# FIRST VERSION - Works, but is not very DRY
# print("- START -")
# print("Welcome to the Lambda Calculator.")
# first_number = int(input("Please enter the first number: "))
# second_number = int(input("Please enter the second number: "))
# oper = input("Please enter the oper for the two numbers [ + | - | / | * ]: ")
# if oper == "+":
#     result = lambda a, b: a + b
#     print(f"The total is: {result(first_number, second_number)}")
# elif oper == "-":
#     result = lambda a, b: a - b
#     print(f"The total is: {result(first_number, second_number)}")
# elif oper == "/":
#     result = lambda a, b: a / b
#     print(f"The total is: {result(first_number, second_number)}")
# elif oper == "*":
#     result = lambda a, b: a * b
#     print(f"The total is: {result(first_number, second_number)}")
# else:
#     print("That is an invalid operator. Please try again.")

# print("- END -")

# SECOND VERSION - Using lambda, but also importing operator/using to better create shorter code
# using the imported "operator" functionality, I set up a basis for what values equal operators here
ops = { "+": operator.add, "-": operator.sub, "/": operator.truediv, "*": operator.mul }
choice = "Y"

print("- START -")
while choice != "N":
    print("Welcome to the Lambda Calculator.")
    first_number = int(input("Please enter the first number: "))
    second_number = int(input("Please enter the second number: "))
    operator = input("Please enter the operator for the two numbers [ + | - | / | * ]: ")
    if operator == "+" or "-" or "/" or "*":
        print(f"The total is: {ops[operator](first_number, second_number)}")
    else:
        print("That is an invalid operator. Please try again.")
    choice = input("Would you like to make another caluclation? [Y / N]: ").upper()
print("- END -")
