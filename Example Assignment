"""
Author: <name> (<student_id>)

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


# Part 1 (due Week 6) #


def satisfies(product, cond):
    """
    Determines whether a product satisfies a given condition.

    Input : A product feature list (product() and a condition
            (cond) as specified above.
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

    <Paragraph on problem, challenges, and overall approach.>

    <Paragraph on specific programming techniques and Python
     language elements used.>

    """
    pass


def selection(products, conditions):
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
    [['Galaxy S20', 'Samsung', 6.2, 4000, 1348], ['Nova 5T', 'Huawei', 6.26, 3750, 497], ['V40 ThinQ', 'LG', 6.4, 3300, 598], ['Reno Z', 'Oppo', 6.4, 4035, 397]]

    <Paragraph on problem, challenges, and overall approach.>

    <Paragraph on specific programming techniques and Python
     language elements used.>

    """
    pass


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
    [['Reno Z', 'Oppo', 6.4, 4035, 397], ['Galaxy S20', 'Samsung', 6.2, 4000, 1348], ['Nova 5T', 'Huawei', 6.26, 3750, 497], ['V40 ThinQ', 'LG', 6.4, 3300, 598], ['iPhone11', 'Apple', 6.1, 3110, 1280]]
    >>> screen_battery_price = [None, None, 10, 1/1000, -1/100]
    >>> linearly_ranked(phones, screen_battery_price)
    [['Reno Z', 'Oppo', 6.4, 4035, 397], ['Nova 5T', 'Huawei', 6.26, 3750, 497], ['V40 ThinQ', 'LG', 6.4, 3300, 598], ['Galaxy S20', 'Samsung', 6.2, 4000, 1348], ['iPhone11', 'Apple', 6.1, 3110, 1280]]

    The input table is not changed by the function. That is
    after calling it, we still have:
    >>> phones
    [['iPhone11', 'Apple', 6.1, 3110, 1280], ['Galaxy S20', 'Samsung', 6.2, 4000, 1348], ['Nova 5T', 'Huawei', 6.26, 3750, 497], ['V40 ThinQ', 'LG', 6.4, 3300, 598], ['Reno Z', 'Oppo', 6.4, 4035, 397]]

    <Paragraph on problem, challenges, and overall approach.>

    <Paragraph on specific programming techniques and Python
     language elements used.>

    """
    pass


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
    [['Nova 5T', 'Huawei', 6.26, 3700, 497], ['P30 Pro', 'Huawei', 6.4, 3500, 398], ['Pixel 3', 'Google', 6.3, 3800, 688]]
    >>> big_screen = [(2,1)]
    >>> relevant(phones, big_screen)
    [['R17 Pro', 'Oppo', 6.6, 3200, 457]]
    >>> big_screen_but_cheap = [(2,1),(4,-1)]
    >>> relevant(phones, big_screen_but_cheap)
    [['P30 Pro', 'Huawei', 6.4, 3500, 398], ['R17 Pro', 'Oppo', 6.6, 3200, 457]]
    >>> big_screen_large_battery = [(2,1),(3,1)]
    >>> relevant(phones, big_screen_large_battery)
    [['P30 Pro', 'Huawei', 6.4, 3500, 398], ['R17 Pro', 'Oppo', 6.6, 3200, 457], ['Pixel 3', 'Google', 6.3, 3800, 688]]

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
    [['iPhone11', 'Apple', 6.1, 3110, 1280], ['Nova 5T', 'Huawei', 6.26, 3750, 497], ['V40 ThinQ', 'LG', 6.4, 3500, 800]]
    >>> selection(neg_ex, conds)
    [['7T', 'OnePlus', 6.3, 3300, 1200]]
    >>> selection(new_phones, conds)
    [['Galaxy Note 9', 'Samsung', 6.3, 3600, 700], ['A9 2020', 'Oppo', 6.4, 4000, 355]]

    <Paragraph on problem, challenges, and overall approach.>

    <Paragraph on specific programming techniques and Python
     language elements used.>

    <Paragraph on computational complexity.>

    """
    pass


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)