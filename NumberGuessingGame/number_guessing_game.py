import random

target = random.randint(1,100)

while True:

    userChoice = input("Guess the target or Quit(Q):")

    if (userChoice == "Q"):
        break

    userChoice = int(input("Guess the target: "))
    if (userChoice == target):
        print("Succsessful , Your Guess Is Correct!!")
        break

    elif(userChoice < target):
        print("Your number is smaller , Guess Again.")

    else:
        print("Your number is bigger , Guess Again.")

print("---GAME OVER---")