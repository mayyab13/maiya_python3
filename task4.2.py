def inside_circle(x, y, r):
    return x*x + y*y <= r*r

r = float(input("radius: "))

points = [(1, 1), (2, 2), (3, 3)]
count = 0

for p in points:
    if inside_circle(p[0], p[1], r):
        count += 1

print(count)
print("Calculation completed.")
