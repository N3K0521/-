from math import sqrt, pi
from sys import float_info
import random # For task1c
import timeit # For task1c
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


# Task 1A - Merge
def merge(lst1, lst2):
    """
    Input: Two sorted lists lst1, lst2
    Output: One sorted list 'res' merged together
    >>> merge([1, 2, 4, 6], [3, 5, 7, 8])
    [1, 2, 3, 4, 5, 6, 7, 8]

    >>> merge([1, 2, 3], [4, 5, 6])
    [1, 2, 3, 4, 5, 6]

    >>> merge([11, 13, 15], [])
    [11, 13, 15]

    >>> merge([], [16, 18, 20])
    [16, 18, 20]
    """
    res = []
    i = 0
    j = 0
    while i < len(lst1) and j < len(lst2): 
        if lst1[i] < lst2[j]:
            res.append(lst1[i])
            i += 1
        else:
            res.append(lst2[j])
            j += 1
    return res + lst1[i::] + lst2[j::]

# Task 1B - Merge Sort
def merge_sort(lst):
    """
    Input: list of elements
    Output: Sorted list of elements
    >>> merge_sort([3, 7, 9, 6, 2, 5, 4, 1, 8])
    [1, 2, 3, 4, 5, 6, 7, 8, 9]

    >>> merge_sort([11, 0, 1, 5, 7, 2])
    [0, 1, 2, 5, 7, 11]

    >>> merge_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """
    k, n = 1, len(lst)
    while k < n:
        nxt = []
        for a in range(0, n, 2*k):
            b, c = a + k, a + 2 * k
            nxt += merge(lst[a:b], lst[b:c])
        lst = nxt
        k = 2 * k
    return lst

# Selection Sort Code
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

# Insertion Sort Code
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

# Task 1C - Analysis of Sorting Algorithms
if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
    # Constructing lists from 1 to 1000
    sorts_lst = []
    inc_lst = list(range(1, 1000+1))
    dec_lst = list(range(1000+1, 1, -1))
    rand_lst = list(range(1, 1000+1))
    random.shuffle(rand_lst) #shuffle randome list

    # mergesort
    sorts_lst.append(('merge sort', 'increasing list', inc_lst))
    sorts_lst.append(('merge sort', 'decreasing list', dec_lst))
    sorts_lst.append(('merge sort', 'random list', rand_lst))

    # insertionsort
    sorts_lst.append(('insertion sort', 'increasing list', inc_lst))
    sorts_lst.append(('insertion sort', 'decreasing list', dec_lst))
    sorts_lst.append(('insertion sort', 'random list', rand_lst))

    # selectionsort
    sorts_lst.append(('selection sort', 'increasing list', inc_lst))
    sorts_lst.append(('selection sort', 'decreasing list', dec_lst))
    sorts_lst.append(('selection sort', 'random list', rand_lst))    

    for item in sorts_lst:
        # Unpacking the tuples
        name, status, lst = item     #sequence unpacking
        start = timeit.default_timer()  #grabs the wall clock not cpu time,
                                        #the perf_counter() can also be used
                                        #function as this is now what default_timer()
                                        #is from Python3.3
        if name == 'insertion sort':
            insertion_sort(lst)
        elif name == 'selection sort':
            selection_sort(lst)
        elif name == 'merge sort':
            res = merge_sort(lst)
        else:
            print('Error in identifying type of sort...exiting program')
            break
        end = timeit.default_timer()
        print('The time taken in {} for a/an {} is: {}'.format(name, status, end-start))



# Task 2 - Post Offices
def dist(p1, p2):
    """Computes Euclidean distance between points p1 and p2.
    """
    dist = ((p1-p2)**2+(p1-p2)**2)**(1/2)
    return dist


def offices_to_merge(points):
    """
    Input : list of 2d coordinates of post offices,
            points=[(x1, y1), (x2, y2)...(xn, yn)]} with n>1
    Output: a pair of indices (l, k) such that...
            for all pairs of indices 0 <= i < j <=n it holds that
            dist(points[l], points[k]) <= dist(points[i], points[j])
    
    For example:
    >>> points = [(350, 150), (500, 250), (150, 150), (50, 400), (200,100)]
    >>> offices_to_merge(points)
    (2, 4)
    """
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            dist = ((points[j][0]-points[i][0])**2+(points[j][0]-points[i][1])**2)**(1/2)

    '''
    n = len(points)
    l, k = 0, 1
    for i in range(n):
        for j in range(i+1, n):
            if dist(points[i], points[j]) < dist(points[1], points[k]):
                l, k = i, j
            #INV: for all a, b with 0 <= a <= i+1 < b j <= j+1,
            #     dist(points[1], points[k]) <= dist(points[a], points[b])
    return l, k
    '''
            


# Task 3 - Regula Falsi

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
    left_sign = sign(f(a))
    while True:
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
        y = f(c)
        if abs(y) <= acc or c==a or c==b:
            return c
        elif sign(y) == left_sign:
            a = c
        else:
            b = c
    return None

if __name__=="__main__":
    import doctest
    doctest.testmod()

# Task 1C - Analysis of Sorting Algorithms
if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
    # Constructing lists from 1 to 1000
    sorts_lst = []
    inc_lst = list(range(1, 1000+1))
    dec_lst = list(range(1000+1, 1, -1))
    rand_lst = list(range(1, 1000+1))
    random.shuffle(rand_lst) #shuffle randome list

    # mergesort
    sorts_lst.append(('merge sort', 'increasing list', inc_lst))
    sorts_lst.append(('merge sort', 'decreasing list', dec_lst))
    sorts_lst.append(('merge sort', 'random list', rand_lst))

    # insertionsort
    sorts_lst.append(('insertion sort', 'increasing list', inc_lst))
    sorts_lst.append(('insertion sort', 'decreasing list', dec_lst))
    sorts_lst.append(('insertion sort', 'random list', rand_lst))

    # selectionsort
    sorts_lst.append(('selection sort', 'increasing list', inc_lst))
    sorts_lst.append(('selection sort', 'decreasing list', dec_lst))
    sorts_lst.append(('selection sort', 'random list', rand_lst))    

    for item in sorts_lst:
        # Unpacking the tuples
        name, status, lst = item     #sequence unpacking
        start = timeit.default_timer()  #grabs the wall clock not cpu time,
                                        #the perf_counter() can also be used
                                        #function as this is now what default_timer()
                                        #is from Python3.3
        if name == 'insertion sort':
            insertion_sort(lst)
        elif name == 'selection sort':
            selection_sort(lst)
        elif name == 'merge sort':
            res = merge_sort(lst)
        else:
            print('Error in identifying type of sort...exiting program')
            break
        end = timeit.default_timer()
        print('The time taken in {} for a/an {} is: {}'.format(name, status, end-start))
