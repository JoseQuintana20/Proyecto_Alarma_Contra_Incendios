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