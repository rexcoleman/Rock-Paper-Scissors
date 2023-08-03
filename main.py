rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

gameImages = [rock, paper, scissors]

userChoice = int(input("What do you want to choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n"))

if userChoice >= 3 or userChoice < 0:
    print("You picked an invalid number")

else:
    print(f"You chose: {gameImages[userChoice]}")
    computerChoice = random.randint(0, 2)
    print(f"Computer Chose: {gameImages[computerChoice]}")

    if userChoice == 0 and computerChoice == 2:
        print("You win!")
    elif computerChoice > userChoice:
        print("You lose!")
    elif computerChoice == userChoice:
        print("Draw")
    elif userChoice == 2 and computerChoice == 0:
        print("You Lose!")
    elif computerChoice < userChoice:
        print("You win!")
    else:
        print("fail")
