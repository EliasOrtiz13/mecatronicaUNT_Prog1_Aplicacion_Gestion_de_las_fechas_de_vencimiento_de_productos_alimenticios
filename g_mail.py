import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class EnviarEmail():

    def notificar_estado_producto(self, destinatario, nombre, dia1, dia2, datos_productos):  
        
        # dirección desde dónde se envian los correos
        gmail_user = "estadodeproductos@gmail.com"
        password = "glqvyexbiaybvoxs" #contraseña generada que no varía
        mail_from = gmail_user

        #para quien va destinado
        mail_to = destinatario #Correo del destinatario
        asunto = "Productos próximos a vencerse dentro de {} a {} dias".format(dia1, dia2)
        
        mensaje = ''
        if len(datos_productos) != 0:
            txt = ''
            for i in range(len(datos_productos)):
                txt += '- {}, {}, {}, {}, vence el {} \n'.format(datos_productos[i][0], datos_productos[i][1], 
                datos_productos[i][2], datos_productos[i][3], datos_productos[i][5])

            mensaje = "Hola {}, los sigientes productos estan próximos a vencerse:\n {}".format(nombre, txt)
        else:
            mensaje = "Hola {}, no hay productos proximos a caducar dentro de 19 días".format(nombre)

        #proceso de login sobre el servidor
        mimemsg = MIMEMultipart()
        mimemsg['From']=mail_from
        mimemsg['To']=mail_to
        mimemsg['Subject']=asunto
        mimemsg.attach(MIMEText(mensaje, 'plain'))
        connection = smtplib.SMTP(host='smtp.gmail.com', port=587)
        connection.starttls()
        connection.login(gmail_user,password)
        connection.send_message(mimemsg)
        connection.quit()

if __name__ == '__main__':
    alarma = EnviarEmail()
    alarma.notificar_estado_producto()