print("a * x ^ 2 + b * x + c = 0")

a = int(input("a = "))

b = int(input("b = "))

c = int(input("c = "))

print(a, " * x ^ 2 + ", b, " * x + ", c, " = 0")

d = b ** 2 - 4 * a * c

print("D = ", d)

if d > 0:
    x1 = (-b + d ** -2) / (2 * a)
    x2 = (-b - d ** 2) / (2 * a)
    print("x1 = ", x1)
    print("x2 = ", x2)

elif d == 0:
    x = -b / (4 * a)
    print("x = ", x)
else:
    print("D < 0 => ar aqvs amonaxsni")
