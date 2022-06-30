# Дан радиус окружности R. Найти ее длину и площадь
#  l=2πr
# S=πR²

import math
R = int(input())
p = 3.14
l = 2 * p * R
S = R ** 2 * math.pi
print('длина окружности: ' + str(l))
print( f'площадь окружности: {S} ')


