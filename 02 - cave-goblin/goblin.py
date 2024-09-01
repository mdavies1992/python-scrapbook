heroactions = ["1] - Attack", "2] - Block", "3] - Run Away!"]
goblinactions = ["Stab", "Growl"]

def determineheroaction():
    print("- ACTIONS AVAILABLE: -")
    for action in heroactions:
        print(action)
    return input("What action do you want to take (input number): ")


print("You are in a cave, facing down an evil goblin with a very pointy stick. It's time to fight!")
print("-")
print(determineheroaction())
