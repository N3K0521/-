# Tutorial 3

'''
Prepared Question:
Alcohol is a drug that is processed by the body in a relatively predictable way. Because alcohol can
impair an individual's driving, in Australia you are not legally allowed to drive unless your blood
alcohol level (BAL) is below 0.05%. It takes approximately one hour for your BAL to decrease by 0.015.

1. 
Implement in Python a function, hours_to_legal_limit(bal), that takes an individual's current BAL and returns an integer
representing the number of hours that individual must wait before they can legally drive, rounded to the larger number (we
want to be on the safe side!). You must use either a for-loop or a while-loop inside your function. The function can be 
handwritten.

2. 
Explain why you chose to use one kind of loop instead of the other kind. The explanation can be short, but it must be 
meaningful.
'''

def hours_to_legal_limit(bal):
    number_of_hours = 0
    while bal >= 0.15:
        number_of_hours += 1
        bal = bal - 0.015
    print(number_of_hours)

'''
I used a while loop because this case was conditional, which might be run ultimately until the condition was achieved. 
For loops are more suitable in the case when implement time is known.
''' 

# List of lists

'''
What you would find is that every element of the outer_list refers to the same inner_list. When you follow the links you
would see we are overwriting the same list contents again and again, changing inner_list from [0,0,0,0] to [0,1,2,3] to
[4,5,6,7] to [8,9,10,11] to [12,13,14,15]. For make_my_list to do as the programmer likely intended, you will need N many
distinct inner lists.
'''

# Multiplication Table

def multiplication_table(x):
    table = []
    for num1 in range(1, x+1):
        line = []
        for num2 in range(1, x+1):
            line += num1 * num2
        table.append(line)
    return table
#There are many ways to implement the extension option, but a simple way using the tools you currently know is shown below.
#This could be made more concise by using decomposition.
def maths_table(x, operator):
    table = []
    for num1 in range(1, x+1):
        if operator == '*':
            line += num1 * num2
        elif operator == '/':
            line += num1 / num2
        elif operator == '+':
            line += num1 + num2
        elif operator == '-':
            line += num1 - num2
    table.append(line)
    return maths_table

# Loop Challenges

# 1
def padded():
    my_list = []
    for num in range(1, 101):
        number = str(num)
        while len(number) < 3:
            number = '0' + number
        my_list += number
    return my_list

# 2
def binary(number):
    count = 0
    for num in number:
        count += int(num) #could also use a conditional expression
    return count

# 3
def even(my_list):
    seen = []
    for i in range(len(my_list)):
        if my_list[i] not in seen:
            seen += my_list[i]
            count = 0
            for j in range(i, len(my_list)):
                count += (1 if my_list[i] == my_list[j] else 0)
            if count%2 != 0:
                return False
    return True

'''
Checkpoint
1. What is the definition of a computational problem?
2. What range best reflects the sequence 10, 7, 4, 1, -2? (There are multiple correct answers.)
3. Write a Python function, double, that takes a list of integers as arguments, and returns the
same list with all values doubled.
4. Write a Python function, table, that takes an integer x as an argument, and returns an n by n table,
where table[i][j] == i+j. For example, table(3) would return [[0,1,2],[1,2,3],[2,3,4]].
'''

#Solutions:
# 1.
# A computational problem is a typically infinite collection of questions(callled inputs or instances),
# each of which has at least one correct associated answer(called output)." 

# 2.
# range(10, -3, 3), or range(10, -4, -3), or range(10, -5, -3).

# 3.
def double(my_list):
    # cannot use 'for i in my_list'
    for i in range(len(my_list)):
        my_list[i] *= 2
    return my_list

# 4.
def table(n):
    t = []
    for i in range(n):
        row = []
        for j in range(n):
            row += [i+j]
        t.append(row)
    return t