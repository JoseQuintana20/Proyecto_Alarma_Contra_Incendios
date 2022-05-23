import mysql.connector
from decouple import config
from flask import Flask, render_template, request, redirect, url_for, flash, Response, stream_with_context


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

def guardarDB2(mydb, email, password):
    cur = mydb.cursor()
    cur.execute('INSERT INTO datos_form (email, password) VALUES ("{email}",  "{password}")'.format(
        email=email, password=password))
    cur.close()

def formDB(email, password):
    mydb = conectarDB()
    guardarDB2(mydb, email, password)


def cargarDB(valores):
    mydb = conectarDB()
    guardarDB(mydb, valores)
