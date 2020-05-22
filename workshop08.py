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


def gcd(a, b):
    """ Determines greatest common divisor of two integers.
    
    Input : two integers a and b such that not a==b==0
    Output: greatest common divisor of a and b
    
    For example:
    >>> gcd(0, 4)
    4
    >>> gcd(10, 0)
    10
    >>> gcd(18, 27)
    9
    >>> gcd(21, 13)
    1
    """
    if b == 0:
        return a
    return gcd(b, a%b)


def reverse(lst):
    """ Computes reverse of input sequence.
    
    Input : any list (lst)
    Output: reverse of lst
    
    For example:
    >>> reverse([1, 2, 3, 4])
    [4, 3, 2, 1]
    >>> reverse([10, 11, 12, 13, 14])
    [14, 13, 12, 11, 10]
    >>> reverse([1])
    [1]
    >>> reverse([])
    []
    """
    if len(lst) == 0:
        return lst
    else:
        return (reverse(lst[1:]) + [lst[0]])


def is_pal(string):
    """Checks whether string is palindrome.
    
    Input : any string
    Output: True if string==string[::-1]
    
    For example:
    >>> is_pal('aa')
    True
    >>> is_pal('aabb')
    False
    >>> is_pal('aba')
    True
    """
    a = reversed(list(string))
    if list(a) == list(string):
        return True
    else:
        return False


from collections import deque
from graphs import neighbours, print_grid_traversal
import graphs

def bfs_traversal(graph, s, goals=[]):
    """
    >>> g = graphs.ex_tree
    >>> bfs_traversal(g, 0, {12})
    [0, 1, 2, 12]
    >>> print_grid_traversal(g, 10, bfs_traversal(g, 0, {12}))
    000---001---002   ***---***   ***---***   ***---***---***   
                 |     |           |           |           |
    ***---***---003---***---***---***---***---***---***   ***   
                 |                 |     |     |     |     |
    ***---***---***---***---***   ***   ***   ***   ***   ***   
     |     |     |                       |           |      
    ***   ***   ***---***---***---***   ***---***   ***---***   
     |     |           |     |                              
    ***   ***---***   ***   ***---***---***---***---***---***   
    >>> print_grid_traversal(g, 10, bfs_traversal(g, 0, {22}))
    000---001---002   ***---***   ***---***   ***---***---***   
                 |     |           |           |           |
    ***---004---003---005---***---***---***---***---***   ***   
                 |                 |     |     |     |     |
    ***---***---006---***---***   ***   ***   ***   ***   ***   
     |     |     |                       |           |      
    ***   ***   ***---***---***---***   ***---***   ***---***   
     |     |           |     |                              
    ***   ***---***   ***   ***---***---***---***---***---***   
    """
    visited = []
    boundary = [s]
    while len(boundary) > 0:
        v = boundary.pop(0)
        visited += [v]
        for w in neighbours(v, graph):
            if w not in goals:
                if w not in visited and w not in boundary:
                    boundary.append(w)
            else:
                if w not in visited and w not in boundary:
                    boundary.append(w)
                    v = boundary.pop(0)
                    visited += [v]
                break
    return visited
    
def dfs_traversal(graph, s, goals=[]):
    """
    >>> g = graphs.ex_tree
    >>> print_grid_traversal(g, 10, dfs_traversal(g, 0, {12}))
    000---001---002   ***---***   ***---***   ***---***---***   
                 |     |           |           |           |
    ***---***---003---***---***---***---***---***---***   ***   
                 |                 |     |     |     |     |
    ***---***---***---***---***   ***   ***   ***   ***   ***   
     |     |     |                       |           |      
    ***   ***   ***---***---***---***   ***---***   ***---***   
     |     |           |     |                              
    ***   ***---***   ***   ***---***---***---***---***---***   
    >>> print_grid_traversal(g, 10, dfs_traversal(g, 0, {9, 40, 49}))
    000---001---002   ***---***   ***---***   ***---***---***   
                 |     |           |           |           |
    ***---***---003---***---***---***---***---***---***   ***   
                 |                 |     |     |     |     |
    ***---***---004---***---***   ***   ***   ***   ***   ***   
     |     |     |                       |           |      
    ***   ***   005---006---008---***   ***---***   ***---***   
     |     |           |     |                              
    ***   ***---***   007   009---010---011---012---013---014   
    """
    visited = []
    boundary = [s]
    while len(boundary) > 0:
        v = boundary.pop()
        visited += [v]
        for w in neighbours(v, graph):
            if w not in visited and w not in boundary:
                boundary.append(w)
                if w in goals:
                    v = boundary.pop()
                    visited += [v]
    return visited

def get_path(parent_list, s, e):
    reversed_path = [e]
    while s not in reversed_path:#our reversed path doesn't contain starting vertex:
        v = reversed_path[-1]
        if v == None:
            break
        reversed_path.append(parent_list[v])
    return reverse(reversed_path)#reverse reversed_path

def bfs_path(graph, s, goals=[]):
    """
    >>> g = graphs.ex_tree
    >>> print_grid_traversal(g, 10, bfs_path(g, 0, {22}))
    000---001---002   ***---***   ***---***   ***---***---***   
                 |     |           |           |           |
    ***---***---003---***---***---***---***---***---***   ***   
                 |                 |     |     |     |     |
    ***---***---004---***---***   ***   ***   ***   ***   ***   
     |     |     |                       |           |      
    ***   ***   ***---***---***---***   ***---***   ***---***   
     |     |           |     |                              
    ***   ***---***   ***   ***---***---***---***---***---***   
    """
    visited = []
    parents = [None]*len(graph)
    boundary = [s]
    while len(boundary) > 0:
        v = boundary.pop(0)
        visited += [v]
        for w in neighbours(v, graph):
            if w not in visited and w not in boundary:
                boundary.append(w)
                parents[w] = v
                #w's parent
                # put w's parent in the partent list
    return get_path(parents, goals[0], goals[1])


def dfs_path(graph, s, goals=[]):
    """
    >>> g = graphs.ex_tree
    >>> print_grid_traversal(g, 10, dfs_path(g, 0, [9, 39]))
    000---001---002   ***---***   ***---***   ***---***---***   
                 |     |           |           |           |
    ***---***---003---004---005---006---007---008---009   ***   
                 |                 |     |     |     |     |
    ***---***---***---***---***   ***   ***   ***   010   ***   
     |     |     |                       |           |      
    ***   ***   ***---***---***---***   ***---***   011---012   
     |     |           |     |                              
    ***   ***---***   ***   ***---***---***---***---***---***   
    """
    visited = []
    parents = [None]*(len(graph))
    boundary = [s]
    while len(boundary) > 0:
        v = boundary.pop()
        visited += [v]
        for w in neighbours(v, graph):
            if w not in visited and w not in boundary:
                boundary.append(w)
                parents[w] = v
    return get_path(parents, goals[0], goals[1])


if __name__=='__main__':
    """
    when the path is unweighted, bfs psth is shorter than the dfs path
    when every pari of vertices are joined by an edge, which is called
    as a complete graph.
    
    """

    import doctest
    doctest.testmod(verbose=True)
