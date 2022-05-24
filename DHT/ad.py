import time
import json

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
#print(b)

string = "((26.1,),)"
characters = "(,)"

#for x in range(len(characters)):
#    string = string.replace(characters[x],"")
#s = int(string)
#print(s)

variables = {
    "fecha": time.localtime(),
    "temp": 1,
    "temp_f": 2,
}

fecha = variables['fecha']
variables['fecha'] = '{}/{}/{}'.format(fecha[2],fecha[1],fecha[0])
print(variables['fecha'])
print(variables['temp'])
print(variables['temp_f'])
print("--------------------------------------------")
print(fecha)
print("--------------------------------------------")
print("--------------------------------------------")

payload = json.dumps(variables)
print(payload)
print("--------------------------------------------")


