from evento.evento_importante import EventoImportante
from notificadores.email_notificador import EmailNotificador
from notificadores.sms_notificador import SMSNotificador
from notificadores.push_notificador import PushNotificador
from usuarios.usuario import Usuario
from arquivo import salvar_usuarios, carregar_usuarios

opcoes_notificacao = {
    "email": EmailNotificador,
    "sms": SMSNotificador,
    "push": PushNotificador
}

evento = EventoImportante()
usuarios_carregados = carregar_usuarios()
for u in usuarios_carregados:
    evento.registrar_usuario(u)

print("=== Sistema de Notificações ===")
while True:
    print("1. Cadastrar novo usuário")
    print("2. Enviar notificação a todos")
    print("3. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do usuário: ")
        tipo = input("Tipo de notificação (email, sms, push): ").lower()
        if tipo in opcoes_notificacao:
            usuario = Usuario(nome, opcoes_notificacao[tipo]())
            evento.registrar_usuario(usuario)
            salvar_usuarios(evento.usuarios)
            print("Usuário cadastrado com sucesso!\n")
        else:
            print("Tipo de notificação inválido!\n")

    elif opcao == "2":
        evento.notificar_todos("Um novo evento importante ocorreu!")

    elif opcao == "3":
        print("Saindo...")
        break

    else:
        print("Opção inválida!\n")
