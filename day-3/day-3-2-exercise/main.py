# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

# - Under 18.5 they are underweight
# - Over 18.5 but below 25 they have a normal weight
# - Over 25 but below 30 they are slightly overweight
# - Over 30 but below 35 they are obese
# - Above 35 they are clinically obese.

#Write your code below this line 👇
bmi = weight / (height ** 2)
dispBmi = '{:.2f}'.format(bmi)
if (bmi < 18.5):
  print(f"Your BMI is {dispBmi}, You are under-weight")
elif (bmi > 18.5 and bmi < 25):
  print(f"Your BMI is {dispBmi}, You are normal, congrats!!")
elif (bmi > 25 and bmi < 30):
  print(f"Your BMI is {dispBmi}, You are slightly over-weight")
elif (bmi > 30 and bmi < 35):
  print(f"Your BMI is {dispBmi}, You are obese")
else:
  print(f"Your BMI is {dispBmi}, You are clinically obese")


