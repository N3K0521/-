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

###Task 1
def partial_sum(start, end, step):
    output = 0
    if end >= 0:
        end = end + 1
    elif end < 0:
            end = end - 1
    for i in range(start, end, step):
        output = output + i
    return output
    
###Task 2
def reverse_strings(my_list):
    i = 0
    flip = 0
    while i < (len(my_list)/2):
        flip = my_list[i]
        my_list[i] = my_list[(len(my_list))-1-i]
        my_list[(len(my_list))-1-i] = flip
        i = i + 1
    return (''.join(my_list))

def complete(my_list):
    start = my_list[0]
    end = my_list[-1]
    output = []
    for i in range(start, end + 1):
        output.append(i)
    return output    

###Task 3
def addition_table(numbers):
    table = []
    for j in range(3):
        row = []
        for i in range(0, len(numbers)):
            row.append(numbers[i] + j + 1)
        table.append(row)
    return table

###Task 4
def remove_outliers(table):
    maximum = [0][0]
    minimum = [0][0]
    for i in range(len(table)):
        for j in range(len(table[i])):
            if table[i][j] > maximum:
                maximum = table[i][j]
            elif table[i][j] < minimum:
                minimum = table[i][j]
    avg = (maximum + minimum)/2
    for i in range(len(table)):
        for j in range(len(table[i])):
            if table[i][j] == maximum:
                table[i][j] = avg
            elif table[i][j] == minimum:
                table[i][j] = avg
    return table
    