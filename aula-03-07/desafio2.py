import math
import os
os.system("cls")

a = -1

b = 2

c = 3

delta = (b ** 2) - 4 * a * c

print(f"Delta: {delta} |", end = " ")

x1 = (-b + (delta ** (1/2))) / (2 * a)
x2 = (-b - math.sqrt(delta)) / (2 * a)


print(f"x1 = {x1} | x2 = {x2}")