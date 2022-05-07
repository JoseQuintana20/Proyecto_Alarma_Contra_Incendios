import time

fecha = time.localtime()
a = '{}/{}/{}'.format(fecha[2],fecha[1],fecha[0])
#a = fecha.fo    t(fecha[2],fecha[1],fecha[0])
temp = 29

if temp > 27:
    a=2

print(a)