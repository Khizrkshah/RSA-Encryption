def extendedEuclidean(a, b):
    if b == 0:  # work till b is 0
        d, x, y = a, 1, 0  # d = ax + by and d|a and d|b
    else:
        d, x1, y1 = extendedEuclidean(b, a % b)  # a becomes b and b becomes remainder of a/b
        x = y1  # values interchanged     for b and a%b
        y = x1 - y1 * (a // b)  # values interchanged     a=b.q+r   q=quotient
    return d, x, y

