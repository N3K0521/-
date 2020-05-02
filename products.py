"""
Author: <Huixin Wang> (<31552544>)

In this assignment we implement the backend of an intelligent product
search engine where potential customers can search a database of products
characterized by different features taking into account the customer's
preferences.

Functions for 1 and 2 are due in Part 1 of the assignment. Functions
for 3 and 4 are due in Part 2.

As a global conventions, to select products based on hard criteria,
we will use Python objects representing conditions. These are represented
as triples (i, c, v) where i is an integer feature index, c is a relation
symbol in ['<', '<=' '==', '>=', '>', '!='], and v is some feature value.
A product (represented by a feature vector) _satisfies_ condition (i, c, v)
if its i-th feature value is in relation c with the value v. This will be
implemented in a function 'satisfies'. For example:
>>> inexpensive = (4, '<=', 1000)
>>> satisfies(['Nova 5T', 'Huawei', 6.26, 3750, 497], inexpensive)
True
>>> satisfies(['iPhone11', 'Apple', 6.1, 3110, 1280], inexpensive)
False

For more information see the function documentations below and the
assignment sheet.
"""

# Part 1

# Task A: Product selection

# Conditions
large_screen = (2,'>=', 6.3)
inexpensive = (4, '<=', 1000)
apple_product = (1, '==', 'apple')
not_apple = (1, '!=', 'Apple')
phones = [['iPhone11', 'Apple', 6.1, 3110, 1200], 
         ['Galaxy S20', 'Samsung', 6.2, 4000, 1348],
         ['Nova 5T', 'Huawei', 6.26, 3750, 497],
         ['V40 ThinQ', 'LG', 6.4, 3300, 598],
         ['Reno Z', 'Oppo', 6.4, 4035, 397]]
c = ['<', '<=', '==', '>=', '>', '!=']
not_apple = (1, '!=', 'Apple')

def satisfies(product, conds):
    """
    Determines whether a product satisfies a given condition.

    Input : A product feature list (product) and a condition
            (conds) as specified above.
    Output: True if cond holds for the product otherwise False.

    For example, consider the following conditions:
    >>> inexpensive = (4, '<=', 1000)
    >>> large_screen = (2, '>=', 6.3)
    >>> apple_product = (1, '==', 'Apple')

    With this the function behaves as follows:
    >>> satisfies(['Nova 5T', 'Huawei', 6.26, 3750, 497], inexpensive)
    True
    >>> satisfies(['iPhone11', 'Apple', 6.1, 3110, 1280], inexpensive)
    False
    >>> satisfies(['iPhone11', 'Apple', 6.1, 3110, 1280], large_screen)
    False
    >>> satisfies(['iPhone11', 'Apple', 6.1, 3110, 1280], apple_product)
    True
    
    Products are selected based on hard criteria, using Python objects
    representing conditions (i, c, v):
    i: representing an integer feature index
    c: relation symbol in ['<', '<=' '==', '>=', '>', '!=']
    v: some feature value

    A product (represented by a feature vector) satisfies condition (i, c, v)
    if its i-th feature value is in relation c with the value v. This will be
    implemented in this function, which is named as 'satisfies'.
    
    This function solves the problem of determining whether the input
    product satisfies the given condition by comparing its chosen feature
    to the condition's matching feature. This function allows users to see
    if the product input meets with the potential customers' demands.
    For the chosen term from the product feature list to be examined, we
    have to guarantee that only the feature required is tested. This
    implementation is based on the insight that looping can be used to
    execute examination with multi-conditions.
    
    In more detail, the function firstly examine the feature index "c" 
    by using the boolean expression, including the "if" and "elif" statement;
    after determining the target relation symbol, the function then compares
    the feature value "v" (from the triple) to the input product's matching
    feature value (from the list input), if satisfies, the output will be True;
    otherwise, it will return as False. 
    """
    feature = product[conds[0]]
    c = conds[1]
    if c == '>':
        if conds[2] > feature:
            return False
        return True
    elif c == '<':
        if conds[2] < feature:
            return False
        return True
    elif c == '==':
        if conds[2] == feature:
            return False
        return True
    elif c == '>=':
        if conds[2] >= feature:
            return False
        return True
    elif c == '<=':
        if conds[2] <= feature:
            return False
        return True
    elif conds[2] != feature:
        return False
    return True

def selection(products, conds):
    """
    Filters a given product table by a list of conditions.

    Input : A product table (products) and a list of conditions
            (conditions) consisting of triples (i, c, v) as specified
            in the module documentation.
    Output: The list of products satisfying all conditions.

    For example let's assume the following database of phones
    with features name, manufacturer, size, battery capacity, price.
    >>> phones = [['iPhone11', 'Apple', 6.1, 3110, 1280],
    ...           ['Galaxy S20', 'Samsung', 6.2, 4000, 1348],
    ...           ['Nova 5T', 'Huawei', 6.26, 3750, 497],
    ...           ['V40 ThinQ', 'LG', 6.4, 3300, 598],
    ...           ['Reno Z', 'Oppo', 6.4, 4035, 397]]

    Then the function behaves as follows:
    >>> large_screen = (2, '>=', 6.3)
    >>> cheap = (4, '<=', 400)
    >>> selection(phones, [cheap, large_screen])
    [['Reno Z', 'Oppo', 6.4, 4035, 397]]
    >>> not_apple = (1, '!=', 'Apple')
    >>> selection(phones, [not_apple])
    [['Galaxy S20', 'Samsung', 6.2, 4000, 1348],
     ['Nova 5T', 'Huawei', 6.26, 3750, 497],
     ['V40 ThinQ', 'LG', 6.4, 3300, 598],
     ['Reno Z', 'Oppo', 6.4, 4035, 397]]

    This function solves the problem of selecting all products satisfies the
    given conditions. Different to the first function, this function which is
    named as 'selection' examines a list of products against a triple of
    conditions. To achieve the purpose, the first function was injected to
    examine whether the input product satisfies each condition. After examining
    the first condition, if it's True, the ans will be saved as temporarily True
    and pass it to the next examination. If the product satisfies all conditions,
    the list will append to the final answer. If one examination returns False
    within the loop, the product will then be then confirmed as not satisfying
    the customers' preference.

    The programming techniques and Python language elements used including using
    the function previously defined, using a for loop inside a for loop to
    traverse each condition and etc. list.append(item) is a Python language element.
    The append function is used to add item at the end of the list. The item can
    be numbers, string, dictionaries and another list. Meanwhile, the if statements
    are also used. In this case, a break statement is used in the for loop to
    terminates the innermost loop since it is used inside a nested loop.
    """
    feature = products[conds[0]]
    ans = []
    for i in range(len(products)):
    	temp = True # Save as temporarily True if satisfies the first condition.
    	for j in range(len(conds)):
    		if satisfies(product[i], conds[j]):
    			temp = False
    			break
    	if temp == True:
    		ans.append(conds[i]) # Add it to the list if satisfies both conds.
    return ans 

# Task B: Product Ranking #
def data_sorted(data):
    """
    In this function, a selection sorted is used for recurrently finding the
    maximum data and make it become the first item, so the table can be sorted
    in a decreasing order (from maximum to the minimum). In this case, the input
    data is a table. Firstly, assuming the maximum product index as i, then keep
    comparing its next index with it by using the for loop, once the next index
    is greater than the initial index 'i', it will then be replaced(swap), and
    the following index will then be compared to the new temporarily maximum
    product index. By doing this, the table will then be sorted in a decending
    order, from the highest weights to the lowest.
    """
    for i in range(len(data)): 
        temporarily_max = i
        for j in range(i+1, len(data)):
            if data[j][1] > data[temporarily_max][1]:# comparing the weights
                temporarily_max = j
        data[i], data[temporarily_max] = data[temporarily_max], data[i] #swap
    return data

def specific_type(phones, weights):
    """
    The function below separates the case when the brand or model of the phone
    is specified. Since the first two features are strings which cannot be used
    to calculate the weights mathematically, they have to be discussed before
    the 'linearly_ranked' function.
    This function determines the cases include in:
    1. Neither brand or model is specified.
       (In this case, directly go back to the 'linearly_ranked' function)
    2. The model is specified.
    3. The brand is specified.
    4. Both the model and brand is specified.
    """
    ans = []
    if weights[0] == None and weights[1] == None:
        return phones
    if weights[0] == None and weights[1] != None:
        for i in range(len(phones)):
            if phones[i][1] == weights[1]:
                ans.append(phones[i])
        return ans
    if weights[0] != None and weights[1] == None:
        for i in range(len(phones)):
            if phones[i][0] == weights[0]:
                ans.append(phones[i])
        return ans
    if weights[0] != None and weights[1] != None:
        for i in range(len(phones)):
            if phones[i][0] == weights[0] and phones[i][1] == weights[1]:
                ans.append(phones[i])
        return ans
   
def linearly_ranked(products, weights):
    """
    Ranks products in order of preference as specified by a linear
    weight vector.

    Input : Product table (products) with n columns, list of
            weights of length n containing at position i the
            linear weight for product feature column i or None if
            no weight is specified for column i
            (must be None for non-numeric column).
            At least one weight must be different from None.
    Output: A new table containing all products from the input table
            in decreasing order of the linear score given, for a product
            prod in products, by the sum of prod[i]*weights[i] over
            all column indices i with weights[i]!=None.

    For example let's assume the following database of phones
    with features name, manufacturer, size, battery capacity, price:
    >>> phones = [['iPhone11', 'Apple', 6.1, 3110, 1280],
    ...           ['Galaxy S20', 'Samsung', 6.2, 4000, 1348],
    ...           ['Nova 5T', 'Huawei', 6.26, 3750, 497],
    ...           ['V40 ThinQ', 'LG', 6.4, 3300, 598],
    ...           ['Reno Z', 'Oppo', 6.4, 4035, 397]]

    This leads to the following behavior
    >>> battery = [None, None, None, 1, None]
    >>> linearly_ranked(phones, battery)
    [['Reno Z', 'Oppo', 6.4, 4035, 397],
     ['Galaxy S20', 'Samsung', 6.2, 4000, 1348],
     ['Nova 5T', 'Huawei', 6.26, 3750, 497],
     ['V40 ThinQ', 'LG', 6.4, 3300, 598],
     ['iPhone11', 'Apple', 6.1, 3110, 1280]]
    >>> screen_battery_price = [None, None, 10, 1/1000, -1/100]
    >>> linearly_ranked(phones, screen_battery_price)
    [['Reno Z', 'Oppo', 6.4, 4035, 397],
     ['Nova 5T', 'Huawei', 6.26, 3750, 497],
     ['V40 ThinQ', 'LG', 6.4, 3300, 598],
     ['Galaxy S20', 'Samsung', 6.2, 4000, 1348],
     ['iPhone11', 'Apple', 6.1, 3110, 1280]]

    The input table is not changed by the function. That is
    after calling it, we still have:
    >>> phones
    [['iPhone11', 'Apple', 6.1, 3110, 1280],
     ['Galaxy S20', 'Samsung', 6.2, 4000, 1348],
     ['Nova 5T', 'Huawei', 6.26, 3750, 497],
     ['V40 ThinQ', 'LG', 6.4, 3300, 598],
     ['Reno Z', 'Oppo', 6.4, 4035, 397]]

    This function is implied to solve the problem of ranking all products
    via a linear weight vector. After filtering the cases where brands or
    models are specified, the weight of each product will be calculated in
    this function below. Firstly, the weights feature are given as a tuple,
    to calculate the total weights of a product by adding all features'
    weights, it can be concluded as:
    total_weights = sum(products[i][2,3,4] * weight[2,3,4])
    which means adding the product of each product feature and its matching
    weight feature. After having the weights, the 'ans' in this function will
    become the input of the 'data_sorted' function above, to make the table be
    sorted in decending order. Then, the final answer will then be returned
    to the user showing the table of phones from highest weight to lowest with
    their feature details.

    In this function, programming techniques such as using a nested for loop
    and boolean statements are also applied; append function plays an important
    role in this function as well. Meanwhile, assignment operator like '+=' or
    '!=' is also used.
   """
    screen = weights[2]
    battery = weights[3]
    price = weights[4]
    products = specific_type(phones, weights)
    feature = products[conds[0]]
    ans = []
    final_ans = []
    for i in range(len(products)):
    	total_weights = 0
    	for j in range(2, len(products[i])):# products[i] = one product
    		if weights[feature] != None:
    			total_weights += products[i][feature] * weights[feature]
    	ans.append((products[i], total_weights))
    ans = data_sorted(ans)
    for i in range(len(ans)):
    	final_ans.append(ans[i][0])
    return final_ans

# Part 2 (due Week 11) #

def relevant(products, preferences):
    """
    Filters a product table for relevant products given user preferences.

    Input : A product table (products) and a list of preferences, where
            each preference is a pair (i, p) with i being the index of to a
            numeric column in products and p is either +1 or -1 depending
            on whether the user considers feature i to be positive or negative.
    Output: A new list of products that are relevant with respect to the
            preferences. A product is relevant if it is not dominated by another
            product, which is defined as follows:
            - prod1 dominates prod2 with respect to preference (i,p) if
              prod1[i] > prod2[i] in case p=1 (or prod1[i] < prod2[i] in case p=-1)
            - prod1 dominates prod2 if prod1 dominates prod2 with respect to at
              least one specified preference and not prod2 does not dominate prod2
              with respect to any specified preference

    For example:
    >>> phones = [['iPhone11', 'Apple', 6.1, 3110, 1280],
    ...           ['Galaxy S21', 'Samsung', 6.2, 3300, 1348],
    ...           ['Nova 5T', 'Huawei', 6.26, 3700, 497],
    ...           ['P30 Pro', 'Huawei', 6.4, 3500, 398],
    ...           ['R17 Pro', 'Oppo', 6.6, 3200, 457],
    ...           ['Pixel 3', 'Google', 6.3, 3800, 688]]
    >>> large_battery_but_cheap = [(3,1), (4,-1)]
    >>> relevant(phones, large_battery_but_cheap)
    [['Nova 5T', 'Huawei', 6.26, 3700, 497],
     ['P30 Pro', 'Huawei', 6.4, 3500, 398],
     ['Pixel 3', 'Google', 6.3, 3800, 688]]
    >>> big_screen = [(2,1)]
    >>> relevant(phones, big_screen)
    [['R17 Pro', 'Oppo', 6.6, 3200, 457]]
    >>> big_screen_but_cheap = [(2,1),(4,-1)]
    >>> relevant(phones, big_screen_but_cheap)
    [['P30 Pro', 'Huawei', 6.4, 3500, 398],
     ['R17 Pro', 'Oppo', 6.6, 3200, 457]]
    >>> big_screen_large_battery = [(2,1),(3,1)]
    >>> relevant(phones, big_screen_large_battery)
    [['P30 Pro', 'Huawei', 6.4, 3500, 398],
     ['R17 Pro', 'Oppo', 6.6, 3200, 457],
     ['Pixel 3', 'Google', 6.3, 3800, 688]]

    <Paragraph on problem, challenges, and overall approach.>

    <Paragraph on specific programming techniques and Python
     language elements used.>

    <Paragraph on computational complexity.>

    """
    pass
    

def inferred_conditions(pos_examples, neg_examples):
    """
    Infers selection conditions from positive and negative product examples.

    Input:  two non-empty lists of products, pos_examples and neg_examples,
            based on the same list of _numeric_ features
    Output: Set of conditions conds such that
            len(selection(neg_examples, conds)) is minimal
            under the constraint that
            selection(pos_examples, conds)==pos_examples

    Let's first consider a simple example with one column:
    >>> pos_ex = [[10], [14]]
    >>> neg_ex = [[4], [11], [20]]
    >>> conds = inferred_conditions(pos_ex, neg_ex)
    >>> selection(pos_ex, conds)
    [[10], [14]]
    >>> selection(neg_ex, conds)
    [[11]]

    For a more complex example, let's go back to our
    phone application. Assume the user has specified
    the following positive and negative examples.
    >>> pos_ex = [['iPhone11', 'Apple', 6.1, 3110, 1280],
    ...           ['Nova 5T', 'Huawei', 6.26, 3750, 497],
    ...           ['V40 ThinQ', 'LG', 6.4, 3500, 800]]
    >>> neg_ex = [['Galaxy S20', 'Samsung', 6.46, 3000, 1348],
    ...           ['V40 ThinQ', 'LG', 5.8, 3100, 598],
    ...           ['7T', 'OnePlus', 6.3, 3300, 1200]]

    Another table of new phones could be as follows.
    >>> new_phones = [['Galaxy S9', 'Samsung', 5.8, 3000, 728],
    ...               ['Galaxy Note 9', 'Samsung', 6.3, 3600, 700],
    ...               ['A9 2020', 'Oppo', 6.4, 4000, 355]]

    Then the conditions found by the function should behave
    as follows:
    >>> conds = inferred_conditions(pos_ex, neg_ex)
    >>> selection(pos_ex, conds)
    [['iPhone11', 'Apple', 6.1, 3110, 1280],
     ['Nova 5T', 'Huawei', 6.26, 3750, 497],
     ['V40 ThinQ', 'LG', 6.4, 3500, 800]]
    >>> selection(neg_ex, conds)
    [['7T', 'OnePlus', 6.3, 3300, 1200]]
    >>> selection(new_phones, conds)
    [['Galaxy Note 9', 'Samsung', 6.3, 3600, 700],
     ['A9 2020', 'Oppo', 6.4, 4000, 355]]

    <Paragraph on problem, challenges, and overall approach.>

    <Paragraph on specific programming techniques and Python
     language elements used.>

    <Paragraph on computational complexity.>

    """
    pass


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    
