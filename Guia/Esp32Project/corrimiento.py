import mysql.connector
from time import sleep

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

vectortotal = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,  0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,  0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,  0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,  0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,  0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
l = len(vectortotal)
# Iniciar proceso Mqtt
def run():
    while(True):
        sleep(1)
        # Almacenar en la Base de datos
        cur = mydb.cursor()
        cur.execute('DELETE FROM grafica')
        cur.execute('SELECT Distancia FROM Datos')
        vector = cur.fetchall()
        for i in range(l):
            if l-i-1 > 0:
                vectortotal[l-i-1] = vectortotal[l-i-2]
            else:
                aux = vector[0][0]
                aux = aux.replace("b","").replace("'","").replace("[","").replace("]","")
                vectortotal[0] = float(aux)

        for dato in vectortotal:
            cur = mydb.cursor()
            cur.execute('INSERT INTO grafica (actual) VALUES ({num})'.format(num=dato))
                
        #print(vectortotal) 


if __name__ == '__main__':
    run()