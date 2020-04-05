# Task 1: Maths
# Replace the '' in each line with one of [+, -, *, //, %, /, **]
# to create a statement that evaluates to True. 
# For example, (a) can be changed to:
0 == (x + x) % x

# We start by assigning values to variables x and y
x = 3
y = 5

# a
0 == (x - x) * x 
# b
4 == x ** (y - x) - y 
# c
7.5 == (x * y) / (y - x)

# Task 2: Booleans
# Replace the '' in each line with one of [==, !=, <=, >=, <, >]
# to create a statement that evaluates to True.
# For example, (a) can be changed to:
10 <= 10

#a
10 == 10
#b
10%4 > 12//7
#c
3**2 != 10-3

# Task 3: Temperature Conversion
# Replace the '' with a numerical expression that converts the
# temperature in Fahrenheit (temp_f) to the temperature in Celsius.
# For instance, if Celsius were 3 degrees more than Fahrenheit (incorrect!),
# the implementation would be:
# temp_c = temp_f + 3

temp_c = (temp_f-32)*5/9

# Task 4: Name Factoids
# Replace the '' with an expression that evaluates to a string with
# the following pattern:
# factoids = '<name> has <number of letters>. It starts with <letter> and ends with <letter>.'
# For example, if you do not change the given name, factoids would
# evaluate to:
#     'Jane has 4 letters. It starts with J and ends with e.'
# NOTE: You must implement factoids so that it would work for any value
#       assigned to name.

name = 'Jane'
factoids = print(name+' has '+str(len(name))+' letters. It starts with '+name[0]+' and ends with '+name[-1]+'.')


# Task 5: Coin Flip
# THIS TASK IS ONLY FOR FIT1053 STUDENTS

# Replace the '' with any necessary import statements
import random
def flip(numberofflipping):
    countHead=0
    countTail=0
    for x in range(numberofflipping):
        result=random.randint(0,1)
        if result==0:
            countHead+=1
        else:
            countTail+=1
    print('The probability of getting Head is',100*(countHead/numberofflipping),'%')
    print('The probability of getting Tail is',100*(countTail/numberofflipping),'%')

# another solution:
from random import random
def flip(bias):
    return 'The flipped coin with bias {} has a value of heads: {}' \
        .format(bias, bias > random())