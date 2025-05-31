from notificadores.interface_notificador import INotificador

class EmailNotificador(INotificador):
    def notificar(self, mensagem):
        print(f"[Email] {mensagem}")