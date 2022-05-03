# Este codigo se encarga de guardar los datos en la base de datos
# Esta atendo a la actividad en el topico y una ves hay un dato 
# actualiza la tabla

from paho.mqtt import client as mqtt_client
from decouple import config
import mysql.connector
from time import sleep

broker = "broker.emqx.io"
port = 1883
topic = "esp3201"
# generate client ID with pub prefix randomly
client_id = "WEB"
# username = 'emqx'
# password = 'public'


def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

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

datos = ""
def on_message(client, userdata, msg):
    print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
    datos = str(msg.payload)
    # Almacenar en la Base de datos
    cur = mydb.cursor()
    cur.execute('DELETE FROM Datos')
    ejec = 'INSERT INTO Datos (Distancia) VALUES ("'+datos+'");'
    cur.execute(ejec)
        

# Iniciar proceso Mqtt
def run():
    client = connect_mqtt()
    client.subscribe(topic)
    client.on_message = on_message
    client.loop_forever()

if __name__ == '__main__':
    run()