import smtplib
from decouple import config

message = '#Advertencia! Posible incendio!#'
subject='Advertencia!'

message = 'Subject: {}\n\n{}'.format(subject, message)

server = smtplib.SMTP('smtp.gmail.com', 587)

server.starttls()
server.login (config('NAME_MAIL'), config('PASSWORD_MAIL'))

server.sendmail('Alerta.Temprana.Incendio@gmail.com', 'josequintanadf@unimagdalena.edu.co', message)

server.quit()

print("Correo enviado exitosamente!")