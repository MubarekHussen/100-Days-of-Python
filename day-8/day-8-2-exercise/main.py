#Write your code below this line 👇
import math


def prime_checker(number):
    check = math.ceil(int(math.sqrt(number)))
    if (number == 2):
        print("It's a prime number")
    for i in range(2, check):
        if (number % i == 0):
            print("It's not a prime number")
            break
        else:
            print("It's a prime number")
            break


#Write your code above this line 👆

#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
