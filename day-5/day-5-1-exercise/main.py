# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
tot = 0
length = 0
for height in student_heights:
    tot += height
    length += 1
    average = round(tot / length)

print(average)
