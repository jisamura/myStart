# На ввод даются параметры деталей компьютера CPU, RAM, SSD, Monitor.
# Если параметр существует в соответствующем списке (создать списки доступных параметров) то произвести расчет
# Иначе вывести "Вы ввели не существующий параметр"
# Не забыть добавить скидку в 5% при стоимость ПК > 60000



cpucores =  int(input('CPU Cores [2, 4, 6, 8]: '))
ram = int(input('RAM GB [4, 8, 16, 32]: '))
ssd = int(input('SSD GB [128, 256, 512]: '))
monitor = int(input('Monitor [24, 27, 32]: '))

lista = [2, 4, 6, 8]

listb = [4, 8, 16, 32]

listc = [128, 256, 512]

listd = [24, 27, 32]

if cpucores in lista and ram in listb and ssd in listc and monitor in listd:
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
else:
    print(' Вы ввели не существующий параметр ')