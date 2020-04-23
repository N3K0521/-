# Tutorial 4

# Prepared Question
'''
Your phone (likely) knows you who your most-used contacts are so they can be displayed on the
speed-dial page. Here are two different ways we could implement this functionality in Python.
'''
def speed_dial_v1(contact_list):
    sd_name, sd_number, sd_freq = contact_list.pop()
    while len(contact_list) > 0:
        name, number, freq = contact_list.pop()
        if freq > sd_freq:
            sd_name, sd_number, sd_freq = name, number, sd_freq
    return (sd_name, sd_number)

def speed_dial_v2(contact_list):
    sd_name, sd_number, sd_freq = contact_list[0]
    for contact in contact_list:
        name, number, freq = contact
        if freq > sd_freq:
            sd_name, sd_number, sd_freq = name, number, freq
    return (sd_name, sd_number)

# 1. Complete a code trace on these function cells, and record the values of x and y:

    list1 = [('Buffy', '04#', 5),('Blade', '04#', 2), ('Abe', '03#', 4)]
    x = speed_dial_v1

    list2 = [('Tiffany', '04#', 5),('Hermione', '07#', 2),('Morgan', '00#', 4)]
    y = speed_dial_v2

'''
Answer: 
For speed_dial_v1: 
1st-('Buffy', '04#', 5) 
2nd-('Buffy', '04#', 5) & ('Blade', '04#', 2) -> 5 > 2 -> ('Buffy', '04#', 5)
3rd-('Buffy', '04#', 5) & ('Abe', '03#', 4) -> 5 > 4 -> ('Buffy', '04#', 5)
4th-len(contact_list) < 0 -> loop ends
Return ('Buffy', '04#')

For speed_dial_v2:
1st-('Tiffany', '04#', 5)
2nd-the first thing in the list is Tiffany -> freq not > sd_freq -> keep the origin contact_list
3rd-the second thing is Hermione -> 2 is not > 5 -> Keep the origin contact_list
4rd-Morgan in the list -> 4 is not > 5 -> Keep the origin contact_list
5th-No contact left in the list needs to be tested
Return ('Tiffany', '04#')
'''

# 2. Which implementation do you think is better? Justify your answer.
'''
Answer:
I think the first implementation is better. Because you might call other people later, which means
the variables in the loop will increase, in this case using a "While loop" is better. (Because 
using a "for loop" requires a set number of trials.) 
'''