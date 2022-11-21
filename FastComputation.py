def fastComputation(a, b, m):
    r = 1  # return value initialized with 1
    while b > 0:  # power has to be greater than 0
        if b & 1 == 1:  # b&1 to get the least bit, and then check if the output is true with ==1
            r = (r * a) % m  # if the bit is 1, result is updated with the multiplication and mod (definition of recursive sequence)  x=a.b%m
        a = (pow(a, 2)) % m  # also definition of recursive sequence, the 2nd case, from online notes
        b >>= 1  # right shift operator keeps shifting to right till we get all binary values for b
    return r



