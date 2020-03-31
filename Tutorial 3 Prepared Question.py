'''
Prepared Question:
Alcohol is a drug that is processed by the body in a relatively predictable way. Because alcohol can
impair an individual's driving, in Australia you are not legally allowed to drive unless your blood
alcohol level (BAL) is below 0.05%. It takes approximately one hour for your BAL to decrease by 0.015.

1. 
Implement in Python a function, hours_to_legal_limit(bal), that takes an individual's current BAL and returns an integer
representing the number of hours that individual must wait before they can legally drive, rounded to the larger number (we
want to be on the safe side!). You must use either a for-loop or a while-loop inside your function. The function can be 
handwritten.

2. 
Explain why you chose to use one kind of loop instead of the other kind. The explanation can be short, but it must be 
meaningful.
'''

def hours_to_legal_limit(bal):
    number_of_hours = 0
    while bal >= 0.15:
        number_of_hours += 1
        bal = bal - 0.015
    print(number_of_hours)

'''
I used a while loop because this case was conditional, which might be run ultimately until the condition was achieved. 
For loops are more suitable in the case when implement time is known.
''' 
