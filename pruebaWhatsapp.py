import pywhatkit as kit
import time

def enviar_whatsapp():
    # Utilizo un diccionario en el que el par clave/valor son el numero de telefono y el mensaje respectivamente
    mensajes = {}

    print("Bienvenido a la herramienta de envío de mensajes por WhatsApp")
    print("Introduce el número de teléfono y el mensaje que quieras enviar")
    print("Puedes hacerlo cuantas veces quieras, añade 'fin' como número para terminar")

    while True:
        numero = input('Introduce el número de teléfono (con +34 o el prefijo internacional): ')
        if numero.lower() == 'fin':
            break
        mensaje = input('Introduce el mensaje que quieres enviar: ')
        mensajes[numero] = mensaje  # Se añade el mensaje y el número al diccionario

    print("Enviando mensajes...")

    for numero, mensaje in mensajes.items():
        try:
            kit.sendwhatmsg_instantly(
                phone_no=numero,
                message=mensaje,
                wait_time=10,
                tab_close=True,
                close_time=3
            )  # Enviar mensaje
            time.sleep(10)  # Esperar 10 segundos entre mensajes, esto se puede cambiar.

        except Exception as e:
            print("Error al enviar el mensaje a", numero, ":", e)

# Llamada a la función
enviar_whatsapp()



