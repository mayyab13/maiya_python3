import math

a = float(input("Side a: "))
b = float(input("Side b: "))
c = float(input("Side c: "))
d = float(input("Side d: "))
diag = float(input("Diagonal: "))

s1 = (a + b + diag) / 2
s2 = (c + d + diag) / 2

area1 = math.sqrt(s1 * (s1 - a) * (s1 - b) * (s1 - diag))
area2 = math.sqrt(s2 * (s2 - c) * (s2 - d) * (s2 - diag))

print(area1 + area2)
