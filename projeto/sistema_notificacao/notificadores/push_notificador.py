from notificadores.interface_notificador import INotificador

class PushNotificador(INotificador):
    def notificar(self, mensagem):
        print(f"[Push Notification] {mensagem}")