def rectangle_area(x, y):
    return x * y

def triangle_area(x, y):
    return 0.5 * x * y

x = float(input("X: "))
y = float(input("Y: "))
z = float(input("Z: "))
t = float(input("T: "))

area = rectangle_area(x, y) + triangle_area(z, t)
print(area)
