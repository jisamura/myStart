cpucores =  int(input('CPU Cores [2, 4, 6, 8]: '))
ram = int(input('RAM GB [4, 8, 16, 32]: '))
ssd = int(input('SSD GB [128, 256, 512]: '))
monitor = int(input('Monitor [24, 27, 32]: '))
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
print('Total: ' + str(Total) + ' RUB')



# Цену каждой детали.
# “CPU: 10000 RUB”
# “RAM: 10000 RUB”
# “MotherBoard: 10000 RUB”
# “SSD: 10000 RUB”
# “PSU: 10000 RUB”
# “Case: 10000 RUB”
# “Monitor: 10000 RUB”
# Итоговую стоимость.
# “Total: 100000 RUB”