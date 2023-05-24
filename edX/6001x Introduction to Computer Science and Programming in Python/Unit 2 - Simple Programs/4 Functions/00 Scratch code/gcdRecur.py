def gcdRecur(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # https://en.wikipedia.org/wiki/Euclidean_algorithm greatest common divisor (GCD) / Highest Common Factor (HCF)
    # Euclid of Alexandria - Born Mid 4th centuary BC - often referred to as the "founder of geometry"
    if b == 0:
        return a

    return gcdRecur(b, a % b)


print(gcdRecur(9, 12))
