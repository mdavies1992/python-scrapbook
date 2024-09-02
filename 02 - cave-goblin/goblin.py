# imports needed for this to work!
import random

# values that are needed and may change during the script:
complete = 0
heroactions = ["1] - Attack", "2] - Block", "3] - Run Away!"]
choice = ""
herohp = 10
goblinhp = 10

# method for determining/stating player hp and goblin hp:
def healthcheck():
    print(f"# Your Hit Points are at {herohp} #")
    print(f"# The Goblin's Hit Points are at {goblinhp} #")

# quick method for determining the players chosen action:
def determineheroaction():
    print("- ACTIONS AVAILABLE: -")
    for action in heroactions:
        print(action)
    return input("What action do you want to take (input number): ")

# method to complete the players action:
def playeraction(choice):
    global goblinhp
    if choice == "1":
        print("You strike the goblin with your trusty blade!")
        damage = random.randint(1, 4)
        print(f"You deal {damage} damage!")
        goblinhp -= damage
    elif choice =="2":
        print("You raise your shield to block an incoming attack!")
    elif choice == "3":
        print("You run away, like a coward!")
    else:
        print("That isn't a number of an action you can take... oh no, you are paralyzed by indecision!")


# method to complete the goblins action:
def goblinaction():
    global herohp
    rng = random.randint(1, 2)
    if rng == 1:
        print("The goblin stabs you with its pointy stick!")
        if choice == "2":
            print("...But you block it with your shield, good job!")
        else:
            damage = random.randint(1, 3)
            print(f"The goblin deals {damage} damage to you!")
            herohp -= damage
    else:
        print("The goblin snarls and growls at you, menacingly!")

# The script and where the magic happens!:
print("You are in a cave, facing down an evil goblin with a very pointy stick. It's time to fight!")
print("-")
while complete == 0:
    healthcheck()
    choice = determineheroaction()
    playeraction(choice)
    if goblinhp <= 0:
        complete += 1
        print("You have slain the goblin, congratulations!")
    elif choice == "3":
        complete += 1
    else:
        goblinaction()
        if herohp <= 0:
            complete += 1
            print("You have been slain to the goblin!")
print("- GAME END -")
