"""Даны действительные числа x и y. Получить
(|x| - |y|) / (1 + |xy|)"""

x = -9
y = -5

solution  = (abs(x - y)) / (1 + abs(x * y))

print("X: " + str(x))
print("Y: " + str(y) + "\n")

print("Solution: " + str(solution))
