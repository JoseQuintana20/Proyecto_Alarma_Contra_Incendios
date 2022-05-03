import threading
import time
# Tarea a ejecutarse cada determinado tiempo.
def timer():
    while True:
        print("¡Hola, mundo!")
        time.sleep(3)   # 3 segundos.
# Iniciar la ejecución en segundo plano.
t = threading.Thread(target=timer)
t.start()