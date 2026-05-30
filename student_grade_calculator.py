marks1 = float(input("Enter marks of Subject 1: "))
marks2 = float(input("Enter marks of Subject 2: "))
marks3 = float(input("Enter marks of Subject 3: "))

total = marks1 + marks2 + marks3
average = total / 3

if average >= 90:
    grade = "A"

elif average >= 75:
    grade = "B"

elif average >= 60:
    grade = "C"

elif average >= 40:
    grade = "D"

else:
    grade = "F"

print("Total Marks =", total)
print("Average Marks =", average)
print("Grade =", grade)
