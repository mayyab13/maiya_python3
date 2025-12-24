def GCD(a, b):
    while b != 0:
        a, b = b, a % b
    return a

A = int(input("A: "))
B = int(input("B: "))
C = int(input("C: "))
D = int(input("D: "))

num = A * D
den = B * C

g = GCD(num, den)
num //= g
den //= g

print("Result:", num, "/", den)
