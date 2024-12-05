class Notificacion:
    def enviar(self, mensaje):
        pass

class Email(Notificacion):
    def enviar(self, mensaje):
        return f"Email enviado con el mensaje: {mensaje}"

class SMS(Notificacion):
    def enviar(self, mensaje):
        return f"SMS enviado con el mensaje: {mensaje}"

class Push(Notificacion):
    def enviar(self, mensaje):
        return f"Notificación push enviada con el mensaje: {mensaje}"

def enviar_notificaciones(notificaciones, mensaje):
    for notificacion in notificaciones:
        print(notificacion.enviar(mensaje))

if __name__ == "__main__":
    notificaciones = [Email(), SMS(), Push()]
    enviar_notificaciones(notificaciones, "Hola, esta es una notificación.")
