complete = 0
heroactions = ["1] - Attack", "2] - Block", "3] - Run Away!"]
goblinactions = ["Stab", "Growl"]
choice = ""
herohp = 10
goblinhp = 10

def healthcheck():
    print(f"# Your Hit Points are at {herohp} #")
    print(f"# The Goblin's Hit Points are at {goblinhp} #")

def determineheroaction():
    print("- ACTIONS AVAILABLE: -")
    for action in heroactions:
        print(action)
    return input("What action do you want to take (input number): ")


print("You are in a cave, facing down an evil goblin with a very pointy stick. It's time to fight!")
print("-")
while complete == 0:
    healthcheck()
    choice = determineheroaction()
    complete += 1
