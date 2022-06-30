# После того как пользователь введет 4 числа проверить их все на равность 0.
# Если среди них есть хотя бы 1 ноль, то вывести "неправильные параметры"
# Иначе сделать расчет и вывести стоимости всех компонентов.
# Если итоговая стоимость больше 60000, сделать скидку 5%.


# if cpucores == 0:
#     print('Неправильные параметры')
# elif ram == 0:
#     print('Неправильные параметры') 
# elif ssd == 0:
#     print('Неправильные параметры')    
# elif monitor == 0:
#     print('Неправильные параметры')    

cpucores =  int(input('CPU Cores [2, 4, 6, 8]: '))
ram = int(input('RAM GB [4, 8, 16, 32]: '))
ssd = int(input('SSD GB [128, 256, 512]: '))
monitor = int(input('Monitor [24, 27, 32]: '))
if cpucores == 0 or ram == 0 or ssd == 0 or monitor == 0:
    print('неправильные параметры') 
else:
    cpuprice = cpucores * 3500
    ramprice = ram * 300
    mbprice = cpuprice * 0.4
    ssdprice = ssd * 16
    psu = cpucores * 100
    psuprice = psu * 10
    caseprice = mbprice * 0.6
    monitorprice = (monitor - 20) * 2500
    print('CPU: ' + str(cpuprice) + ' RUB')
    print('RAM: ' + str(ramprice) + ' RUB')
    print('MotherBoard: ' + str(mbprice) + ' RUB')
    print('SSD: ' + str(ssdprice) + ' RUB')
    print('PSU: ' + str(psuprice) + ' RUB' )
    print('Case: ' + str(caseprice) + ' RUB')
    print('Monitor: ' + str(monitorprice) + ' RUB')
    Total = cpuprice + ramprice + mbprice + ssdprice + psuprice + caseprice + monitorprice
    if Total > 60000:
        Total = Total * 0.95
        print('Скидка 5 %')
    print('Total: ' + str(Total) + ' RUB')
        



