#Searching:
def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1
"""
find -> inverse of the [] operator
takes a character and finds the index where that character appears
f not found, returns -1
"""

#looping and counting
word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count +1 
print(count)

#string method:
word = 'banana'
new_word = word.upper()
>>> 'BANANA'
word.find('na', 3) #optional argument
word.find('b', 1, 2) #third argument

#the in operator
'a' in 'banana'
>>> True
def in_both(word1, word2):
    for letter in word1:
        if letter in word2:
            print(letter)
            
#while loop
def sequence(n):
    while n != 1:
        print(n)
        if n % 2 == 0: #n is even
            n = n / 2
        else:
            n = n*3 + 1
"""
condition: n!=1 -> loop will continue until n is 1
each time: cheking whether the output is even or odd
if even: n is divided by 2
else: n is replaced with n*3 + 1
"""

#break
while True:
    line = input('>')
    if line == 'done':
        break
    print(line)
"""
check the condition anywhere in the loop
which canexpress the stop condition affirmatively
stop when this happens
"""

#lists are mautable, strings are not where you can't change it
#list methods:
lst.append(item) #adds item to the end of list lst
lst.count(item) # returns the number of occurrences of item in list lst
lst.index(item) # returns the index of the first occurrence of item in lst
lst.insert(index, item) insert item into list just before index index
lst.pop() removes last item in the list
lst.remove(item) removes first occurrence of item in the list
lst.reverse() reverses the order of items in the list
lst.sort() sorts the list #all numbers/strings, sort -> from lowest to highest
#tuple method
count()
index()

#reading word lists
>>> fin = open('words.txt') #fin is a common name for a file object used for input

>>> fin.readline()
'aa\r\n' # the next word is "aa"
>>> fin.readline()
'aa\r\n' #the next word is "aah"
#to remove the whitespace \r\n:
>>> line = fin.readline()
>>> word = line.strip()
>>> word
'aahed'

#use a file object as part of a for loop
fin = open('words.txt')
for line in fin:
    word = line.strip()
    print(word)
#the program reads words.txt and prints each word, one per line

#math modules:
sqrt(x) #square root
ceil(X) #smallest integer >= x
floor(x) #largest integer <= x
factorial(x) #x!(=x(x-1)(x-2)...1)
cos(x)
sin(x)
exp(x)
log(x)
>>> for math import sqrt #for module import function_name
>>> sqrt (2)

#list
[2:5] -> 2 included 5 excluded
[:3] not included the third 3rd term
[3:] including the third 3rd term

#Dijkstra's algorithm
node = find_lowest_code_node(costs)
while node is not None:
    cost = costs[node]
    neighbours = graph[node]
    for n in neighbours.keys():
        new_cost = cost + neighbours[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)

def find_lowest_code_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs: #traverse(遍历) all nodes
        cost = costs[node]
        if cost < lowest_cost and node not in processed: #if current node's cost is lower and not processed before
            lowest_cost = cost #this node will be the lowest cost node
            lowest_cost_node = node
        
