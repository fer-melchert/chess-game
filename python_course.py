# Python Full Course for Beginners by Programming with Mosh
# Link: https://www.youtube.com/watch?v=_uQrJ0TkZlc
#
# This file contains code written as part of following the tutorial.
# The purpose is to document my learning and understanding of Python concepts.
#
# Notes:
# - Code may be directly inspired by or adapted from the course material.
# - The `skipped_section` variable is used to prevent earlier code from running while focusing on new concepts.
# - This code is for educational and personal documentation purposes only.
# - Any modifications, experiments, or additional comments are my own contributions.

import math

course = 'Python for beginners'
print(len(course))
print(course.upper())
print(course)
print(course.find('n'))
print(course.replace('beginners', 'absolute beginners'))
print('Python' in course)

x = 10
x = x + 3
x += 3 #augmented assignment operator
print(x)

x = 10
x -=3
print(x)

x = 10 + 3 * 2
print(x) #order of operations = exponentiation, multiplication or division, addition or subtraction
x = 10 + 3 * 2 ** 2
print(x)
x = (10 + 3) * 2 ** 2
print(x)

x = 2.9
print(round(x))
print(abs(-2.9)) #abs = absolute = return the positive value of a number
#module = separate file with some reusable code ex. math module, use import
print(math.ceil(2.9))
print(math.floor(2.9))

# IF STATEMENTS
is_hot = False
is_cold = False
if is_hot:
    print("It's a hot day")
    print("Enjoy your day!")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes!")

else:
    print("It's a lovely day!")
print('Have a good one!')

price = 1000000
good_credit = True
if good_credit:
    down_payment =  0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down payment: ${down_payment}")

# LOGICAL OPERATORS IN PYTHON: and(both), or(at least one), not(inverses boolean value)
has_high_income = False
has_good_credit = False
if has_high_income or has_good_credit:
    print("Eligible for loan")

has_good_credit = True
has_criminal_record = False
if has_good_credit and not has_criminal_record:
    print("Eligible for loan")

#COMPARISSION OPERATORS IN PYTHON: compare variable with value (>, <, ==, =!)
temperature = 35
if temperature > 30: #expression = piece of code that produces a value (in this case boolean expression)
    print("It's a hot day!")
else:
    print("It's not a hot day.")

name = "Fernando"
if len(name) < 3:
    print("username must be at least 3 characters")
elif len(name) > 50:
    print("username must have a maximum of 50 characters")
else:
    print("valid username")

def skipped_section():
    weight = int(input('Weight: '))
    unit = input('(L)bs or (K)g?: ')
    if unit.upper() == "L":
        converted = weight * 0.45
        print(f"Your weight is {converted} kilos")
    else:
        converted = weight / 0.45
        print(f"Your weight is {converted} pounds")
        print('this code is skipped unless called')

#WHILE LOOPS IN PYTHON: execute a block of code multiple times
def skipped_section2():
    i = 1
    while i <= 5:
        print('*' * i)
        i = i + 1
    print("Done")

    secret_number = 9
    guess_count = 0
    guess_limit = 3
    while guess_count < guess_limit:
        guess = int(input('Guess number: '))
        guess_count += 1
        if guess == secret_number:
            print('You won!')
            break
    else:
        print('Sorry, you failed!')

#CAR GAME EXERCISE
def skipped_section3():
    command = ""
    started = False
    while True:
        command = input("> ").lower()
        if command == "start":
            if started:
                print("Car is already started")
            else:
                started = True
                print("Car started...")
        elif command == "stop":
            if not started:
                print("Car is already stopped!")
            else:
                started = False
                print("Car stopped.")
        elif command == "help":
            print("""
start - to start the car
stop - to stop the car
quit - to quit the game
        """)
        elif command == "quit":
            break
        else:
            print("invalid command!")

#FOR LOOPS IN PYTHON
for item in ['Misha', 'John', 'Sarah']:
    print(item)
for item in range(5, 10, 2): #steps in 2 increments
    print(item)

prices = [10, 20, 30]
total = 0
for price in prices:
    total += price #total = total + price
print(f'total: {total}')

#NESTED LOOPS IN PYTHON: adding one loop inside another loop
for x in range(4):
    for y in range(3):
        print(f"({x}, {y})")

numbers = [5, 2, 5, 2, 2]
for x_count in numbers:
    print('x' * x_count)
numbers = [5, 2, 5, 2, 2]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)

#LISTS IN PYTHON
names = ['John', 'Bob', 'Misha', 'Sarah', 'Mary']
print(names)
print(names[2])
print(names[-1])
print(names[2:])

numbers = [3, 6, 2, 8, 10, 4]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)

#2D LISTS IN PYTHON
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
print(matrix[0][1])
matrix[0][1] = 20
print(matrix[0][1])
for row in matrix:
    for item in row:
        print(item)

#LIST METHODS (FUNCTIONS)








