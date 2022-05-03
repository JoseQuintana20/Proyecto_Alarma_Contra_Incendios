# Write your code here :-)
from machine import Pin, PWM
from time import sleep
import network
from hcsr04 import HCSR04
# Libreria Mqtt
from umqttsimple import MQTTClient


# Sensor ultrasonico
# wire Orange, pin 15
echo = 15
# wire Brown, pin 2
tigger = 2

# Declarar parametros del sensor
sensor = HCSR04(trigger_pin=tigger, echo_pin=echo, echo_timeout_us=1000000)

# Connect to internet
def do_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('CLARO_WIFI5E0', 'CLAROI5E0')
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())
    # Para desconectar del wifi
    # wlan.disconnect()

# Pines de control del puente H
in1 = Pin(33, Pin.OUT)
in2 = Pin(25, Pin.OUT)
in3 = Pin(26, Pin.OUT)
in4 = Pin(27, Pin.OUT)

# Giro de los motores
in1.off()
in2.on()
in3.on()
in4.off()

# Connect to internet
do_connect()

# Mqtt process
########################################
SERVER = "broker.emqx.io"
client = MQTTClient("esp3201", SERVER)
topic = "esp3201"
try:
    client.connect()
    print("conexión mqtt exitosa!\n")
except:
    print("Error en conexión mqtt\n")
########################################

# data vector
# Un segundo por cada dato
segundos = 1
datos = []

setpoint = 7

while True:
    # Canal A bomba del recipiente azul
    # PWM_max = 400 y PWM_min = 200 Nota: cuando hay agua
    # Canal B bomba del recipiente rojo
    # PWM_max = 350 y PWM_min = 250 Nota: cuando hay agua
    # PWM.duty --> (0-1023)

    # Obtener distancia actual
    distance = sensor.distance_cm()

    # Control de sistema
    # Bomba que ingresa agua
    
    
    if distance < setpoint:
        # Bomba que ingresa agua
        PWMA = PWM(Pin(32))
        PWMA.duty(0)
        # Bomba que saca agua
        PWMB = PWM(Pin(14))
        PWMB.duty(340)
    else:
        # Bomba que ingresa agua
        PWMA = PWM(Pin(32))
        PWMA.duty(390)
        # Bomba que saca agua
        PWMB = PWM(Pin(14))
        PWMB.duty(0)
    

    # Almacenamiento y envio de datos
    if len(datos) < segundos:
        # Almacenar los datos
        print('Distance:', distance, 'cm')
        datos.append(distance)
    else:
        # print(datos)
        # Enviar los datos
        client.publish(topic, str(datos))
        """
        for i in datos:
            client.publish(topic, str(i))
        """
        datos = []
        print("Enviados!!")

    # Secs
    sleep(1)