# tuples, a compound data type, are often used to swap varaiable values:
# ------
# x = y
# y = x --- Doesn't work, unable to swap vars. We could use a temp variable to get around this..
#
# temp = x
# x = y
# y = temp
#
# Better still, use a tuple
# (x,y) = (y,x) --- Creates a tuple with the bindings for x and y by simple taking the opposite versions in the tuple.
#
# tuples, are used to return more than one value from a function
# ------                                   def quotient_and_remainder(x,y):
#                                              q = x // y
#                                              r = x % y
#                                              return (q, r)
#                                          (quot, rem) + quotient_and_remainder(4,5)
#
#                                          t = (2,"one",3)
#                                          t[0] evaluates to 2
#                                          (2,"one",3) + (5,6) evaluates to (2,"one",3,5,6)
#                                          t[1:2] slice tuple, evaluates to ("one",) Note: extra ',' at the end
#                                                              means this is a tuple. i.e, ('one',) creates a tuple
#                                                              whereas the parenthesis ('one') in this case are treated
#                                                              as scoping things i.e. type string, not a tuple
#                                          t[1:3] slice tuple, evaluates to ("one",3)
#                                          t[1] = 4 gives error, can't modify object
# Note square brackets, that's because we're indexing

def get_data(aTuple):
    nums = ()  # empty tuple
    words = ()
    for t in aTuple:  # tuples are iterable
        # singleton tuple: just the int part e.g., (1, 'mine) and concatenate into nums
        nums = nums + (t[0],)
        if t[1] not in words:
            # singleton tuple: just the string part e.g., (1, 'mine) and concatenate into words
            words = words + (t[1],)
    min_nums = min(nums)
    max_nums = max(nums)
    unique_words = len(words)
    return (min_nums, max_nums, unique_words)


# aTuple consists of a collection of four tuples: aTuple((int,string), (int,string), (int,string), (int,string))
#
# test by looking for values by typing: small ; large ; words
# note how the tuple (small, large, words) creates and updates values for the int variables: small, large, and words
# value for 'small' is 1 ; 'large' is 7 ; 'words' is 3
(small, large, words) = get_data(((1, 'mine'),
                                  (3, 'yours'),
                                  (5, 'ours'),
                                  (7, 'mine')))
