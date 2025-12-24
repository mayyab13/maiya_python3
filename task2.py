import math

def triangle_area(a):
    return (math.sqrt(3) / 4) * a * a

a = float(input("side of hexagon: "))
hexagon_area = 6 * triangle_area(a)
print("Hexagon area:", hexagon_area)
print("Area calculated successfully.")