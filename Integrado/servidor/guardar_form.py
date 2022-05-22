import mysql.connector
from decouple import config


def conectarDB():
    mydb = mysql.connector.connect(
        host='localhost',
        user=config('USER_DB'),
        password=config('PASSWORD_DB'),
        database=config('NAME_DB2')
    )

    return mydb

def guardarDB(mydb):
    cur = mydb.cursor()
    cur.execute('INSERT INTO datos (email, password) VALUES ("{email}",  "{password}")'.format(
        email=email, password=password))
    cur.close()

def formDB():
    mydb = conectarDB()
    guardarDB(mydb)


