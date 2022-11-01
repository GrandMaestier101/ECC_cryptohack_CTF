from unicodedata import decimal


def mulIn(x, p):

    if x % p == 0:
        raise ZeroDivisionError("Impossible inverse")
    return pow(x, p - 2, p)


def ecc_double(x1, z1, A, p):
    v1 = x1 + z1
    v = (v1**2) % p
    v2 = x1 - z1
    u = (v2**2) % p
    u1 = v - u
    X3 = (u * v) % p
    v3 = (((A + 2) * mulIn(4, p)) * u1) % p
    v4 = u + v3
    Z3 = (u1 * v4) % p
    print("xDBL::", X3, Z3)
    return (X3, Z3)


def ecc_add(x1, z1, x2, z2, generator, p):
    (X, Z) = generator
    v0 = x1 + z1
    v1 = x2 - z2
    v1 = (v1 * v0) % p
    v00 = x1 - z1
    v22 = x2 + z2
    v2 = (v22 * v00) % p
    v3 = v1 + v2
    v33 = (v3**2) % p
    v4 = v1 - v2
    v44 = (v4**2) % p
    X3 = (v33 * Z) % p
    Z3 = (v44 * X) % p
    print("xADD::", X3, Z3)
    return (X3, Z3)


def double_and_add(multi, generator, p, A):
    (x3, y3) = (0, 0)
    (x1, y1) = generator
    (x_tmp, y_tmp) = generator
    (xt, zt) = ecc_double(x1, y1, A, p)
    print(bin(multi))

    for i in str(bin(multi)[3:]):
        if i == "0":
            print(i)
            (x1, y1) = ecc_double(x_tmp, y_tmp, A, p)
            (x3, y3) = ecc_add(xt, zt, x_tmp, y_tmp, generator, p)
            (x_tmp, y_tmp) = (x1, y1)
            (xt, zt) = (x3, y3)
        elif i == "1":
            print(i)
            (x1, y1) = ecc_add(xt, zt, x_tmp, y_tmp, generator, p)
            (x3, y3) = ecc_double(xt, zt, A, p)
            (xt, zt) = (x3, y3)
            (x_tmp, y_tmp) = (x1, y1)

    return (xt, zt, x_tmp, y_tmp)


p = (2**255) - 19
A = 486662
generator = (9, 1)
W = double_and_add(21130179955454, generator, p, A)
print(W)
xxp = 34655252392062538301926346329342767649606368749829230604528422469197693493395
xxq = 18975275063269890569938942933199878839539368781641748200071773296230514454196
print((xxp * mulIn(xxq, p)) % p)
xxp1 = 10862921441847926380086853109516164629078624641754609720823213339915381505097
xxq1 = 40151752408397156033331271149552828508158864411863909798375881344786581135636
print((xxp1 * mulIn(xxq1, p)) % p)
