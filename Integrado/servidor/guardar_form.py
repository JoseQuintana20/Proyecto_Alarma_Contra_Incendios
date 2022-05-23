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

def guardarDB(mydb):
    cur = mydb.cursor()
    cur.execute('INSERT INTO datos_form (email, password) VALUES ("{email}",  "{password}")'.format(
        email=email, password=password))
    cur.close()

def formDB(email, password):
    mydb = conectarDB()
    guardarDB(mydb, email, password)


