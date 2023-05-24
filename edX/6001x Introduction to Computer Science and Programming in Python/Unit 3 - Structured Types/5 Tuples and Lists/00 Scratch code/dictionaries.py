# Python dictionairies
#
# store pairs of data
#      - ket
#      - value
#
# Values: any type (immutable and mutable)
#         can be duplicates
#         dictionary values can be lists, even other dictionaries!
#
# Keys:   must be unique
#         must be immutable type (int, float, string, tuple, bool)
#             actually need an object that is hashtable, but think of as immutable as all
#             immutable types are hashable
#             * careful with float type as a key
#
# No order is guaranteed!
#
# Store diff object types
# -----------------------
# x = {1:{1:0}, (1,3):"string", "const":[3.14,2.7,8.44]}
#
# create dictionary
# -----------------
my_dict = {}  # empty dictionary, Note: curly braces
grades = {"Ana": "B", "John": "A+", "Denise": "A", "Katy": "A"}

# Retrieve value for a given key
# --------
grades["John"]  # returns A+
grades["Fred"]  # gives a KeyError

# Add a key, value pair
# ---------
grades["Fred"] = "A"

# Test if key in dictionary
# -------------------------
grades = {"Ana": "B", "John": "A+", "Denise": "A", "Katy": "A"}
"John" in grades  # returns a boolean value of True

# Test if value in dictionary
# ---------------------------
grades = {"Ana": "B", "John": "A+", "Denise": "A", "Katy": "A"}
"A" in grades.values()


# Delete entry, just as for lists, del (l[0]), we can use del command
# ------------
del (grades["Ana"])

# get an iterable that acts like a tuple of all keys
# --------------------------------------------------
grades = {"Ana": "B", "John": "A+", "Denise": "A", "Katy": "A"}
grades.keys()  # returns dict_keys(['Ana', 'John', 'Denise', 'Katy'])

# get an iterable that acts like a tuple of all values
# ----------------------------------------------------
grades = {"Ana": "B", "John": "A+", "Denise": "A", "Katy": "A"}
grades.values()  # returns dict_values(['B', 'A+', 'A', 'A']
