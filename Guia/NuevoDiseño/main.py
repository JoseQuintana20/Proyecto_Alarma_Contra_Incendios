from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector

app = Flask(__name__)

def conectarDB():
    mydb = mysql.connector.connect(
        host='localhost',
        user='admin',
        password='password',
        database='espdatos'
    )

    return mydb

# Conectar MySQL
mydb = conectarDB()

@app.route('/', methods=['GET', 'POST'])
def graficas():
    
    cur = mydb.cursor()
    cur.execute('SELECT actual FROM grafica')
    datocrudo = cur.fetchall()
    datosg = []
    print("Hello!")
    for i in datocrudo:
        datosg.append(i[0])
    tiempo = []
    for i in range(len(datosg)):
        tiempo.append(i)
    return render_template("graficas.html", datosg = datosg, tiempo = tiempo)
    
if __name__ == '__main__':
    app.run(debug=True)