# forma de enviar correos desde python
from email.mime.text import MIMEText
# MIME = Multi-Purpose Internet Mail Extensions
from email.mime.multipart import MIMEMultipart
import smtplib
mensaje = MIMEMultipart()
password = 'Pruebas2020' # contraseña del correo
mensaje['From'] = 'testappseduardo@gmail.com' # cliente del correo
mensaje['Subject'] = 'Registro completado!' # Titulo del correo

def enviarCorreo(para, nombre):
    print(para)
    print(nombre)
    mensaje['To'] = para # el correo a quien quiero enviar el correo
    cuerpo = 'Hola! {} \n Gracias por comunicarte conmigo, nos pondremos en contacto pronto! 😁'.format(nombre)
    mensaje.attach(MIMEText(cuerpo,'plain')) # ahora, adjunto toda la configuracion del correo con el cuerpo del mensaje a enviar y le indico en que formato se mandara
    try:
        servidorSMTP = smtplib.SMTP('smtp.gmail.com', 587) # configuro mi servidor smtp (que va a ser el encargado de conectarse con los servidores de outlook)
        servidorSMTP.starttls() # indico que el metodo de cifrado del envio de los correo sea starttls
        servidorSMTP.login(mensaje['From'], password) # me logeo
        servidorSMTP.sendmail(
            mensaje['From'], 
            mensaje['To'],  
            mensaje.as_string()) # envio el correo con toda la configuracion del mensaje previamente realizada
        servidorSMTP.quit() # me desconecto porque sino la proxima vez que vuelva a hacer login puede generar conflictos de autenticacion
        return True
    except Exception as e:
        print(e)
        return False


