from umqttsimple import MQTTClient
import network
import ujson
import time
import random


SSID = "Jose2001"
PASSWORD = "alogente"


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

    SERVER = "15.228.254.5"
    client = MQTTClient("test", SERVER)

    topic = "test"

    client.connect()

    while True:
        variables = {
            "fecha": str(time.localtime()),
            "numero1": random.random()*10,
            "numero2": random.random(),
        }
        payload = ujson.dumps(variables)
        print(payload)
        client.publish(topic, payload)
        time.sleep(1)

    client.disconnect()


if __name__ == "__main__":
    run()

