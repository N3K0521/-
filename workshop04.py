'''
DO NOT CHANGE THE NAME OF THIS FILE, or else the tester will not work. 
The first function requires that you replace the given strings with
your personal details. It is important that you enter your student number
and your student email correctly. If your number and email do not match we
will then check your name, so your name acts as a failsafe.
'''

# Student details
def details():
    student_number = '31552533' #write your student number as a string
    student_email = 'hwan0158' + '@student.monash.edu' #write your student email
    name = 'Huixin Wang' #write your name as it appears on Moodle
    return str(student_number), student_email, name

''' Simple Functions '''
# is_in()
def is_in(char, string):
    for i in range(len(string)):
        if char == string[i]:
            return True
    return False

# is_sorted()
def is_sorted(seq):
    for i in range(len(seq)-1):
        if seq[i] > seq[i+1]:
            return False
    return True

# abs()
def abs(x):
    if x >= 0:
        absx = x
    elif x < 0:
        absx = 0 - x
    return absx

# all()
def all(lst):
    for element in lst:
        if not element:
            return False
    return True

# any()
def any(lst):
    for element in lst:
        if element:
            return True
    return False

# max()
def max(lst):
    ma = lst[0]
    for element in lst:
        if element > ma:
            ma = element
    return ma

# min()
def min(lst):
    mi = lst [0]
    for element in lst:
        if element < mi:
            mi = element
    return mi

# reversed()
def reversed(seq):
    res = []
    ri = len(seq) - 1
    for i in range(len(seq)):
        res.append(seq[ri - i])
    return res
'''
def rev_manual_pos_gen(mylist):
    max_index = len(mylist) - 1
    return [ mylist[max_index - index] for index in range(len(mylist)) ]

def rev_manual_neg_gen(mylist):
    ## index is 0 to 9, but we need -1 to -10
    return [ mylist[-index-1] for index in range(len(mylist)) ]

def rev_manual_index_loop(mylist):
    a = []
    reverse_index = len(mylist) - 1
    for index in range(len(mylist)):
        a.append(mylist[reverse_index - index])
    return a

def rev_manual_loop(mylist):
    a = []
    reverse_index = len(mylist)
    for index, _ in enumerate(mylist):
        reverse_index -= 1
        a.append(mylist[reverse_index])
    return a
'''

# sum()
def sum(lst):
    res = 0
    for element in lst:
        res += element
    return res

'''Complex Functions'''
def bin(x):
    return format(x, '#b')

