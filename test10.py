# Дано двузначное число. Найти сумму и произведение его цифр.

a = int(input())
b = a // 10 
c = a % 10
sum = b + c
p = b * c
print(sum)
print(p)


