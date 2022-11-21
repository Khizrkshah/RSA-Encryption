from ExtendedEuclidean import extendedEuclidean
from FastComputation import fastComputation


def chineseRemainder(p, q, c, d):
    n = p * q
    dp = d % (p - 1)
    dq = d % (q - 1)

    mp = fastComputation(c, dp, p)
    mq = fastComputation(c, dq, q)

    gcd, x, y = extendedEuclidean(p, q)

    m = (mp * y * q + mq * x * p) % n
    return m
