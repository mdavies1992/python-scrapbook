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
ops = { "+": operator.add, "-": operator.sub, "/": operator.truediv, "*": operator.mul }
print("- START -")
print("Welcome to the Lambda Calculator.")
first_number = int(input("Please enter the first number: "))
second_number = int(input("Please enter the second number: "))
oper = input("Please enter the oper for the two numbers [ + | - | / | * ]: ")
if oper == "+" or "-" or "/" or "*":
    print(f"The total is: {ops[oper](first_number, second_number)}")
else:
    print("That is an invalid operator. Please try again.")

print("- END -")
