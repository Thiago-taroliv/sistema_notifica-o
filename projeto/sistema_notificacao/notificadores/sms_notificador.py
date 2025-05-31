from notificadores.interface_notificador import INotificador

class SMSNotificador(INotificador):
    def notificar(self, mensagem):
        print(f"[SMS] {mensagem}")