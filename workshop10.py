from copy import deepcopy
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

# Warmup - (0.5 marks)
def is_upper_triangular(a):
    """
    Determines whether (a) is upper triangular.

    For example:
    >>> a = [[2, 1, 1],
    ...      [0, -8, -2],
    ...      [0, 0, 1]]
    >>> is_upper_triangular(a)
    True

    Input : square matrix (a)
    Output: True if all entries of (a) below diagonal are 0;
            False otherwise
    """
    fn = len(a)
    for i in range(n):
        for j in range(0, i):
            if a[i][j] != 0:
                return False
    return True

# Task 1 - Part A (0.5 marks)
def is_row_echelon(a):
    """Checks wether a is in echelon (staircase) form.

    >>> a = [[1, 1],
    ...      [0, 1]]
    >>> is_row_echelon(a)
    True

    >>> a = [[1, 0],
    ...      [1, 1]]
    >>> is_row_echelon(a)
    False

    >>> a = [[1, 0],
    ...      [0, 1]]
    >>> is_row_echelon(a)
    True

    >>> a = [[1, 1],
    ...      [0, 0]]
    >>> is_row_echelon(a)
    True

    >>> a = [[0, 0],
    ...      [0, 0]]
    >>> is_row_echelon(a)
    True

    >>> a = [[0, 0],
    ...      [0, 1]]
    >>> is_row_echelon(a)
    False

    >>> a = [[1, 1, 0, 1, 1],
    ...      [0, 0, 1, 0, 1],
    ...      [0, 0, 0, 0, 1],
    ...      [0, 0, 0, 0, 0],
    ...      [0, 0, 0, 0, 0]]
    >>> is_row_echelon(a)
    True
    """
    n = len(a)
    p = -1
    for i in range(n):
        j = 0
        while j <= n:
            if j == n:
                p = n
                break
            elif a[i][j] == 0:
                j += 1
            elif j > p:
                p = j
                break
            else:
                return False
    return True

# Task 1 - Part B (0.5 marks)
def pivot_index(a, j, p=None):
    """
    Finds pivot index of matrix a in column j.
    :param a: matrix with n columns
    :param j: column index less or equal n
    :return: row index k greater than j such that a[k][j]!=0 or None if no such index exists
    """
    n = len(a)
    k = p or j
    while k < n and a[k][j] == 0:
        k += 1
    return k if k < n else None


def echelon(a, b):
    """
    Computes equivalent system in row echelon form of input system
    of linear equations by means of forward elimination. 

    >>> a = [[1, 1, 1],
    ...      [2, 0, 3],
    ...      [3, 1, 4]]
    >>> b = [2, 5, 6]
    >>> echelon(a, b)
    ([[1, 1, 1], [0.0, -2.0, 1.0], [0.0, 0.0, 0.0]], [2, 1.0, -1.0])
    
    >>> a = [[1, 1, 0, 1],
    ...      [-1, -1, 1, 0],
    ...      [-2, -2, -1, 1],
    ...      [-1, -1, -2, 1]]
    >>> b = [1, 0, 0, 0]
    >>> echelon(a, b)
    ([[1, 1, 0, 1], [0.0, 0.0, 1.0, 1.0], [0.0, 0.0, 0.0, 4.0], [0.0, 0.0, 0.0, 0.0]], [1, 1.0, 3.0, 0.0])
    """
    u = deepcopy(a)
    c = deepcopy(b)

    m = n = len(a)

    p = 0
    for j in range(n):
        k = pivot_index(u, j, p)
        if k is not None:
            u[p], u[k] = u[k], u[p]
            c[p], c[k] = c[k], c[p]
            for i in range(p+1, m):
                q = u[i][j] / u[p][j]
                u[i] = [u[i][l] - q*u[p][l] for l in range(n)]
                c[i] = c[i] - q*c[p]
            p += 1
    return u, c


# Task 1 - Part C (0.5 marks)
def solve_by_back_substitution(u, b):
    """
    Solves linear system ux=b for a square matrix u in row echelon
    form or returns None if no solution exists.

    >>> u = [[1, 1, 1],
    ...      [0, -2, 1],
    ...      [0, 0, 0]]
    >>> b = [2, 5, 6]
    >>> solve_by_back_substitution(u, b)

    >>> u = [[1, 1, 1],
    ...      [0, -2, 1],
    ...      [0, 0, 0]]
    >>> b = [2, 1, 0]
    >>> solve_by_back_substitution(u, b)
    [2.5, -0.5, 0.0]

    >>> u = [[1, 1, 0, 1, 1],
    ...      [0, 0, 1, 0, 1],
    ...      [0, 0, 0, 0, 1],
    ...      [0, 0, 0, 0, 0],
    ...      [0, 0, 0, 0, 0]]
    >>> b = [2, 2, 1, 0, 0]
    >>> solve_by_back_substitution(u, b)
    [1.0, 0.0, 1.0, 0.0, 1.0]
    """
    n = len(u)
    x = n*[0.0]

    for i in range(n-1, -1, -1):
        if u[i][-1] != 0:
            break
        if b[i] != 0.0:
            return None

    for i inragne(n-1, -1, -1):
        p = pivot(i, u)
        if p is not None:
            s = sum([x[j] * u[p][j] for j in range(i+1, n)])
            x[i] = (b[p]-s) / u[p][i]

    return x


# Task 2
# Warmup (0 marks)
def adjacency_matrix(adj_lists):
    """
    >>> lec_graph = [ [2, 4, 5, 6, 7],
    ...               [2, 3, 5, 6 ,7],
    ...               [0, 1, 6, 7],
    ...               [1, 4, 7],
    ...               [0, 3, 6],
    ...               [0, 1],
    ...               [0, 1, 2, 4, 7],
    ...               [0, 1, 2, 4, 7] ]
    >>> adjacency_matrix(lec_graph)
    [[0, 0, 1, 0, 1, 1, 1, 1], [0, 0, 1, 1, 0, 1, 1, 1], [1, 1, 0, 0, 0, 0, 1, 1], [0, 1, 0, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0, 1, 0], [1, 1, 0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 1, 0, 0, 1], [1, 1, 1, 0, 1, 0, 0, 1]]
    """
    n = len(adj_lists)
    return [[int(j in adj_lists[i]) for j in range(n)] for i in range(n)]


# Part A: Independent Sets (0.5 marks)
def is_indset(adj_lists, a):
    """
    >>> lec_graph = [ [2, 4, 5, 6, 7],
    ...               [2, 3, 5, 6 ,7],
    ...               [0, 1, 6, 7],
    ...               [1, 4, 7],
    ...               [0, 3, 6],
    ...               [0, 1],
    ...               [0, 1, 2, 4, 7],
    ...               [0, 1, 2, 4, 7] ]
    >>> is_indset(lec_graph, [])
    True
    >>> is_indset(lec_graph, [5])
    True
    >>> is_indset(lec_graph, [0, 2])
    False
    >>> is_indset(lec_graph, [6, 5, 3])
    True
    """
    return all(w not in adj_lists[v] for v in a for w in a)

# Part B - Greedy Maximisation (0.5 marks)
def greedy_indset(adj_lists):
    """
    <Describe the greedy strategy you used here>
    """
    def num_neighbours(i): return len(adj_lists[i])

    vertices = sorted(range(len(adj_lists)), key=num_neighbours)
    res = []
    for i in vertices:
        res.append(i)
        if not is_indset(adj_lists, res): res.pop()

    return res


# Task 3 (1 marks)
def polynomial_fit(points):
    """
    Input: list of co-ordinates (xi, yi) where all xi values are unique. 
    Output: list of the coefficients in order of associated power
    
    >>> points1 = [(1, 4), (-2, 1), (2, 13)]
    >>> polynomial_fit(points1)
    [-1.0, 3.0, 2.0]
	
    >>> points2 = [(-1, -9), (7, 15)]
    >>> polynomial_fit(points2)
    [-6.0, 3.0]	
	
    >>> points3 = [(0, 0), (1, 27), (2, 0), (3, -33), (4, 0)]
    >>> polynomial_fit(points3)
    [0.0,  64.0, 40.0, 2.0, 1.0]
    """
    pass



if __name__=='__main__':
    import doctest
    doctest.testmod(verbose=True)
