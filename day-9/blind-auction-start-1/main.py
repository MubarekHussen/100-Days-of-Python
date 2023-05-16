from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)
print("Welcome to the secret auction program")
isThere = ""
dic = {}


def auction():# print(dic)
    name = input("What is your name?: ")
    bid = input("What's your bid?: $")
    global dic
    dic[name] = bid
    global isThere
    isThere = input(
        "Are there any other bidders? Type 'yes' or 'no'. \n").lower()


auction()
while (isThere != "no" and isThere == "yes"):
    clear()
    auction()

max = 0
key = ""
for i in dic:
    if (max < int(dic[i])):
        max = int(dic[i])
        key = i
clear()
print(f"The winner is {key} with a bid of ${max}")
