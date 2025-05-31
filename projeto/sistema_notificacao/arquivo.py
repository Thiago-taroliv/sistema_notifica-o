import json
import os

CAMINHO_ARQUIVO = "dados/usuarios.json"

def salvar_usuarios(usuarios):
    dados = []
    for usuario in usuarios:
        dados.append({
            "nome": usuario.nome,
            "notificador": type(usuario.notificador).__name__.replace("Notificador", "").lower()
        })
    os.makedirs(os.path.dirname(CAMINHO_ARQUIVO), exist_ok=True) 
    with open(CAMINHO_ARQUIVO, "w") as f:
        json.dump(dados, f, indent=4)

def carregar_usuarios():
    if not os.path.exists(CAMINHO_ARQUIVO):
        return []
    with open(CAMINHO_ARQUIVO, "r") as f:
        dados = json.load(f)

    from usuarios.usuario import Usuario
    from notificadores.email_notificador import EmailNotificador
    from notificadores.sms_notificador import SMSNotificador
    from notificadores.push_notificador import PushNotificador

    notificadores = {
        "email": EmailNotificador,
        "sms": SMSNotificador,
        "push": PushNotificador
    }

    usuarios = []
    for item in dados:
        nome = item["nome"]
        tipo = item["notificador"]
        notificador = notificadores[tipo]()
        usuarios.append(Usuario(nome, notificador))

    return usuarios
