#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
totalPayment = float(input("What is the total Payment? "))
numberOfPeople = int(input("What is the toatal number of people? "))
paymentPerEach = totalPayment / numberOfPeople
tip = float(input("Give the tip in percent? ")) / 100
netTip = 1 + tip
eachPayment = '{:.2f}'.format(round((paymentPerEach * netTip), 2))
print(
    f"The total payment including tht tip per each individual is {eachPayment}"
)
