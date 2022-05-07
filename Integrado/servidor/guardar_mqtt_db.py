import mysql.connector
from decouple import config


def conectarDB():
    mydb = mysql.connector.connect(
        host='localhost',
        user=config('USER_DB'),
        password=config('PASSWORD_DB'),
        database=config('NAME_DB')
    )

    return mydb


def guardarDB(mydb, valores):
    cur = mydb.cursor()
    cur.execute('INSERT INTO datos_tiempo_real (fecha_adquisicion, temp, temp_f) VALUES ("{fecha_adquisicion}", {temp}, {temp_f})'.format(
        fecha_adquisicion=valores['fecha'], temp=valores['temp'], temp_f=valores['temp_f']))
    cur.close()


def cargarDB(valores):
    mydb = conectarDB()
    guardarDB(mydb, valores)
