# На ввод дается логин в виде почты (@) и пароль
# Если в логине присутствует символ @ и пароль больше или равно 8 символов
# Вывести "Correct"
# Иначе Incorrect


a = input()
b = input()



if '@' in a and len(b) >= 8:
    print('Correct')
else:
    print('Incorrect')