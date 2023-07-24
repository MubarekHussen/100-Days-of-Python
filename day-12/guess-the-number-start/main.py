#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
from art import logo
import random

print(logo)
numbers = []
stope = False
for i in range(1, 101):
    numbers.append(i)
# print(numbers)
value = random.choice(numbers)


def low(guess):
    global value
    if (guess < value):
        print("Too low")


def high(guess):
    global value
    if (guess > value):
        print("Too high")


level = input("Type 'h' for hard, type 'e' for easy: ")
if (level == 'h'):
    attempets = 5
    # global value
    for i in range(0, 5):
        print(f"You have {attempets} left make a guess")
        guess = int(input("Make a guess: "))
        low(guess)
        high(guess)
        if (value == guess):
            print(f"You got it the answer was: {value}")
            stope = True
            break
        attempets -= 1
    if (stope):
        print("Guess again!")
    else:
        print("You have run out of guess, You lose")
elif (level == "e"):
    attempet = 10
    # global value
    for i in range(0, 10):
        print(f"You have {attempet} left make a guess")
        guess = int(input("Make a guess: "))
        low(guess)
        high(guess)
        if (value == guess):
            print(f"You got it the answer was: {value}")
            stope = True
            break
        attempet -= 1
    if (stope):
        print("Guess again!")
    else:
        print("You have run out of guess, You lose")
