<<<<<<< HEAD
import time

fecha = time.localtime()
a = '{}/{}/{}'.format(fecha[2],fecha[1],fecha[0])
#a = fecha.fo    t(fecha[2],fecha[1],fecha[0])
temp = 25

if temp > 27:
    a = 1
else:
    a = 2 

form = {
    "email": str('jose'),
    "password": str('1234'),
}
#print(form['email'])

def calculo():
    return 1,2,3

a,b,c=calculo()
print(b)
=======
import time

fecha = time.localtime()
a = '{}/{}/{}'.format(fecha[2],fecha[1],fecha[0])
#a = fecha.fo    t(fecha[2],fecha[1],fecha[0])
temp = 25

if temp > 27:
    a = 1
else:
    a = 2 

form = {
    "email": str('jose'),
    "password": str('1234'),
}


print(form['email'])
>>>>>>> 254203cdecff57d8c0e2c3ba55fabc0b51bf8bca
