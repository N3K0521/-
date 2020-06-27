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

"""
Backtracking
def solutions(completed, options, partial = []):
    if completed(partial):
        return [partial]
    else:
        res = []
        for o in options(partial):
            augmented = partial + [o]
            res += solutions(completed, options, augmented)
            return res
        
def backtracking_task(x):
    def options(partial):
        ...
    def completed(partial):
        ...
    return solutions(completed, options, starting_partial)
"""

# Part A - Palindromic Bitlists (0.5 Marks)
def palindrome_binary(n):
    """
    Input: integer n
    Output: list of bitlists in lexicographical order where each bitlist is
            a palindrome.
    
    For Example:
    >>> palindrome_binary(2)
    [[0, 0], [1, 1]]
    >>> palindrome_binary(3)
    [[0, 0, 0], [0, 1, 0], [1, 0, 1], [1, 1, 1]]
    >>> palindrome_binary(4)
    [[0, 0, 0, 0], [0, 1, 1, 0], [1, 0, 0, 1], [1, 1, 1, 1]]
    """
    def options(partial):
        if len(partial) < n//2 + n%2:
            return [0,1]

        return [partial[n-len(partial)-1]]
    def completed(partial):
        return len(partial) == n

    return solutions(completed, options, [])

# Part B - All Paths (0.5 Marks)
def all_paths(M, u, v):
    """
    Input: Graph 'M' as adjacency matrix, and vertexes 'u' and 'v'
    Output: List of vertices in lexicographical order that finds 
            all paths from 'u' to 'v'.
    
    For Example:
    >>> M = [ [0, 1, 1, 0],
    ...       [1, 0, 1, 1],
    ...       [1, 1, 0, 0],
    ...       [0, 1, 0, 0]]
    >>> all_paths(M, 0, 1)
    [[0, 1], [0, 2, 1]]
    >>> all_paths(M, 1, 0)
    [[1, 0], [1, 2, 0]]
    >>> all_paths(M, 0, 3)
    [[0, 1, 3], [0, 2, 1, 3]]
    >>> all_paths(M, 2, 3)
    [[2, 0, 1, 3], [2, 1, 3]]
    """
    def options(partial):
        opt = []
        for i in range(len(M)):
            if M[partial[-1]][i] and i not in partial:
                opt += [i]
            return opt
        def completed(partial):
            return partial[-1] == v
    return solutions(completed, options, [u])

# Part C - Stairs (0.5 Marks)
def stairs(staircase):
    """
    Input: Bitlist (list of lists) representing a staircase input where 1
           represents a safe stair, and 0 represents an unsafe stair.
    Output: An integer which represents the number of possible ways to
            climb the stairs given the restrictions by allowing to jump
            the staircase by jumping one step, two steps or three steps; but
            you are not allowed to jump the same number of steps twice in a
            row.
    
    For Example:
    >>> stairs([1, 1, 0, 1, 1])
    3
    >>> stairs([1, 0, 1, 0, 1])
    0
    >>> stairs([1, 0, 0, 1])
    1
    >>> stairs([1, 1, 0, 1])
    2
    >>> stairs([1, 1, 1, 1])
    3
    """
    def options(partial):
        opt = []
        if len(partial) == 1:
            for i in range(1, 4):
                if i < len(staircase) and staircase[i]:
                    opt += [i]
        else:
            prohib = partial[-1]-partial[-2]
            for i in range(1,4):
                if i != prohib:
                    stair = partial[-1] + i
                    if stair<len(staricase) and staircase[stair]:
                        opt += [stair]
        return opt
    def complete(partial): return partial[-1] == len(staircase) - 1
    return len(solutions(complete, options, [0]))

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
