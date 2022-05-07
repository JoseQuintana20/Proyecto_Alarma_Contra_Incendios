from umqttsimple import MQTTClient
import network
import ujson
import time
import random
from machine import Pin
import dht

sensor = dht.DHT22(Pin(15))

SSID = "ISSA"
PASSWORD = "L4cand3lar1a"


def do_connect(SSID, PASSWORD):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    if not wlan.isconnected():
        print("connecting to network...")
        wlan.connect(SSID, PASSWORD)

        while not wlan.isconnected():
            pass
    print("network config:", wlan.ifconfig())


def run():
    do_connect(SSID, PASSWORD)

    SERVER = "54.207.92.242"
    client = MQTTClient("test", SERVER)

    topic = "test"

    client.connect()


    while True:
        sensor.measure()
        variables = {
            "fecha": str(time.localtime()),
            "temp": sensor.temperature(),
            #"temp_f": temp* (9/5)+ 32.0,
        }
        payload = ujson.dumps(variables)
        print(payload)
        client.publish(topic, payload)
        time.sleep(2)

    client.disconnect()


if __name__ == "__main__":
    run()
