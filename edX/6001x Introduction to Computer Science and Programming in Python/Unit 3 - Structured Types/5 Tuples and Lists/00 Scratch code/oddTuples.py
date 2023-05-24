def oddTuples(aTup):
    # print(aTup)
    '''
    aTup: a tuple

    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    values = ()
    for i, value in enumerate(aTup):
        if not i % 2:
            #print(str(i), value)
            values += aTup[i],
            # print(values)
    return(values)


reply = oddTuples(('I', 'am', 'a', 'test', 'tuple'))
print(reply)
# type(reply)


# Now for the elegent answer...

def oddTuples2(aTup):
    '''
    Another way to solve the problem.

    aTup: a tuple

    returns: tuple, every other element of aTup. 
    '''
    # Here is another solution to the problem that uses tuple
    #  slicing by 2 to achieve the same result
    return aTup[::2]


reply = oddTuples2(('I', 'am', 'a', 'test', 'tuple'))
print(reply)
