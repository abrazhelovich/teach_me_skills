"""Даны катеты прямоугольного треугольника. Найти его
гипотенузу и площадь."""

a = 3
b = 4

s = (a * b) / 2
l = pow((pow(a, 2) + pow(b, 2)), (1 / 2))

print("a: " + str(a))
print("b: " + str(b))
print("\nL: " + str(l))
print("S: " + str(s))
