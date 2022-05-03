import smtplib
from decouple import config
import pyautogui, webbrowser
from time import sleep

########################################################################################################
########################################### MENSAJE A EMAIL ############################################
########################################################################################################

message = '#Advertencia! Posible incendio!#'
subject='Advertencia!'

message = 'Subject: {}\n\n{}'.format(subject, message)

server = smtplib.SMTP('smtp.gmail.com', 587)

server.starttls()
server.login (config('NAME_MAIL'), config('PASSWORD_MAIL'))

server.sendmail('Alerta.Temprana.Incendio@gmail.com', 'josequintanadf@unimagdalena.edu.co', message)

server.quit()

print("Correo enviado exitosamente!")

########################################################################################################
########################################## MENSAJE A WHATSAPP ##########################################
########################################################################################################

webbrowser.open("https://web.whatsapp.com/send?phone=+573122389016")

sleep(10)

for i in range(10):
    pyautogui.typewrite('#Advertencia! Posible incendio!#')
    pyautogui.press('enter')