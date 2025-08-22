# TASK 1:Creating variables
my_integer = 10
my_float = 3.14
my_string = "Hello, Python!"
my_boolean = True

# Printing each variable with its type
print(my_integer, type(my_integer))
print(my_float, type(my_float))
print(my_string, type(my_string))
print(my_boolean, type(my_boolean))

# TASK 2:Conversions
float_to_int = int(19.99)
int_to_str = str(50)
str_to_float = float("50")

# Printing results and types
print(float_to_int, type(float_to_int))
print(int_to_str, type(int_to_str))
print(str_to_float, type(str_to_float))

# TASK 3:User input
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# Greeting
print(f"Hello, {first_name} {last_name}!")

# Task 4: Taking user's name
age = 20
# a.Fix: Convert age to string before concatenation
print("You are " + str(age) + " years old.")

# b.Explanation:
# The error occurs because you can't concatenate a string with an integer directly.

# User input
word = input("Enter your favourite word: ")
repeat_count = int(input("How many times should it be repeated? "))

# :Output
print((word + " ") * repeat_count)

# Task:6
#print("Hello	SyntaxError
#int("abc")	ValueError
#"age" + 10	TypeError
