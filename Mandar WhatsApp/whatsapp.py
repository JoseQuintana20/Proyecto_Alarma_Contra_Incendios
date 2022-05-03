# Importamos el ModuMódulo
import pywhatkit

# Usamos Un try-except
try:
  # Enviamos el mensaje
  pywhatkit.sendwhatmsg("+573122389016",  
                        "#Advertencia! Posible incendio!#",
                        15,6)
  print("Mensaje Enviado")
  
except:
  print("Ocurrio Un Error")