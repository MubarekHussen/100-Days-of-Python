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

#Write your code below this line 👇
import random

inpt = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."
          ))
if (inpt >= 3):
  print("Invalid character" or "yahebabi")
choice = ["Rock", "Paper", "Scissors"]
rand = random.randint(0, 2)
comp = choice[rand]
person = choice[inpt]
if (person == "Scissors"):
    print(scissors)
elif (person == "Rock"):
    print(rock)
elif (person == "Paper"):
    print(paper)

print("Computer Chose:")
if (comp == "Scissors"):
    print(scissors)
elif (comp == "Rock"):
    print(rock)
elif (comp == "Paper"):
    print(paper)
if (comp == "Rock" and person == "Scissors"):
    print("You lose")
elif (comp == "Scissors" and person == "Paper"):
    print("You lose")
elif (comp == "Paper" and person == "Rock"):
  print("You lose")
else:
  print("You Win")