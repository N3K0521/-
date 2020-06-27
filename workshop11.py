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


# Warmup
def lex_less_eq(a, b):
    """Determines whether sequence (a) is lexicographically less or equal to
    sequence (b); equivalent to a <= b.

    For example:
    >>> lex_less_eq('tactic', 'tree')
    True
    >>> lex_less_eq('tactic', 'tactical display')
    True
    >>> lex_less_eq([1, 2, 3], [0, 1, 2, 3])
    False
    """
    for i in range(min(len(a), len(b))):
        if a[i] != b[i]:
            return a[i] < b[i]
    return len(a) <= len(b)

# Task 1: Part A - Recursive Bitlist
def rbitlists(n):
    """Generates list of all bitlists of length n in lexicographic order
    using recursion.

    For example.
    >>> rbitlists(2)
    [[0, 0], [0, 1], [1, 0], [1, 1]]
    >>> rbitlists(3)
    [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]

    <Write your explanation here>
    The implementation lists bitlists recursively from the base case n==0 where
    the solution only consits of the empty bitlist.
    Recursively, the function first generates all length n bitlists resulting
    from pretending 0 to all bitlists of length n-1 and then all length n
    bitlists resulting from prepending 1 to all bitlists of length n-1.
    The approach is correct because all teh bitlists resulting from prepending
    0 are lexicographically smaller than those resulting from prepending 1 (and
    internally the length n-1 bitlists are ordered lexicorgraphically by
    correctness of the recursive call)
    """
    if n ==0:
        return [[]]

    lists = rbitlists(n-1)

    return [[0] + lst for lst in lists] + \
           [[1] + lst for lst in lists]

# Task 1: Part B - Recursive Permutations
def rpermutations(lst):
    """ Generates all permutations of input list.
    
    >>> sorted(rpermutations(list(range(1, 4))))
    [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    >>> sorted(rpermutations(list(range(1, 5))))
    [[1, 2, 3, 4], [1, 2, 4, 3], [1, 3, 2, 4], [1, 3, 4, 2], [1, 4, 2, 3], [1, 4, 3, 2], [2, 1, 3, 4], [2, 1, 4, 3], [2, 3, 1, 4], [2, 3, 4, 1], [2, 4, 1, 3], [2, 4, 3, 1], [3, 1, 2, 4], [3, 1, 4, 2], [3, 2, 1, 4], [3, 2, 4, 1], [3, 4, 1, 2], [3, 4, 2, 1], [4, 1, 2, 3], [4, 1, 3, 2], [4, 2, 1, 3], [4, 2, 3, 1], [4, 3, 1, 2], [4, 3, 2, 1]]
    >>> sorted(rpermutations(list('JOE')))
    [['E', 'J', 'O'], ['E', 'O', 'J'], ['J', 'E', 'O'], ['J', 'O', 'E'], ['O', 'E', 'J'], ['O', 'J', 'E']]

    <Write your explanation here>
    For the base case of an empty input list the only permutation is the empty
    list itself. For non-empty lst, assuming that we can enumerate all
    permutations of the sublist lst[:-1] (all excep last element), we can then
    recursively generate a list of all permutations by inserting the last element
    in all possible positions for each permutation of the smaller list.
    """
    if len(lst)==0:
        return [[]]

    perms = rpermutations(lst[:-1])
    res = []
    for perm in perms:
        res += [perm[:i]+[lst[-1]]+perm[i:] for i in range(len(perm), -1, -1)]
    return res

# Task 2: Part B1 - Bounded Lists
def lex_suc(bitlists, upper_bounds):
    """
    Input: bitlist a!=[1, ..., 1]
    Output: direct lex.successor of a
    """
    res = bitlists[:]
    i = len(res) - 1
    while res[i] == upper_bounds[i]:
        res[i] = 0
        i -= 1
    res[i] += 1
    return res

def bounded_lists(upper_bounds):
    """
    Input: List of positive integers of length 'n'
    Output: List of lists where i, lst[i] <= upper_bound[i]

    >>> bounded_lists([1, 1, 2])
    [[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [0, 1, 1], [0, 1, 2], [1, 0, 0], [1, 0, 1], [1, 0, 2], [1, 1, 0], [1, 1, 1], [1, 1, 2]]
    """
    first = len(upper_bounds)*[0]
    last = upper_bounds
    res = [first]
    while res[-1] != last:
        res += [lex_suc(res[-1], upper_bounds)]
    return res


# Task 2: Part 1 - Greedy Exchange
def greedy_exchange(amount, denominations):
    """
    >>> greedy_exchange(56, [20, 10, 5, 1])
    [2, 1, 1, 1]
    >>> greedy_exchange(350, [100, 50, 10, 5, 2, 1])
    [3, 1, 0, 0, 0, 0]
    >>> greedy_exchange(12, [9, 6, 5, 1])
    [1, 0, 0, 3]
    """
    res = []
    s = 0
    for i in range(len(denominations)):
        c = (amount - s) // denominations[i]
        s += c*denominations[i]
        res += [c]
    return res if s==amount else None

    
# Task 2: Part B2 - Brute Force Implementation
def brute_force_coin_exchange(amount, denominations):
    """
    Input: The target amount of you want to reach and a list of 
           coins (i.e. denominations) that you have an infinite amount of.
    Output: A list of integers where each index represents the number of 
            coins the denominations list.

    >>> brute_force_coin_exchange(15, [10, 7, 6, 1])
    [0, 2, 0, 1]
    """
    def cost(solution):
        return sum(solution)

    def is_feasible(solution):
        total = 0
        for i in range(len(solution)):
            total += solution[i]*denominations[i]
        return total == amount

    upper_bounds = []
    for denom in denominations:
        upper_bounds += [amount // denom]

    sols = bounded_lists(upper_bounds)
    feasible = filter(is_feasible, sols)
    opt = min(feasible, key=cost)
    return opt


# Task 2: Part C - Backtracking Implementation

def solutions(completed, options, part = []):
    if completed(part):
        return [part]
    else:
        res = []
        for o in options(part):
            augmented = part + [o]
            res += solutions(completed, options, augmented)
        return res
    
def backtracking_exchange(amount, denominations):
    """
    >>> backtracking_exchange(56, [20, 10, 5, 1])
    [2, 1, 1, 1]
    >>> backtracking_exchange(12, [9, 6, 5, 1])
    [0, 2, 0, 0]
    """
    n = len(denominations)

    def total(part):
        return sum(part[i]*denominations[i] for i in range(len(part)))

    def complete(part):
        return len(part) == n and amount - total(part) == 0

    def options(part):
        if len(part) == n:
            return []
        else:
            remaining = amount - total(part)
            max_coins = remaining // denominations[len(part)]
            return reversed(range(max_coins + 1))

    sols = solutions(complete, options)

    return min(sols, key=sum, default=None)


if __name__=='__main__':
    import doctest
    doctest.testmod()
