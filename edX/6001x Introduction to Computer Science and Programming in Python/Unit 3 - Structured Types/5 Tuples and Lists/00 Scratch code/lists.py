# lists (a compund data type)
# -----
#
# ordered sequence of information, accessible by index
# a list is denoted by square brackets, []
#
# a list contains elements
#    - usually homogeneous (i.e., all integers)
#    - can contaon mixed types (not common)
# list elements can be changed so a list is mutable
#
# lists, like tuples and strings are iterable and you can use slice operations
# ["a","b","c"][2] evaluates to string 'c'
# ["a","b","c"][0:2] evaluates to list ['a', 'b']
# ["a","b","c"][0:3] evaluates to list ['a', 'b', 'c']
#
# Sring iteration
# ---------------
s = "abc"
for i in a:
    print(f"type: {type(s)} value: {i}")
#
s = ("parens used for scoping")  # String
for i in a:
    print(f"type: {type(s)} value: {i}")
#
# Tuple iteration
# ---------------
t = ("a", "b", "c")
for i, char in enumerate(t):
    print(f"type: {type(t)} element: {i}, value: {char}")
#
t = ("singleton",)  # Tuple, note comma; ,
for i in t:
    print(f"type: {type(t)} value: {i}")
#
# List iteration
# --------------
l = ["a", "b", "c"]
for i in l:
    print(f"type: {type(l)} value: {i}")
#
# Lists - operations on lists - add
# ---------------------------------
l1 = ["a", "b", "c"]
l1.append("d")  # add element to end of list, restricted to 1 element at a time
l1.extend(["e", "f"])  # add multiple elements to end of list
#                  the dot: objects have methods and functions
#                  access this information by object_name.do_something()
l2 = ["g", "h"]  # combine lists together using + operator, to give you a new list
l1 += l2
for i in l1:  # note entire list can be refrenced with slicing [:]
    print(f"type: {type(l1)} value: {i}")
#
# Lists - operations on lists - remove
# ------------------------------------
l = ["a", "b", "c", "d", "e", "f", "g", "a"]
l.remove("a")  # mutates l by deleting first element who's value is "a"
del (l[0])  # mutates l by deleting element 0
l.pop()  # mutates l by deleting highest element
print(f"l.remove(\"a\"): {l}")
#
# other list operations
# ---------------------
#
# l.sort(), l.reverse() >>> mutates l
l = [1, 4, 3, 0]
l.sort()  # mutates l=[0,1,3,4]
l.reverse()  # mutates l=[4,4,2,0]
sorted(l)  # returns sorted list, does not mutate
# sorted(l) >>> returns soreted list, without mutating l
#
# https://docs.python.org/3/tutorial/datastructures.html
#
# ALIASES: variables porinting to the same object in memory, could be lists or other object types
# --------
# warm = ["red","yellow","orange"]
# hot = warm
# hot.append("pink")
#
# Cloning a list (create a new list and copy every elemenet using: newList = fromList[:]
# --------------
l = ["a", "b"]
newList = list[:]
print(F"list: {l} ; newList: {newList}")
#
# Find element index for a given value
# ------------------------------------
l = ["a", "b"]
print(f"l.index(2): {l.index('b')}")  # returns l.index(2): 1
#
# Convert lists to strings and back
# ---------------------------------
# split()
s = "abc"
newList = list(s)  # list(stringVar): convert a string to list ['a', 'b', 'c']
# ''.join(listVar): convert a list to a string with commas inserted 'a,b,c'
','.join(newList)
# convert string to list returns ['', 'bc'], splits on spaces if called without a parameter
s.split("a")
# convert string to list returns ['a', 'c'], splits on spaces if called without a parameter
s.split("b")
# convert string to list returns ['ab', ''], splits on spaces if called without a parameter
s.split("c")
# convert string to list returns ['abc'], splits on spaces if called without a parameter
s.split("x")
