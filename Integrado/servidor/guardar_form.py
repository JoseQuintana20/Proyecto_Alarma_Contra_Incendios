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

@app.route('/formulario', methods=['GET', 'POST'])
def ejemplo3():
    if request.method == 'POST':
        email = request.form['correo']
        password = request.form['contraseña']

        return render_template('visualizar.html', email=email, password=password)

    return render_template('formulario.html')

def guardarDB(mydb):
    ejemplo3()
    cur = mydb.cursor()
    cur.execute('INSERT INTO datos (email, password) VALUES ("{email}",  "{password}")'.format(
        email=email, password=password))
    cur.close()


def formDB():
    mydb = conectarDB()
    guardarDB(mydb)
