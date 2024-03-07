import math
import os
os.system("cls")

a = -1

b = 2

c = 3

delta = (b ** 2) - 4 * a * c

print(f"Delta:{delta}")

x1 = (-b + math.sqrt(delta)) / (2 * a)
x2 = (-b - math.sqrt(delta)) / (2 * a)


print(x1)
print(x2)