def GCD(a, b):
    while b:
        a, b = b, a % b
    return a

A = int(input("A: "))
B = int(input("B: "))
C = int(input("C: "))
D = int(input("D: "))

num = A * D - B * C
den = B * D

g = GCD(abs(num), den)
num //= g
den //= g

print(num, "/", den)
