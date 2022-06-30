# На ввод даются 3 числа.
# Вывести True or False если треугольник с такими длинами может существовать.

a = int(input())
b = int(input())
c = int(input())

print(a + b > c and b + c > a and c + a > b )