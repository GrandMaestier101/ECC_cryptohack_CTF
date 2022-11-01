import sys
import curve25519
import random
import ecc1


def getPoint(n, x):
    x2 = curve25519.X25519(n, x)
    z2 = (x2**3 + a * (x2**2) + x2) % p
    y2 = ecc1.modular_sqrt(z2, p)
    return (x2, y2)


type = "Curve25519_Montgomery"
p = pow(2, 255) - 19
a = 486662
b = 1
x = 9  # Base point

order = 57896044618658097711785492504343953926856930875039260848015607506283634007912

val = 21130179955454  # Compute valG


if len(sys.argv) > 1:
    val = int(sys.argv[1])

print("Curve 25519 (Montgomery)")
n = 1
G = getPoint(n, x)
print(f"Point {n}G: {G}")
n = 2
G2 = getPoint(n, x)
print(f"Point {n}G: {G2}")
n = 3
G3 = getPoint(n, x)
print(f"Point {n}G: {G3}")


Gv = getPoint(val, x)
print(f"\nPoint {val}G: {Gv}")

(xval, y) = Gv
xval = xval.to_bytes(32, byteorder="little").hex()
print(f"\n  Hex: {xval}")


val = random.randint(0, order)
Gv = getPoint(val, x)
print(f"\nPoint {val}G: {Gv}")

(xval, y) = Gv
xval = xval.to_bytes(32, byteorder="little").hex()
print(f"\n  Hex: {xval}")
