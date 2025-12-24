import math

a = float(input("rectangle side a: "))
b = float(input("rectangle side b: "))
rectangle_area = a * b
print(rectangle_area)

r = float(input("circle radius: "))
circle_area = math.pi * r * r
print(circle_area)

H = float(input("triangle height: "))
base = float(input("triangle base: "))
triangle_area = 0.5 * H * base
print(triangle_area)
