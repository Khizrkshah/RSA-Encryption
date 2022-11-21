from random import randint, randrange

from ExtendedEuclidean import extendedEuclidean
from FastComputation import fastComputation
from MillerRabin import millerRabinTest
from ChineseRemainder import chineseRemainder


def isPrime(number):
    for n in range(2, (number // 2) + 1):
        if number % n == 0:
            return False
    return True


def generateRandomPrimeNumber():
    number = int(randint(1, 10000))
    if isPrime(number):
        if millerRabinTest(number):
            return number
        else:
            return generateRandomPrimeNumber()
    else:
        return generateRandomPrimeNumber()


def encryption(e, n, message):
    cipher = ""  # initiate cipher text as empty

    for c in message:  # go through each character
        m = ord(c)  # to get the unicode value of the character
        cipher = cipher + str(fastComputation(m, e, n)) + " "

    return cipher


def decryption(d, p, q, cipher):
    message = ""  # initialise message as empty
    # characters = cipher.split()  # to make each character separated avoid confusion
    # for i in characters:
    #    c = int(i)  # convert the text to integer, value not actually required, just for message value / print(c)
    #    message = message + chr(fastComputation(c, d, n))  # convert again to string to get the message back

    characters = cipher.split()  # to make each character separated avoid confusion
    for i in characters:
        c = int(i)  # convert the text to integer, value not actually required, just for message value / print(c)
        message = message + chr(chineseRemainder(p, q, c, d))  # convert again to string to get the message back
    return message


def generatePrivateKey(p, q, e):
    phiN = (p - 1) * (q - 1)

    gcd, d, y = extendedEuclidean(e, phiN)  # getting the simplification for d.e=1mod(phi(n))
    d = d % ((p - 1) * (q - 1))  # from online notes, to get actual updated value of d
    return d


def generatePublicKey(n, p, q):
    e = randrange(1, n, 2)
    phiN = (p - 1) * (q - 1)
    gcd, x, y = extendedEuclidean(e, phiN)
    while gcd != 1:
        e = randrange(1, n, 2)
        gcd, x, y = extendedEuclidean(e, phiN)
    return e
