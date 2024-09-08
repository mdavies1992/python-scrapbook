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
nextposition = "x"
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
        print("You are at the goal!")
    elif currentposition == "d":
        print("You can move Up [U], Down [D] or Right [R]")
    elif currentposition == "e":
        print("You can move Up [U], Down [D], Left [L] or Right [R]")
    elif currentposition == "f":
        print("You can move Up [U], Down [D] or Left [L]")
    elif currentposition == "g":
        print("You can move Up [U] or Right [R]")
        complete = True
    elif currentposition == "h":
        print("You can move Up [U], Left [L] or Right [R]")
    elif currentposition == "i":
        print("You can move Up [U] or Left [L]")
    else:
        print("I don't know how you got here, but you're off the grid now, good luck.")
        complete = True

def choosemove(currentposition):
    unlock = False
    if unlock != True:
        action = input("What direction would you like to move in?: ")
        if action == "U":
            print("You move upwards.")
            currentposition = ""
            unlock = True

def updategrid(choice):
    print("a")


print("- GAME START -")
print("You are in the bottom-left corner of this grid. You can move one square in x and y axis', depending on your location. Find your way to the top-right of the grid.")
printgrid()
while complete != True:
    listactions(currentposition)
    if complete != True:
        choice = choosemove(currentposition)
        updategrid(choice)
        complete = True
print("- GAME END -")
