import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

# Cargar variables desde .env
load_dotenv()

remitente = os.getenv("FACTURAS_EMAIL_REMITENTE")
password = os.getenv("FACTURAS_EMAIL_PASSWORD")

destinatario = "asergiopdp94@gmail.com"

if not remitente or not password:
    raise ValueError("Faltan las variables FACTURAS_EMAIL_REMITENTE o FACTURAS_EMAIL_PASSWORD")

mensaje = EmailMessage()
mensaje["From"] = remitente
mensaje["To"] = destinatario
mensaje["Subject"] = "Prueba de envío desde Python"

mensaje.set_content("""
Hola Sergio,

Este es un correo de prueba enviado desde Python usando variables de entorno.

Si recibiste este mensaje, las credenciales funcionan correctamente.

Saludos.
""")

try:
    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.starttls()
        smtp.login(remitente, password)
        smtp.send_message(mensaje)

    print("Correo enviado correctamente.")

except smtplib.SMTPAuthenticationError:
    print("Error de autenticación. Revisa el correo o la contraseña de aplicación.")

except Exception as e:
    print(f"Error al enviar correo: {e}")

input()
