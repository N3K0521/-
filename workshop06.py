from sys import float_info
from math import pi
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
def swap(lst, a, b):
    lst[a], lst[b] = lst[b], lst[a]
        

def find_min(lst, index):
    res = index
    for i in range(index, len(lst)):
        if lst[i] < lst[res]:
            res = i
    return res
        

# selection sort
def selection_sort(lst):
    res = []
    for i in range(len(lst)):
                   minimum = find_min(lst, i)
                   res = swap(lst, i, minimum)

# Task 2
def swap_down(lst, j):
    if lst[j] < lst[j-1]:
        lst[j], lst[j-1] = lst[j-1], lst[j]

def shuffle_down(lst, k):
    while k > 0:
        if lst[k] < lst[k-1]:
            swap_down(lst, k)
            k -= 1
        else:
            break

def insertion_sort(lst):
    for i in range(1, len(lst)):
                   shuffle_down(lst, i)

# Task 3
def get_friends(graph, v):
    friends = []
    for f in range(len(graph)):
        if graph[v][f]:
            friends += [f]
    return friends

def degree(graph, v):
    friends = 0
    for i in range(len(graph[v])):
        if graph[v][i] == 1:
            friends += 1
    return friends
            

def shared_friends(graph, u, v):
    friends_u = get_friends(graph, u)
    friends_v = get_friends(graph, v)
    shared = []
    for f in friends_u:
        if f in friends_v: shared += [f]
    return shared
    
def are_friends(graph, u, v):
    if graph[u][v] == 1:
        return True
    else:
        return False

def clique(graph, vertices):
    for u in vertices:
        for v in vertices:
            if u != v:
                if not are_friends(graph, u, v):
                    return False
    return True

# Task 4 Extension: (NOT ASSESSED)
from sys import float_info
from math import pi

def sign(x):
    return -1.0 if x < 0 else 1.0

def root(f, a, b, acc=float_info.min):
    """
    Input : continuous function f, floats a, b, and acc
            such that the signs of f(a) and f(b) differ
    Output: float x such that abs(f(x))<=acc

    For example:
    >>> from math import log, isclose
    >>> isclose(root(log, 0.1, 2), 1.0)
    True
    >>> def p(x): return 1-x**2
    >>> isclose(root(p, -2, 0), -1.0)
    True
    >>> isclose(root(p, 0, 100), 1.0)
    True
    >>> from math import sin, pi, isclose
    >>> isclose(root(sin, 1, 4), pi)
    True
    """
    


if __name__=="__main__":
    import doctest
    doctest.testmod()
