def consonantcheck(input):
    consonants = ["b", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "w", "v", "x", "y", "z"]
    counter = 0
    breakdown = list(input)
    for letter in breakdown:
        if letter.lower() in consonants:
            counter += 1
    return counter



print("01 - Consnant Checker")
word = input("Please input a word or phrase to check for consonants: ")
result = consonantcheck(word)
print(f"The inputted string \"{word}\" has {result} consonants.")
