import math

a = float(input("rectangle side a: "))
b = float(input("rectangle side b: "))
rectangle_area = a * b
print("Rectangle area:", rectangle_area)

r = float(input("circle radius: "))
circle_area = math.pi * r * r
print("Circle area:", circle_area)

H = float(input("triangle height: "))
base = float(input("triangle base: "))
triangle_area = 0.5 * H * base
print("Triangle area:", triangle_area)
print("Areas calculated successfully.")