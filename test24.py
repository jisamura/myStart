# Определить, является ли число a делителем числа b?

a = int(input())
b = int(input())
 
if b % a == 0:
    print(' Да,является ')
else:
    print(' Нет,не является ')