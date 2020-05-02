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
    word = ''
    while word == '':
        line = f.readline().strip().split()
        if len(line) > 0:
            word = line[0]
    f.close()
    return word
        
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
    for v in range(len(path)-1):
        if path[v] >= len(graph) or path[v+1] >= len(graph):
            return False
        if graph[path[v]][path[v+1]] == 0:
            return False
    return True
            

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
    def row_index(k):
        return k // n
    def col_index(k):
        return k % n
    def neighbors(i):
        res = []
        if col_index(i) > 0:
            res.append(i-1)
        if col_index(i) < n - 1:
            res.append(i+1)
        if row_index(i) > 0:
            res.append(i-n)
        if row_index(i) < m-1:
            res.append(i+n)
        return res

    graph = []
    for i in range(m*n):
        row = []
        nb = neighbors(i)
        for j in range(m*n):
            if j in nb:
                row.append(1)
            else:
                row.append(0)
    return graph


# Task 4
def insert(k, table, i):
    j = k
    while j > 0 and table[j-1][i] > table[j][i]:
        table[j-1], table[j] = table[j], table[j-1]
        j = j - 1
def sort_table(table, col):
    for row in range(1, len(table)):
        insert(row, table, col)
