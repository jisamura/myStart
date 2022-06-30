# Даны радиус круга и сторона квадрата. У какой фигуры площадь больше?
# S=πR²

Ra = float(input())

s = 3.14 * Ra ** 2

a = float(input())

S = a ** 2

if s > S:
    print(s)
elif s < S:
    print(S)


