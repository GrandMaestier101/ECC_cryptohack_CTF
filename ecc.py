from inspect import CO_OPTIMIZED
from operator import mod


def mulIn(x):

    if x % p == 0:
        raise ZeroDivisionError("Impossible inverse")
    return pow(x, p - 2, p)


def poinAdd(x1, y1, x2, y2, p, a):

    if x1 == x2:
        s = ((3 * (x1**2) + a) * mulIn(2 * y1)) % p
    else:
        s = ((y2 - y1) * mulIn(x2 - x1)) % p
    x3 = (s**2 - x1 - x2) % p
    y3 = (s * (x1 - x3) - y1) % p
    return (x3, y3)


def ecc_double(x1, y1, p, a):
    s = ((3 * (x1**2) + a) * mulIn(2 * y1)) % p
    x3 = (s**2 - x1 - x1) % p
    y3 = (s * (x1 - x3) - y1) % p
    return (x3, y3)


def double_and_add(multi, N, p, a):
    (x3, y3) = (0, 0)
    (x1, y1) = N
    (xtem, ytem) = N
    init = 0
    for i in str(bin(multi)[2:]):
        if (i == "1") and (init == 0):
            init = 1
        elif (i == "1") and (init == 1):
            (x3, y3) = ecc_double(xtem, ytem, p, a)
            (x3, y3) = poinAdd(x1, y1, x3, y3, p, a)
            (xtem, ytem) = (x3, y3)
        else:
            (x3, y3) = ecc_double(xtem, ytem, p, a)
            (xtem, ytem) = (x3, y3)
    return (x3, y3)


p = 9739
a = 497
b = 1768
N = (2339, 2213)
print(double_and_add(7863, N, p, a))
