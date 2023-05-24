def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    # Your code here
    revDict = {}
    for key, value in d.items():
        if value not in revDict:
            revDict[value] = [key]
        else:
            revDict[value].append(key)
            revDict[value] = sorted(revDict[value])
    return revDict


d = {4: True, 2: True, 0: True}
print(dict_invert(d))
