# print(" | a | b | c |")
# print("---+---+---+---")
# print(" | d | e | f |")
# print("---+---+---+---")
# print(" | g | h | i |")
# print("---+---+---+---")

# straightline = "---+---+---+---"
topline = " | - | - | - |"
middleline = " | - | - | - |"
bottomline = " | - | - | - |"
currentposition = "g"
complete = False

def printgrid():
    print(topline)
    print("---+---+---+---")
    print(middleline)
    print("---+---+---+---")
    print(bottomline)
    print("---+---+---+---")

def listactions(currentposition):
    global complete
    if currentposition == "a":
        print("You can move Down [D] or Right [R]")
    elif currentposition == "b":
        print("You can move Down [D], Left [L] or Right [R]")
    elif currentposition == "c":
        print("You are at the goal! You win!")
        complete = True
    elif currentposition == "d":
        print("You can move Up [U], Down [D] or Right [R]")
    elif currentposition == "e":
        print("You can move Up [U], Down [D], Left [L] or Right [R]")
    elif currentposition == "f":
        print("You can move Up [U], Down [D] or Left [L]")
    elif currentposition == "g":
        print("You can move Up [U] or Right [R]")
    elif currentposition == "h":
        print("You can move Up [U], Left [L] or Right [R]")
    elif currentposition == "i":
        print("You can move Up [U] or Left [L]")
    else:
        print("I don't know how you got here, but you're off the grid now, good luck.")
        complete = True

def updategrid(action):
    global currentposition
    if currentposition == "a":
        if action == "R":
            print("You move to the Right.")
            currentposition = "b"
        elif action == "D":
            print("You move Downwards.")
            currentposition = "d"
        else:
            print("That is not a valid move.")
    elif currentposition == "b":
        if action == "L":
            print("You move to the Left.")
            currentposition = "a"
        elif action == "R":
            print("You move to the Right.")
            currentposition = "c"
        elif action == "D":
            print("You move Downwards.")
            currentposition = "e"
        else:
            print("That is not a valid move.")
    elif currentposition == "d":
        if action == "U":
            print("You move Upwards.")
            currentposition = "a"
        elif action == "R":
            print("You move to the Right.")
            currentposition = "e"
        elif action == "D":
            print("You move Downwards.")
            currentposition = "g"
        else:
            print("That is not a valid move.")
    elif currentposition == "e":
        if action == "U":
            print("You move Upwards.")
            currentposition = "b"
        elif action == "L":
            print("You move to the Left.")
            currentposition = "d"
        elif action == "R":
            print("You move to the Right.")
            currentposition = "f"
        elif action == "D":
            print("You move Downwards.")
            currentposition = "h"
        else:
            print("That is not a valid move.")
    elif currentposition == "f":
        if action == "U":
            print("You move Upwards.")
            currentposition = "c"
        elif action == "L":
            print("You move to the Left.")
            currentposition = "e"
        elif action == "D":
            print("You move Downwards.")
            currentposition = "i"
        else:
            print("That is not a valid move.")
    elif currentposition == "g":
        if action == "U":
            print("You move Upwards.")
            currentposition = "d"
        elif action == "R":
            print("You move to the Right.")
            currentposition = "h"
        else:
            print("That is not a valid move.")
    elif currentposition == "h":
        if action == "U":
            print("You move Upwards.")
            currentposition = "e"
        elif action == "L":
            print("You move to the Left.")
            currentposition = "g"
        elif action == "R":
            print("You move to the Right.")
            currentposition = "i"
        else:
            print("That is not a valid move.")
    elif currentposition == "i":
        if action == "U":
            print("You move Upwards.")
            currentposition = "f"
        elif action == "L":
            print("You move to the Left.")
            currentposition = "h"
        else:
            print("That is not a valid move.")

print("- GAME START -")
print("You are in the bottom-left corner of this grid. You can move one square in x and y axis', depending on your location. Find your way to the top-right of the grid.")
printgrid()
while complete != True:
    listactions(currentposition)
    if complete != True:
        action = input("What direction would you like to move in?: ")
        updategrid(action)
print("- GAME END -")
