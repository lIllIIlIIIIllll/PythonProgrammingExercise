import random

print("Please input minimal number")
min = int(input())
print("Please input maximal number")
max = int(input())
RandomNumber = random.randint(min,max)
print("Please input the nunmber you guess")
GuessedNumber = int(input())
if GuessedNumber == RandomNumber:
    print("You win, the number is", RandomNumber)
else:
    while(GuessedNumber != RandomNumber):
        print("Guess Again")
        GuessedNumber = int(input())
        if GuessedNumber == RandomNumber:
            print("You win, the number is", RandomNumber)