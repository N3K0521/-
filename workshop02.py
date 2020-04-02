'''
DO NOT CHANGE THE NAME OF THIS FILE, or else the tester will not work.
The first function requires that you replace the given strings with
your personal details. It is important that you enter your student number
and your student email correctly. If your number and email do not match we
will then check your name, so your name acts as a failsafe.
'''

# Student details
def details():
    student_number = '31552544' #write your student number as a string
    student_email = 'hwan0158' + '@student.monash.edu' #write your student email
    name = 'Huixin Wang' #write your name as it appears on Moodle
    return str(student_number), student_email, name


# Task 1
def calculate(x, y, operator):
    def add(x, y):
        return x + y
    def minus(x, y):
        return x - y
    def multiply(x, y):
        return x * y
    def divide(x, y):
        return x / y
    if operator == '+':
        return add(x, y)
    elif operator == '-':
        return minus(x, y)
    elif operator == 'x':
        return multiply(x, y)
    elif operator == '/':
        return divide(x, y)

# Task 2
def is_leap_year(year):
    if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
        return True
    else: 
        return False

def leap_year_answer(year):
    if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
        if (year >= 2020):
            return ('Year ' + str(year) + ' will be a leap year')
        else:
            return ('Year ' + str(year) + ' was a leap year')
    else:
        if (year >= 2020):
            return ('Year ' + str(year) + ' will not be a leap year')
        else:
            return ('Year ' + str(year) + ' was not a leap year')

# Task 3
def next_triangular_number(num):
    i = 1
    output = 0
    while i <= num:
        output = num * (i + 1) / 2 + 1
        i = output + 1
    return output

# Task 4
def add(numbers):
    output = 0
    for i in range(1, len(numbers), 2):
        output += numbers[i]
    return output


def flip(binary_string):
    output = ''
    for i in range(0, len(binary_string)):
        if binary_string[i] == '0':
            output += '1'
        else:
            output += '0'
    return output

# Challenge
import math
e = math.e
def estimate_e(error):
    x = 1
    i = 1 
    fact = 1
    while abs(x - e) >= error:
        fact = fact * i
        x = x + (1 / fact)
        i += 1
    return x

print(estimate_e(0.1))