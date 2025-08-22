# ASSIGNMENT 2

#Task 1: Returning strings from upper to lowecases
s = input("Enter a string: ")
print(s.lower())

#Task 2 : Changing case from Uppercase to Lowercase and vice versa
s = input("Enter a string: ")
print(s.swapcase())

# Task 3 : Remove all uppercase and return the modified string
s = input("Enter a string: ")
result = ''.join([char for char in s if not char.isupper()])
print(result)

#Task 4 : Returning the number of Uppercase and Lowercase in that string
s = input("Enter a string: ")
upper = sum(1 for char in s if char.isupper())
lower = sum(1 for char in s if char.islower())
print(f"Uppercase: {upper}, Lowercase: {lower}")

#Task 5: Remove all charaters from a string that are not in English letters
import string

s = input("Enter a string: ")
result = ''.join([char for char in s if char.isalpha()])
print(result)

#Task 6: Using Heron's Formula
import math

a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
s = (a + b + c) / 2
area = math.sqrt(s * (s - a) * (s - b) * (s - c))
print(f"Area of triangle: {area}")

#Task 7: List of names
names = ["Gabriel", "Ama", "Kwame", "Akosua"]
print("Name".center(20, "-"))
for name in names:
    print(name.ljust(20))

#Task 8: Clean a string
import string

s = input("Enter a messy string: ")
s = s.strip()
s = ''.join([char for char in s if char not in string.punctuation])
s = s.replace(" ", "")
print(s)
