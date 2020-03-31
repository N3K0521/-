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
    if operator == '+':
        print('{} + {} = '.format(x, y))
        print(x + y)
    elif operator == '-':
        print('{} - {} = '.format(x, y))
        print(x - y)
    elif operator == '*':
        print('{} * {} = '.format(x, y))
        print(x * y)
    elif operator == '/':
        print('{} / {} = '.format(x, y))
        print(x / y)

# Task 2
def is_leap_year(year):
    if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
        return True
    else: 
        return False

def leap_year_answer(year):
    if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
        if (year >= 2020):
            print ('Year ' + str(year) + 'will be a leap year.')
        else:
            print ('Year ' + str(year) + 'was a leap year.')
    else:
        if (year >= 2020):
            print ('Year ' + str(year) + 'will not be a leap year.')
        else:
            print ('Year ' + str(year) + 'was not a leap year.')

# Task 3
def next_triangular_number(num):
    pass


# Task 4
def add(numbers):
    pass


def flip(binary_string):
    pass


# Challenge
def estimate_e(error):
    pass