import paho.mqtt.client as mqtt
import json
import subprocess
from guardar_mqtt_db import cargarDB
from decouple import config
import smtplib 

def email():
    message = '#Advertencia! Posible incendio!#'
    subject='Advertencia!'
    message = 'Subject: {}\n\n{}'.format(subject, message)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login (config('NAME_MAIL'), config('PASSWORD_MAIL'))
    server.sendmail('Alerta.Temprana.Incendio@gmail.com', 'josequintanadf@unimagdalena.edu.co', message)
    server.quit()
    print("Correo enviado exitosamente!")


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    client.subscribe("test")


def on_message(client, userdata, msg):
    valores_json = str(msg.payload, 'utf-8')
    valores = json.loads(valores_json)
    cargarDB(valores)
    print(valores)
    if datos_tiempo_real[0][1] > 27:
        email()
        

def run():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect("localhost", 1883)
    client.loop_forever()


if __name__ == '__main__':
    run()
