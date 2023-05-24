'''
You can see what the Python collections.abc module considers to be a Collection and a Sequence:

collections.abc - Abstract Base Classes for Containers - Python 3.7.2 documentation
https://docs.python.org/3/library/collections.abc.html#collections-abstract-base-classes

Basically, a Sequence is a Collection that implements the __getitem__ and __len__ methods, excluding dictionaries
(because its __getitem__ accepts more than just integers; the Python sequence check has an explicit dictionary exclusion).

Are all the types you mentioned Collections? According to collections.abc the answer is “yes”:

abc = Abstract Base Class
https://docs.python.org/3/library/abc.html#module-abc
'''
from collections.abc import Collection, Sequence
all(issubclass(i, Collection) for i in [list, tuple, str, dict, set])  # True

# Great. But which of them are also Sequences?:

# https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
aList = [i for i in [list, tuple, str, bytes,
                     dict, set] if issubclass(i, Sequence)]
# [list, tuple, str, bytes]

# So, of those listed, just the list, tuple, str, and bytes types are Sequences.

'''
A list comprehension consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses.
The result will be a new list resulting from evaluating the expression in the context of the for and if clauses which follow it.
For example, this listcomp combines the elements of two lists if they are not equal:
'''

aList = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x == y]
# [(1, 1), (3, 3)]
aList = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
# [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

# and it’s equivalent to:

combs = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            combs.append((x, y))

'''
Note how the order of the for and if statements is the same in both these snippets.

If the expression is a tuple (e.g. the (x, y) in the above example), it must be parenthesized.
'''

# One more example....
squares = [i * i for i in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

'''
Rather than creating an empty list and adding each element to the end, you simply define the list and its contents at the same time by following this format:

new_list = [expression for member in iterable]

Every list comprehension in Python includes three elements:

    1. expression is the member itself, a call to a method, or any other valid expression that
       returns a value. In the example above, the expression i * i is the square of the
       member value.
    2. member is the object or value in the list or iterable. In the example above, the member
       value is i.
    3. iterable is a list, set, sequence, generator, or any other object that can return its
       elements one at a time. In the example above, the iterable is range(10).
'''
