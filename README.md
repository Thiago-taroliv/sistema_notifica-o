# 🔔 Sistema de Notificações

Este é um projeto em Python que simula um sistema de notificações para usuários.

## ✅ Funcionalidades

- Cadastrar novos usuários
- Escolher o tipo de notificação: **email**, **sms** ou **push**
- Notificar todos os usuários ao mesmo tempo
- Salvar os usuários em arquivo (mesmo depois de fechar o programa)

## 📁 Estrutura

- `main.py`: onde o sistema é executado
- `evento/`: contém a classe do evento que notifica os usuários
- `usuarios/`: contém a classe dos usuários
- `notificadores/`: diferentes formas de notificação (email, sms, push)
- `persistencia.py`: salva e carrega os usuários do arquivo JSON
- `dados/usuarios.json`: arquivo onde os dados são salvos

## 🧠 Padrão Usado

Usa o padrão **Observer** para que vários usuários sejam notificados ao mesmo tempo.

## 💾 Requisitos

- Python 3.7 ou superior
- Nenhuma biblioteca externa
