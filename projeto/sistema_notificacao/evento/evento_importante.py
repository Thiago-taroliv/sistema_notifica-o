class EventoImportante:
    def __init__(self):
        self.usuarios = []

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def notificar_todos(self, mensagem):
        for usuario in self.usuarios:
            usuario.receber_notificacao(mensagem)