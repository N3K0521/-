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
    student_email = 'hwan0518' + '@student.monash.edu' #write your student email
    name = 'Huixin Wang' #write your name as it appears on Moodle
    return str(student_number), student_email, name


# Task 1
def word_from_file(file):
    f = open(file)
    res = []
    for i in f:
        i = i.replace('\n', '')
        line = i.split(',')
        word = line[0].strip()
        res = word
    return res
        
def nested_int_list_from_file(file):
    f = open(file)
    res = []
    for i in f:
        i = i.replace('\n', '')
        line = i.split(',')
        integer = []
        for j in line:
            integer.append(int(j))
        res.append(integer)
    return res

# Task 2
def degree(graph, vertex):
    res = 0
    for i in range(len(graph[vertex])):
        if graph[vertex][i] != 0:
            res = res + 1
    return res

def is_path(graph, path):
    for i in range(len(path)-1):
        if graph[path[i]][path[i+1]]:
            return True
        break
    return False
            

# Task 3
def print_as_grid(graph, n):
    """
    Input : Grid graph (graph), number of columns (n)
    Effect: Prints the graph organized as grid
    """
    
    def index(r, c):
        return r*n + c
    
    m = len(graph) // n
    
    for i in range(m):
        for j in range(n):
            print('*', end='')
            k = index(i, j)
            if j < n-1 and graph[k][index(i, j+1)]:
                print('---', end='')
            else:
                print('   ', end='')
        print('\n', end='')
        if i < m - 1:
            for j in range(n):
                k = index(i, j)
                if graph[k][index(i + 1, j)]:
                    print('|', end='')
                else:
                    print(' ', end='')
                if j < n-1:
                    print('   ', end='')
            print('\n', end='')

def grid_graph(m, n):
    pass


# Task 4
def sort_table(table, col):
    pass
