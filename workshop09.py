'''
DO NOT CHANGE THE NAME OF THIS FILE, or else the tester will not work. 
The first function requires that you replace the given strings with
your personal details. It is important that you enter your student number
and your student email correctly. If your number and email do not match we
will then check your name, so your name acts as a failsafe.
'''
def convert_temp(temp):
    return (temp-32)/1.8
list(map(convert_temp, [90.0, 50.9, 84.6, 100.3]))

def square(x):
    return x**2
def is_odd(i):
    return i % 2 == 1
list(map(square, list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7]))))

list(map(int, filter(str.isdigit, 'c4t, d0g, b14d, fI5h')))

# Task 1
def convert_temp(temps):
    """
    Input: Given a list of temperatures in fahrenheit.
    Output: A list of values converted all to celsius.

    >>> convert_temp([90.0, 50.9, 84.6, 100.3])
    [32.22222222222222, 10.499999999999998, 29.222222222222218, 37.94444444444444]
    """
    return [((temp-32)/1.8) for temp in temps]

def square_odds(lst):
    """
    Input: A sequence of numbers.
    Output: A list with all of the odd numbers squared.

    >>> square_odds([1, 2, 3, 4, 5, 6, 7])
    [1, 9, 25, 49]
    """
    return [n**2 for n in lst if n % 2 != 0]


def only_numbers(in_str):
    """
    Input: A string that has letters and numbers.
    Output: A list numbers with all the letters removed
            and numbers converted to integers.

    >>> only_numbers('abcdef12345')
    [1, 2, 3, 4, 5]
    >>> only_numbers('c4t,d0g,b14d,fI5h')
    [4, 0, 1, 4, 5]
    """
    return [int(c) for c in in_str if c.isdigit()]


def fizz_buzz(num): # Not Assessed (Optional)
    """
    Input: An integer (num) that represents the total number in list.
    Output: A list that from 0 to num (inclusive) that 
            if the current number is divisible by 3, the element 
            should say "FIZZ", if divisible by 5, the number should 
            say BUZZ, if divisible by both 3 and 5 should say FIZZBUZZ, 
            if neither the element append the number.
    
    >>> fizz_buzz(5)
    [0, 1, 2, 'FIZZ', 4, 'BUZZ']
    >>> fizz_buzz(15)
    [0, 1, 2, 'FIZZ', 4, 'BUZZ', 'FIZZ', 7, 8, 'FIZZ', 'BUZZ', 11, 'FIZZ', 13, 14, 'FIZZBUZZ']
    """
    numbers = range(0, num+1)
    # Boolean values are implicitly cast to integers when you multiply
    return [num and ('FIZZ'*(not(num%3)) + "BUZZ"*(not(num%5))) or num for num in numbers]

# Task 2 - Warmup
def common_bf(a, b):
    res = []
    for x in a:
        for y in b:
            if x ==y:
                res += [x]
    return res

def common(a, b):
    """ Computes list of elements common to a and b.

    Input : two lists, a and b, each without duplicate
            elements
    Output: list of all elements x such that
            x in a and x in b

    For example:
    >>> common([5, 46, -25, 3], [2, -1, 10])
    []
    >>> c = common([8, 5, 27, -2, 10], [-3, 5, -27, 10])
    >>> set(c) == {5, 10}
    True
    """
    a, b = sorted(a), sorted(b)
    n1, n2 = len(a), len(b)
    res = []
    i, j = 0, 0
    while i < n1 and j < n2:
        if a[i] < b[j]:
            i += 1
        elif a[i] > b[j]:
            j += 1
        else:
            res += [a[i]]
            i += 1
            j += 1
    return res

# Task 3
def pairs_of_sum(lst, s):
    """ Finds pairs of list elements with specific sum.

    Input : list of unique integers (lst),
            integer (s)
    Output: list containing all pairs (x, y) of elements 
            of lst such that x < y and x + y = s

    For example:
    >>> pairs_of_sum([7, 1, 25, 10], 5)
    []
    >>> pairs_of_sum([7, 1, 25, 10], 32)
    [(7, 25)]
    >>> pairs = pairs_of_sum([-2, 4, 0, 11, 7, 13], 11)
    >>> set(pairs) == {(0, 11), (4, 7), (-2, 13)}
    True
    """
    small = [s/2 - x for x in lst if x <= s/2]
    large = [x - s/2 for x in lst if x > s/2]
    return [(int(s/2-c), int(s/2+c)) for c in common(small, large)]

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
