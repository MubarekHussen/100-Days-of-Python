# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1L = name1.lower()
name2L = name2.lower()

l = name1L.count("l") + name2L.count("l")
o = name1L.count("o") + name2L.count("o")
v = name1L.count("v") + name2L.count("v")
e = name1L.count("e") + name2L.count("e")
t = name1L.count("t") + name2L.count("t")
r = name1L.count("r") + name2L.count("r")
u = name1L.count("u") + name2L.count("u")
e = name1L.count("e") + name2L.count("e")

countTrue = t + r + u + e
countLove = l + o + v + e
score = int(str(countTrue) + str(countLove))

if (score < 10 or score > 90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif (score > 40 and score < 50):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
