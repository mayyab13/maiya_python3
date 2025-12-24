import math

def hypotenuse(a, b):
    return math.sqrt(a*a + b*b)

a1 = float(input("Triangle 1 side a: "))
b1 = float(input("Triangle 1 side b: "))
a2 = float(input("Triangle 2 side a: "))
b2 = float(input("Triangle 2 side b: "))

h1 = hypotenuse(a1, b1)
h2 = hypotenuse(a2, b2)

print("Hypotenuse 1:", h1)
print("Hypotenuse 2:", h2)

if h1 > h2:
    print("First is larger")
else:
    print("Second is larger")
