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
# Another solution:
def leap_year_answer(year):
    if year < 2021:
        if is_leap_year(year):
            return 'Year {} was a leap year'.format(year)
        else:
            return 'Year {} was not a leap year'.format(year)
    else:
        if is_leap_year(year):
            return 'Year {} will be a leap year'.format(year)
        else:
            return 'Year {} will not be a leap year'.format(year)

# Task 3
def next_triangular_number(num):
    i = 1
    output = 0
    while i <= num:
        output = num * (i + 1) / 2 + 1
        i = output + 1
    return output

# Another solution:
def next_triangular_number(num):
    n = 0
    trig_num = 0
    while trig_num < num:
        n += 1
        trig_num += n
    return trig_num

# Task 4
def add(numbers):
    total = 0
    i = 1
    while i < len(numbers):
        total += numbers[i]
        i += 2
    return total

def flip(binary_string):
    output = ''
    for i in range(0, len(binary_string)):
        if binary_string[i] == '0':
            output += '1'
        else:
            output += '0'
    return output

# Another solution:
def flip(binary_string):
    flipped = ''
    i = 0
    while i < len(binary_string):
        if binary_string[i] == '0':
            flipped += '1'
        else:
            flipped += '0'
        i += 1
    return flipped
    
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

# Challenge
# Implement a function, primes(n), that returns a list of all primes less than n.
def primes(n):
    '''
    Input: a positive integer
    Output: a list of positive integers, containing all primes from 1 to n
    '''
    potential = list(range(2,n))
    primes = []
    i = 0
    while i < len(potential):
        num = potential[i]
        if num: #if the number at i is not composite
            primes += [num] #number is prime
            j = i + num
            while j < len(potential):
                potential[j] = None
                j += num
        i += 1
    return primes

'''
Analysis:
The problem asks for a function that finds all prime numbers that are smaller than n.
The most difficult part of solving this problem was implementing a solution that was efficient.
While I could have gone through every number less than n and checked whether it had more than 
two factors, this would be inefficient.

    In my solution I chose to use the algorithm the Sieve of Eratosthenes because this is a simple
algorithm to find all primes up to a given number. My function creates a list of all my numbers
from 2 to n-1, and then iterates through the list eliminating all multiples of number that have
already appeared in the list, and adding all non_eliminated numbers to a list of primes.

    I use two while loops as part of my function. The first while loop ensures that all numbers from
2 to n-1 get checked. The second while loop sets all multiples of a particular number to None, because
if a number is a multiple of another number, then it is not a prime. I could have used for-loops instead
of while-loops. I chose to use while loops because I found the inner loop was easier to understand as a
while-loop.

    I have done my best to remove all inefficiencies in my implementation. My function makes a list of all
numbers from 2 to n-1 (1 is not included because it is neither composite nor prime). All these numbers need
to be checked, so this is not an inefficiency. In my inner-loop, I only remove all multiples of a number if
that number is prime. This means, for example, multiples of 4,6,8, etc. do not have to be removed: they are
already removed because they are multiples of 2. This reduces the amount of redundant checks.
'''