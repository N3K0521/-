# Tutorial 2

# Prepared Question

def accept_hypothesis(mu_hat, mu, sigma, n):
    z_score = (mu_hat - mu) / (sigma/n**0.5)
    # z_score = -15.0
    if z_score < 0:
        z_score *= -1
    # z_score = 15.0
    P = 0
    if z_score < 0.5:
        P = 0.5
    elif z_score < 1:
        P = 0.3
    elif z_score < 2:
        P = 0.15
    else:
        P = 0.02
    # P = 0.02
    p_value = 2*P
    # p_value = 0.04
    return p_value <= 0.05

answer = accept_hypothesis(5, 20, 4, 16)
# answer = True

# Real Roots

def real_roots(a, b, c):
    discriminant = (b * b) - (4 * a * c)
    if discriminant < 0:
        return []
    elif discriminant == 0:
        return [-b / (2 * a)]
    else:
        root_1 = (-b + discriminant ** (1/2)) / (2 * a)
        root_2 = (-b - discriminant ** (1/2)) / (2 * a)
        return [root_1, root_2]

# Unscrambling Code
# Part A - Magic Number

def magic_number(x, y, n):
    if x == n or y == n:
        return True
    elif x+ y == n:
        return True
    elif x-y == n or y-x == n:
        return True
    else:
        return False
# Part B - Icecream
def icecreams(x, summer):
    if summer:
        if 10-x > 0:
            return 10-x
        elif 2-x > 0:
            return 2-x
        return 0
# Part C - Rounding
def rounding(n):
    remainder = n%10
    num = n-remainder
    if remainder < 5:
        return num
    elif remainder > 5:
        return num + 10
    else:
        if num//10%2 == 0:
            return num
        else:
            return num + 10

# Checkpoint
# 1. What is the definition of an algorithm?
# "An algorithm is a sequence of unambiguous instructions for solving a problem, 
# i.e., for obtaining a required output for any legitimate input in a finite amount of time."

# 2. What does the following boolean expression yield?

10>10 or 6>=9 and -2<0 or not 9==5
#True

# 3. What is returned by the following function call?

def trace(x, y):
    if x%y == 0:
        return str(x) + ' is divided by ' + str(y)
    elif y%x == 0:
        return str(y) + ' is divided by' + str(x)
    else:
        return 'Neither divides'

trace(2, 4)
# 4 is divided by 2

# 4. Write a Python function, max, that takes two number, a and b, as arguments, 
# and returns the value of the largest number.

def max(a, b):
    if a > b:
        return a
    else:
        return b