def GCD(a, b):
    while b:
        a, b = b, a % b
    return a

a = int(input("A: "))
b = int(input("B: "))

g = GCD(a, b)
lcm = (a * b) // g

print(g)
print(lcm)
