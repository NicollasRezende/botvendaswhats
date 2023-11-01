from flask import Flask, request
import requests
from config_bot import (VERIFY_TOKEN,
                        WHATSAPP_TOKEN,
                        BASE_URL,
                        PAGE_ID,
                        saudacoes_portugues)
from menssages import Menus, MenuOptions, codigo_aleatorio
from funcs import registrar_mensagem


app = Flask(__name__)


@app.route('/', methods=['GET'])
def verify_webhook():
    if request.args.get("hub.verify_token") == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return "Verificação falhou", 403


@app.route('/', methods=['POST'])
def receive_messages():
    data = request.get_json()

    numero_para_enviar = "5561991769500"
    numero_comercial = "5561991769500"
    detalhes = None
    palavra_chave = codigo_aleatorio
    text = None
    name = None
    numero_user = None
    messagess = []
    user_name = []
    nome = None
    wa_id = None
    button_reply_id = None
    list_reply_id = None
    menu_atual = None
    global opcao_menu
    global equipe
    global aguardando_resposta
    aguardando_resposta = False
    global mensagem_usuario
    mensagem_usuario = None

    try:

        for entry in data['entry']:
            for change in entry['changes']:
                if 'value' in change and 'contacts' in change['value']:
                    for contact in change['value']['contacts']:
                        if 'profile' in contact and 'name' in contact['profile']:
                            nome = contact['profile']['name']
                        if 'wa_id' in contact:
                            wa_id = contact['wa_id']

        for entry in data['entry']:
            for change in entry['changes']:
                if 'value' in change and 'messages' in change['value']:
                    for message in change['value']['messages']:
                        if 'interactive' in message and 'list_reply' in message['interactive']:
                            list_reply = message['interactive']['list_reply']
                            if list_reply['id']:
                                list_reply_id = list_reply['id']
                                break

        try:

            if list_reply_id == 'VOLTAR':
                opcao_menu = 'inicial'
                menu_atual = MenuOptions.INICIAL
                registrar_mensagem(numero_user, name, text, opcao_menu)
                Menus.menu_inicial(wa_id, nome)

            if list_reply_id == 'VOZ':
                opcao_menu = 'VOZ'
                Menus.menu_comercial_voz(wa_id, nome)
                registrar_mensagem(wa_id, nome, button_reply_id, opcao_menu)

            if list_reply_id == 'DADOS':
                opcao_menu = 'DADOS'
                Menus.menu_comercial_dados(wa_id, nome)
                registrar_mensagem(wa_id, nome, button_reply_id, opcao_menu)

            if list_reply_id == 'SEGURANCA':
                opcao_menu = 'SEGURANCA'
                Menus.menu_comercial_seguranca(wa_id, nome)
                registrar_mensagem(wa_id, nome, button_reply_id, opcao_menu)

            if list_reply_id == 'CABEAMENTO':
                opcao_menu = 'CABEAMENTO'
                Menus.menu_comercial_cabeamento(wa_id, nome)
                registrar_mensagem(wa_id, nome, button_reply_id, opcao_menu)

            if list_reply_id == 'LOCACAO':
                opcao_menu = 'LOCACAO'
                Menus.menu_comercial_locacao(wa_id, nome)
                registrar_mensagem(wa_id, nome, button_reply_id, opcao_menu)

# -------------------VOZ-------------------

            if list_reply_id == 'SIP_SERVER':
                opcao_menu = 'SIP SERVER'
                Menus.enviar_msg_SipServer(wa_id)
                Menus.enviar_msg_exemplo(wa_id)
                registrar_mensagem(wa_id, nome, button_reply_id, opcao_menu)

            if list_reply_id == 'GRAVADOR_CHAMADAS':
                opcao_menu = 'GRAVADOR CHAMADAS'
                Menus.enviar_msg_Gravador(wa_id)
                Menus.enviar_msg_exemplo(wa_id)
                registrar_mensagem(wa_id, nome, button_reply_id, opcao_menu)

            if list_reply_id == 'APARELHOS_IP':
                opcao_menu = 'APARELHOS IP'
                Menus.enviar_msg_AparelhoIP(wa_id)
                Menus.enviar_msg_exemplo(wa_id)
                registrar_mensagem(wa_id, nome, button_reply_id, opcao_menu)

            if list_reply_id == 'URA':
                opcao_menu = 'URA'
                Menus.enviar_msg_URA(wa_id)
                Menus.enviar_msg_exemplo(wa_id)
                registrar_mensagem(wa_id, nome, button_reply_id, opcao_menu)

            if list_reply_id == 'GATEWAYS':
                opcao_menu = 'GATEWAYS'
                Menus.enviar_msg_Gateways(wa_id)
                Menus.enviar_msg_exemplo(wa_id)
                registrar_mensagem(wa_id, nome, button_reply_id, opcao_menu)

            if list_reply_id == 'CORREIO_DE_VOZ':
                opcao_menu = 'CORREIO DE VOZ'
                Menus.enviar_msg_Correio_de_voz(wa_id)
                Menus.enviar_msg_exemplo(wa_id)
                registrar_mensagem(wa_id, nome, button_reply_id, opcao_menu)

            if list_reply_id == 'RELATORIOS':
                opcao_menu = 'RELATORIOS'
                Menus.enviar_msg_Relatorios(wa_id)
                Menus.enviar_msg_exemplo(wa_id)
                registrar_mensagem(wa_id, nome, button_reply_id, opcao_menu)

# -------------------DADOS-------------------

            if list_reply_id == 'VPN':
                opcao_menu = 'VPN'
                Menus.enviar_msg_VPN(wa_id)
                Menus.enviar_msg_exemplo(wa_id)
                registrar_mensagem(wa_id, nome, button_reply_id, opcao_menu)

            if list_reply_id == 'FIREWALL':
                opcao_menu = 'FIREWALL'
                Menus.enviar_msg_Firewall(wa_id)
                Menus.enviar_msg_exemplo(wa_id)
                registrar_mensagem(wa_id, nome, button_reply_id, opcao_menu)

            if list_reply_id == 'VIRTUALIZACAO':
                opcao_menu = 'Virtualização'
                Menus.enviar_msg_Virtualizacao(wa_id)
                Menus.enviar_msg_exemplo(wa_id)
                registrar_mensagem(wa_id, nome, button_reply_id, opcao_menu)

# -------------------SEGURANCA-------------------

            if list_reply_id == 'CFTV':
                opcao_menu = 'CFTV'
                Menus.enviar_msg_CFTV(wa_id)
                Menus.enviar_msg_exemplo(wa_id)
                registrar_mensagem(wa_id, nome, button_reply_id, opcao_menu)

            if list_reply_id == 'CERCA_ELETRICA':
                opcao_menu = 'CERCA ELETRICA'
                Menus.enviar_msg_Central_de_Cerca_Eletrica(wa_id)
                Menus.enviar_msg_exemplo(wa_id)
                registrar_mensagem(wa_id, nome, button_reply_id, opcao_menu)

            if list_reply_id == 'ALARME':
                opcao_menu = 'ALARME'
                Menus.enviar_msg_Central_de_Alarme(wa_id)
                Menus.enviar_msg_exemplo(wa_id)
                registrar_mensagem(wa_id, nome, button_reply_id, opcao_menu)

# -------------------CABEAMENTO-------------------

            if list_reply_id == 'INFO':
                opcao_menu = 'INFO'
                Menus.enviar_contato(wa_id, "Comercial", numero_comercial)
                Menus.enviar_link(wa_id, "https://teletronweb.com.br/")
                registrar_mensagem(wa_id, nome, button_reply_id, opcao_menu)

            print("_________________________________________")
            print("Recebido POST das Opçoes:")
            print("USUARIO SELECIONOU", list_reply_id)
            print("NOME:", nome)
            print("NUMERO:", wa_id)
            print("_________________________________________")
        except UnboundLocalError:
            pass

    except ValueError:
        pass

    try:

        for entry in data['entry']:
            for change in entry['changes']:
                if 'value' in change and 'contacts' in change['value']:
                    for contact in change['value']['contacts']:
                        if 'profile' in contact and 'name' in contact['profile']:
                            nome = contact['profile']['name']
                        if 'wa_id' in contact:
                            wa_id = contact['wa_id']

        for entry in data['entry']:
            for change in entry['changes']:
                if 'value' in change and 'messages' in change['value']:
                    for message in change['value']['messages']:
                        if 'interactive' in message and 'button_reply' in message['interactive']:
                            button_reply = message['interactive']['button_reply']
                            if button_reply['id']:
                                button_reply_id = button_reply['id']
                                break

        # VOLTAR

        if button_reply_id == 'contato':
            opcao_menu = 'contato'
            Menus.enviar_contato(wa_id, "Comercial", numero_comercial)
            Menus.enviar_link(wa_id, "https://teletronweb.com.br/")

        if button_reply_id == 'voltar':
            opcao_menu = 'inicial'
            menu_atual = MenuOptions.INICIAL
            registrar_mensagem(numero_user, name, text, opcao_menu)
            Menus.menu_inicial(wa_id, nome)

        # SUPORTE TECNICO

        if button_reply_id == 'SUPORTE_TECNICO':
            equipe = 'Suporte'
            opcao_menu = 'suporte1'
            Menus.menu_supote_tecnico(wa_id, nome)
            registrar_mensagem(wa_id, nome, button_reply_id, opcao_menu)

        if button_reply_id == 'SIM':
            opcao_menu = 'suporte3'
            Menus.enviar_msg_menu_suporte(wa_id)
            Menus.enviar_msg_menu_suporte2(wa_id)
            Menus.menu_voltar_suporte(wa_id, name)
            registrar_mensagem(wa_id, nome, list_reply_id, opcao_menu)
            menu_atual = MenuOptions.SUPORTE4

        if button_reply_id == 'NAO':
            opcao_menu = 'suporte4'
            Menus.menu_suporte_opcoes2(wa_id, nome)
            Menus.menu_inicial(wa_id, nome)
            registrar_mensagem(wa_id, nome, button_reply_id, opcao_menu)

        # FINANCEIRO

        if button_reply_id == 'FINANCEIRO':
            equipe = 'Financeiro'
            opcao_menu = 'financeiro'
            Menus.menu_voltar(wa_id, nome)
            Menus.menu_financeiro2(wa_id, nome)
            registrar_mensagem(wa_id, nome, button_reply_id, opcao_menu)

        # COMERCIAL

        if button_reply_id == 'COMERCIAL':
            equipe = 'Comercial'
            opcao_menu = 'comercial'
            Menus.menu_comercial(wa_id, nome)
            registrar_mensagem(wa_id, nome, button_reply_id, opcao_menu)

# -------------------LOCACAO-------------------

        if button_reply_id == 'LOCACAO2':
            opcao_menu = 'Locação'
            Menus.enviar_msg_Locação_de_equipamentos(wa_id)
            Menus.enviar_msg_exemplo(wa_id)
            registrar_mensagem(wa_id, nome, button_reply_id, opcao_menu)

# -------------------CABEAMENTO-------------------

        if button_reply_id == 'CABEAMENTO':
            opcao_menu = 'Cabeamento'
            Menus.enviar_msg_Cabeamento_estruturado(wa_id)
            Menus.enviar_msg_exemplo(wa_id)
            registrar_mensagem(wa_id, nome, button_reply_id, opcao_menu)

        print("_________________________________________")
        print("Recebido POST das Opçoes:")
        print("USUARIO SELECIONOU", button_reply_id)
        print("NOME:", nome)
        print("NUMERO:", wa_id)
        print("_________________________________________")

    except ValueError:
        pass

    try:
        messagess = data['entry'][0]['changes'][0]['value']['messages']
        user_name = data['entry'][0]['changes'][0]['value']['contacts']

        for user in user_name:
            name = user['profile']['name']

        for messaging in messagess:
            text = messaging['text']['body']
            numero_user = messaging['from']

            if text in saudacoes_portugues:
                text = text
                numero_user = numero_user
                opcao_menu = 'inicial'
                menu_atual = MenuOptions.INICIAL
                registrar_mensagem(numero_user, name, text, opcao_menu)

            if text:
                registrar_mensagem(numero_user, name, text, opcao_menu)

            if palavra_chave in text:
                detalhes = text
                enviar_msg(numero_para_enviar, f"\nO cliente: {name}\n\nnumero: {numero_user}\n\nEsta requisitando {opcao_menu}\n\naqui estao os detalhes:\n\n {detalhes}\n\n")
                Menus.enviar_contato(numero_para_enviar, name, numero_user)
                enviar_msg(numero_user, f"Solicitaçao enviada para a equipe do {equipe}, aguarde o contato da nossa equipe, se precisar de mais alguma coisa pode contar com a gente")
                menu_atual = MenuOptions.INICIAL


        print("_________________________________________")
        print("Recebido POST do Usuario:")
        print("USUARIO DIGITOU", text)
        print("NOME':", name)
        print("NUMERO", numero_user)
        print("_________________________________________")

    except (KeyError):
        pass

    try:
        if menu_atual == MenuOptions.INICIAL:
            Menus.menu_inicial(numero_user, name)
    except UnboundLocalError:
        pass
    except requests.exceptions.RequestException as e:
        print(f"Erro ao enviar mensagem: {e}")

    return "OK"


def enviar_msg(numero, mensagem):

    url = f"{BASE_URL}/{PAGE_ID}/messages"

    headers = {
        "Authorization": f"Bearer {WHATSAPP_TOKEN}",
        "Content-Type": "application/json"
    }

    data = {
        "messaging_product": "whatsapp",
        "to": numero,
        "type": "text",
        "text": {"body": mensagem}
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        return response
    except requests.exceptions.RequestException as e:
        print(f"Erro ao enviar mensagem: {e}")


if __name__ == '__main__':
    app.run(debug=True, port=5000)
