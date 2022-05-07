from flask import Flask, render_template, request, redirect, url_for, flash, Response, stream_with_context
from flaskext.mysql import MySQL
from decouple import config
import smtplib  
import json


app = Flask(__name__)


mysql = MySQL()
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = config('USER_DB')
app.config['MYSQL_DATABASE_PASSWORD'] = config('PASSWORD_DB')
app.config['MYSQL_DATABASE_DB'] = config('NAME_DB')
mysql.init_app(app)


def _datos(cur):
    cur.execute(
        'SELECT fecha_adquisicion, temp, temp_f FROM datos_tiempo_real WHERE id = (SELECT MAX(id) FROM datos_tiempo_real)')
    datos_tiempo_real = cur.fetchall()

    json_data = json.dumps(
        {'fecha': datos_tiempo_real[0][0], 'temp': datos_tiempo_real[0][1], 'temp_f': datos_tiempo_real[0][2]})

    yield f"data:{json_data}\n\n"
    if datos_tiempo_real[0][1] > 27:
        message = '#Advertencia! Posible incendio!#'
        subject='Advertencia!'
        message = 'Subject: {}\n\n{}'.format(subject, message)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login (config('NAME_MAIL'), config('PASSWORD_MAIL'))
        server.sendmail('Alerta.Temprana.Incendio@gmail.com', 'josequintanadf@unimagdalena.edu.co', message)
        server.quit()
        print("Correo enviado exitosamente!")




@app.route('/')
def index():
    return render_template('index.html')


@app.route('/acumulados')
def acumulados():
    cur = mysql.get_db().cursor()

    cur.execute(
        'SELECT fecha_adquisicion, temp, temp_f FROM datos_tiempo_real')
    valores = cur.fetchall()

    return render_template('acumulados.html', valores=valores)


@app.route('/datos_monitoreo')
def datos_monitoreo():
    cur = mysql.get_db().cursor()

    enviar = _datos(cur)

    return Response(stream_with_context(enviar), mimetype='text/event-stream')


if __name__ == '__main__':
    app.run(debug=True)
