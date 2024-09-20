LENGTH_STANDARD = 6
word = input("Enter your word: ")
while len(word) < LENGTH_STANDARD:
    print("Invalid")
    word = input("Enter your word: ")
for i in word:
    print("*", end="")