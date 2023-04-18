# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

left_age = 90 - int(age)
day = str(left_age * 365)
week = str(left_age * 52)
month = str(left_age * 12)

# print("You have " + day +  " days, " + week + " weeks, and " + month + " months left.")


#By using f string

print(f"You have {day} days, {week} weeks, and {month} months left.")








