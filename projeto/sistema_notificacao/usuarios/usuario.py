class Usuario:
    def __init__(self, nome, notificador):
        self.nome = nome
        self.notificador = notificador

    def receber_notificacao(self, mensagem):
        print(f"Usuário: {self.nome}")
        self.notificador.notificar(mensagem)
        print("-" * 30)