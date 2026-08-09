import random

items = ["Rock", "Paper", "Scissor"]

computer = random.choice(items)

user = input("Rock , Paper or Scissor:")

print("COMPUTER CHOOSES", computer)

if user == computer:
    print("Match Draw...")

elif user == "Rock" and computer == "Scissor" :
    print ("User win!!!!")

elif user == "Scissor" and computer == "Rock" :
    print ("User win!!!!")

elif user == "Paper" and computer == "Rock" :
    print ("User Win!!!")

else:
    print("Computer Win!!!")