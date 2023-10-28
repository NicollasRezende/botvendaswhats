from config_bot import BASE_URL, PAGE_ID, WHATSAPP_TOKEN
import requests
from enum import Enum


class MenuOptions(Enum):
    INICIAL = 'inicial'
    FINANCEIRO = 'financeiro'
    SUPORTE1 = 'suporte1'
    SUPORTE2 = 'suporte2'
    SUPORTE3 = 'suporte3'
    SUPORTE4 = 'suporte4'
    OUTROS = 'OUTROS'
    COMERCIAL = 'comercial'
    PRIVACIDADE = 'privacidade'
    ADM = 'administracao'
    VOLTAR = "voltar"


class Menus():

    menu_escolhid = None

    # privacidade

    def menu_privacidade(numero):


        url = f"{BASE_URL}/{PAGE_ID}/messages"

        headers = {
            "Authorization": f"Bearer {WHATSAPP_TOKEN}",
            "Content-Type": "application/json"
        }

        menu = ("*MENU INICIAL*"
                "\n"
                "\n*TELETRON INDUSTRIA E COMERCIO LTDA.*\n\nOlá! seja Bem-vindo a Teletron, antes de começar sua interaçao gostariamos que voce desse uma lida na nossa politica de privacidade:"
                "\n"
                "\nLink: "
                "\n"
                "\nSe voce concorda com nossos termos por favor selecione aceito, caso contrario selecione Nao aceito"
                "\n"
                "\nLembre-se que aceitar os termos vai deixar sua experiencia melhor e mais customizada"
                "\n")

        data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": numero,
            "type": "interactive",
            "interactive": {
                "type": "button",
                "body": {"text": menu},
                "action": {
                    "buttons": [{'type': "reply",
                                 'reply': {"id": "ACEITOU",
                                           "title": "EU CONCORDO"}},
                                {'type': "reply",
                                 'reply': {"id": "NEGOU",
                                           "title": "EU NAO CONCORDO"}},
                                ]}}
        }

        try:
            response = requests.post(url, headers=headers, json=data)
            return response
        except requests.exceptions.RequestException as e:
            print(f"Erro ao enviar mensagem: {e}")

    # inicial

    def menu_inicial(numero, nome):


        url = f"{BASE_URL}/{PAGE_ID}/messages"

        headers = {
            "Authorization": f"Bearer {WHATSAPP_TOKEN}",
            "Content-Type": "application/json"
        }

        menu = ("*MENU INICIAL*"
                "\n"
                "\n*TELETRON INDUSTRIA E COMERCIO LTDA.*\n\nOlá! seja Bem-vindo a Teletron, Para acessar qualquer um dos menus abaixo apenas escolha a opção desejada"
                "\n")

        data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": numero,
            "type": "interactive",
            "interactive": {
                "type": "button",
                "body": {"text": menu},
                "action": {
                    "buttons": [{'type': "reply",
                                 'reply': {"id": "SUPORTE_TECNICO",
                                           "title": "SUPORTE TECNICO"}},
                                {'type': "reply",
                                 'reply': {"id": "FINANCEIRO",
                                           "title": "FINANCEIRO"}},
                                {'type': "reply",
                                 'reply': {"id": "COMERCIAL",
                                           "title": "COMERCIAL"}},
                                ]}}
        }

        try:
            response = requests.post(url, headers=headers, json=data)
            return response
        except requests.exceptions.RequestException as e:
            print(f"Erro ao enviar mensagem: {e}")

    def menu_voltar(numero, nome):

        url = f"{BASE_URL}/{PAGE_ID}/messages"

        headers = {
            "Authorization": f"Bearer {WHATSAPP_TOKEN}",
            "Content-Type": "application/json"
        }

        menu = (
                "\n"
                "\nAperte o botao *VOLTAR* para voltar ao *MENU INICIAL*"
                "\n")

        data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": numero,
            "type": "interactive",
            "interactive": {
                "type": "button",
                "body": {"text": menu},
                "action": {
                    "buttons": [{'type': "reply",
                                 'reply': {"id": "voltar",
                                           "title": "VOLTAR"}},
                                ]}}
        }

        try:
            response = requests.post(url, headers=headers, json=data)
            return response
        except requests.exceptions.RequestException as e:
            print(f"Erro ao enviar mensagem: {e}")

    def menu_voltar_suporte(numero, nome):

        url = f"{BASE_URL}/{PAGE_ID}/messages"

        headers = {
            "Authorization": f"Bearer {WHATSAPP_TOKEN}",
            "Content-Type": "application/json"
        }

        menu = (
                "\n"
                "\nPara voltar ao Menu inicial ou entrar em contato por favor aperte em um dos botos abaixo"
                "\n")

        data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": numero,
            "type": "interactive",
            "interactive": {
                "type": "button",
                "body": {"text": menu},
                "action": {
                    "buttons": [{'type': "reply",
                                 'reply': {"id": "contato",
                                           "title": "CONTATO"}},

                                {'type': "reply",
                                 'reply': {"id": "voltar",
                                           "title": "VOLTAR"}},
                                ]}}
        }

        try:
            response = requests.post(url, headers=headers, json=data)
            return response
        except requests.exceptions.RequestException as e:
            print(f"Erro ao enviar mensagem: {e}")

    # financeiro

    def menu_financeiro(numero, nome):

        url = f"{BASE_URL}/{PAGE_ID}/messages"

        headers = {
            "Authorization": f"Bearer {WHATSAPP_TOKEN}",
            "Content-Type": "application/json"
        }

        menu = ("*FINANCEIRO*"
                "\n"
                "\n*BEM VINDO AO FINANCEIRO ESCOLHA UMA DAS OPÇOES ABAIXO*"
                "\n")

        data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": numero,
            "type": "interactive",
            "interactive": {
                "type": "button",
                "body": {"text": menu},
                "action": {
                    "buttons": [{'type': "reply",
                                 'reply': {"id": "OPÇAO_1_FINANCEIRO",
                                           "title": "OPÇAO 1 FINANCEIRO"}},
                                {'type': "reply",
                                 'reply': {"id": "OPÇAO_2_FINANCEIRO",
                                           "title": "OPÇAO 2 FINANCEIRO"}},
                                {'type': "reply",
                                 'reply': {"id": "OPÇAO_3_FINANCEIRO",
                                           "title": "OPÇAO 3 FINANCEIRO"}},
                                ]}}
        }

        try:
            response = requests.post(url, headers=headers, json=data)
            return response
        except requests.exceptions.RequestException as e:
            print(f"Erro ao enviar mensagem: {e}")

    # suporte tecnico

    def menu_supote_tecnico(numero, nome):

        url = f"{BASE_URL}/{PAGE_ID}/messages"

        headers = {
            "Authorization": f"Bearer {WHATSAPP_TOKEN}",
            "Content-Type": "application/json"
        }

        menu = ("*SUPORTE*"
                "\n"
                "\n*PARA SUPORTE PEDIMOS QUE CONFIRME SE JA TEM CONTRATO COM A GENTE*"
                "\n")

        data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": numero,
            "type": "interactive",
            "interactive": {
                "type": "button",
                "body": {"text": menu},
                "action": {
                    "buttons": [{'type': "reply",
                                 'reply': {"id": "SIM",
                                           "title": "SIM"}},
                                {'type': "reply",
                                 'reply': {"id": "NAO",
                                           "title": "NAO"}},
                                {'type': "reply",
                                 'reply': {"id": "voltar",
                                           "title": "VOLTAR"}},
                                ]}}
        }

        try:
            response = requests.post(url, headers=headers, json=data)
            return response
        except requests.exceptions.RequestException as e:
            print(f"Erro ao enviar mensagem: {e}")

    def menu_suporte_opcoes(numero, nome):

        url = f"{BASE_URL}/{PAGE_ID}/messages"

        headers = {
            "Authorization": f"Bearer {WHATSAPP_TOKEN}",
            "Content-Type": "application/json"
        }

        data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": numero,
            "type": "interactive",
            "interactive": {
                "type": "list",
                "header": {
                    "type": "text",
                    "text": "SELECIONE UMA DAS OPÇOES DE SUPORTE ABAIXO"
                },
                "body": {
                    "text": "OPÇOES DE SUPORTE TECNICO"
                },
                "footer": {
                    "text": "OPÇOES DE SUPORTE"
                },
                "action": {
                    "button": "Clique aqui",
                    "sections": [{
                        "title": "Opções de suporte",
                        "rows": [
                            {"id": "row1_suporte", "title": "SUPORTE 1"},
                            {"id": "row2_suporte", "title": "SUPORTE 2"},
                            {"id": "row3_suporte", "title": "SUPORTE 3"},
                            {"id": "outros_suporte", "title": "OUTROS"},
                            {"id": "VOLTAR", "title": "Voltar ao menu principal"}
                        ]
                    }]
                }
            }
        }

        try:
            response = requests.post(url, headers=headers, json=data)
            return response
        except requests.exceptions.RequestException as e:
            print(f"Erro ao enviar mensagem: {e}")

    def menu_suporte_opcoes2(numero, nome):

        url = f"{BASE_URL}/{PAGE_ID}/messages"

        headers = {
            "Authorization": f"Bearer {WHATSAPP_TOKEN}",
            "Content-Type": "application/json"
        }

        mensagem = ("*SUPORTE*"
                    "\n"
                    "\nINFELIZMENTE A OPÇAO DE SUPORTE NAO ESTA DISPONIVEL PARA VOCE JA QUE VOCE NAO E UM DE NOSSOS CLIENTE POR FAVOR VA AO MENU COMERCIAL PARA COMEÇAR A USAR NOSSOS SERVIÇOS"
                    "\n")

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

    def menu_suporte_outros(numero, nome, msg, menu):

        url = f"{BASE_URL}/{PAGE_ID}/messages"

        headers = {
            "Authorization": f"Bearer {WHATSAPP_TOKEN}",
            "Content-Type": "application/json"
        }

        mensagem = ("*SUPORTE*"
                    "\n"
                    f"\nOLA, sua menssagem foi: {msg} \nseu numero e: {numero}, voce esta no menu: {menu}"
                    "\n")

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

    def enviar_msg_menu_suporte2(numero):

        url = f"{BASE_URL}/{PAGE_ID}/messages"

        headers = {
            "Authorization": f"Bearer {WHATSAPP_TOKEN}",
            "Content-Type": "application/json"
        }

        mensagem = (
                    "\n"
                    "\n\n*FORMULARIO*:"
                    "\n\nNUMERO do formulario: 55374"
                    "\n\n*Nome*:"
                    "\n"
                    "\n*Detalhamento do Problema ou da Solicitação de Suporte*:")

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

    def enviar_msg_menu_suporte(numero):

        url = f"{BASE_URL}/{PAGE_ID}/messages"

        headers = {
            "Authorization": f"Bearer {WHATSAPP_TOKEN}",
            "Content-Type": "application/json"
        }

        mensagem = ("*SUPORTE*"
                    "\n"
                    "\nPor favor envie uma mensagem detalhando seu problema:"
                    "\n"
                    "\nPara descrever o problema, copie e preencha o formulário a seguir:"
                    "\n\n*FORMULARIO*:"
                    "\n(*COPIE O NUMERO DO FORMULARIO E NAO ALTERE*)"
                    "\n\nNUMERO do formulario 55374"
                    "\n\n*Nome*: [Seu Nome]"
                    "\n"
                    "\n*Detalhamento do Problema ou da Solicitação de Suporte*:"
                    "\n[Descreva o problema ou solicitação de suporte de forma detalhada e clara. Inclua informações relevantes, como mensagens de erro, datas e horários em que o problema ocorreu, etc.]")

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

    # comercial

    def menu_comercial(numero, nome):

        url = f"{BASE_URL}/{PAGE_ID}/messages"

        headers = {
            "Authorization": f"Bearer {WHATSAPP_TOKEN}",
            "Content-Type": "application/json"
        }

        data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": numero,
            "type": "interactive",
            "interactive": {
                "type": "list",
                "header": {
                    "type": "text",
                    "text": "MENU COMERCIAL"
                },
                "body": {
                    "text": "*O que podemos oferecer*:\n\n*Voz*\n\n    Sip Server\n    Gravador de Chamadas\n    Aparelhos IP\n    URA\n    Gateways\n    Correio de Voz\n    Relatórios\n\n*Dados*\n\n    VPN\n    Firewall\n    Virtualização\n\n*Segurança*\n\n    CFTV\n    Central de Cerca Elética\n    Central de Alarme\n\n*Cabeamento*\n\n    Cabeamento Estruturado\n\n*Locação*\n\n    Locação de Equipamentos"
                },
                "footer": {
                    "text": "Opções de serviço abaixo:"
                },
                "action": {
                    "button": "Clique aqui",
                    "sections": [{
                        "title": "Opções de serviço",
                        "rows": [
                            {"id": "VOZ", "title": "VOZ"},
                            {"id": "DADOS", "title": "DADOS"},
                            {"id": "SEGURANCA", "title": "SEGURANÇA"},
                            {"id": "CABEAMENTO", "title": "CABEAMENTO"},
                            {"id": "LOCACAO", "title": "LOCACAO"},
                            {"id": "INFO", "title": "Contato/Info"},
                            {"id": "VOLTAR", "title": "Voltar ao menu principal"}
                        ]
                    }]
                }
            }
        }

        try:
            response = requests.post(url, headers=headers, json=data)
            return response
        except requests.exceptions.RequestException as e:
            print(f"Erro ao enviar mensagem: {e}")

    def menu_comercial_voz(numero, nome):

        url = f"{BASE_URL}/{PAGE_ID}/messages"

        headers = {
            "Authorization": f"Bearer {WHATSAPP_TOKEN}",
            "Content-Type": "application/json"
        }

        data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": numero,
            "type": "interactive",
            "interactive": {
                "type": "list",
                "header": {
                    "type": "text",
                    "text": "MENU COMERCIAL"
                },
                "body": {
                    "text": "*O que podemos oferecer*:\n\n*Voz*\n\nSip Server - Serviço de servidor de voz SIP\n\nGravador de Chamadas - Serviço de gravação de chamadas\n\nAparelhos IP - Serviço de telefonia com aparelhos IP\n\nURA - Atendimento automático de voz\n\nGateways - Serviço de integração de rede\n\nCorreio de Voz - Serviço de caixa de correio de voz\n\nRelatórios - Geração de relatórios de chamadas"
                },
                "footer": {
                    "text": "Opções de serviço de voz abaixo:"
                },
                "action": {
                    "button": "Clique aqui",
                    "sections": [{
                        "title": "Opções de serviço",
                        "rows": [
                            {"id": "SIP_SERVER", "title": "Sip Server"},
                            {"id": "GRAVADOR_CHAMADAS", "title": "Gravador de Chamadas"},
                            {"id": "APARELHOS_IP", "title": "Aparelhos IP"},
                            {"id": "URA", "title": "URA"},
                            {"id": "GATEWAYS", "title": "Gateways"},
                            {"id": "CORREIO_DE_VOZ", "title": "Correio de Voz"},
                            {"id": "RELATORIOS", "title": "Relatórios"},
                            {"id": "VOLTAR", "title": "Voltar ao menu principal"}
                        ]
                    }]
                }
            }
        }

        try:
            response = requests.post(url, headers=headers, json=data)
            return response
        except requests.exceptions.RequestException as e:
            print(f"Erro ao enviar mensagem: {e}")

    def menu_comercial_seguranca(numero, nome):

        url = f"{BASE_URL}/{PAGE_ID}/messages"

        headers = {
            "Authorization": f"Bearer {WHATSAPP_TOKEN}",
            "Content-Type": "application/json"
        }

        data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": numero,
            "type": "interactive",
            "interactive": {
                "type": "list",
                "header": {
                    "type": "text",
                    "text": "SEGURANÇA"
                },
                "body": {
                    "text": "*O que podemos oferecer*:\n\n*SEGURANÇA*\n\nCFTV - Serviço de Circuito Fechado de TV\n\nCentral de Cerca Elétrica - Serviço de Cerca Elétrica\n\nCentral de Alarme - Serviço de Alarme de Segurança"
                },
                "footer": {
                    "text": "Opções de serviço abaixo:"
                },
                "action": {
                    "button": "Clique aqui",
                    "sections": [{
                        "title": "Opções de serviço",
                        "rows": [
                            {"id": "CFTV", "title": "CFTV"},
                            {"id": "CERCA_ELETRICA", "title": "Cerca Elétrica"},
                            {"id": "ALARME", "title": "Central de Alarme"},
                            {"id": "VOLTAR", "title": "Voltar ao menu principal"}
                        ]
                    }]
                }
            }
        }

        try:
            response = requests.post(url, headers=headers, json=data)
            return response
        except requests.exceptions.RequestException as e:
            print(f"Erro ao enviar mensagem: {e}")

    def menu_comercial_locacao(numero, nome):

        url = f"{BASE_URL}/{PAGE_ID}/messages"

        headers = {
            "Authorization": f"Bearer {WHATSAPP_TOKEN}",
            "Content-Type": "application/json"
        }

        menu = "*O que podemos oferecer*:\n\n*LOCAÇÃO*\n\nLocação de Equipamentos - Serviço de locação de equipamentos"

        data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": numero,
            "type": "interactive",
            "interactive": {
                "type": "button",
                "body": {"text": menu},
                "action": {
                    "buttons": [{'type': "reply",
                                 'reply': {"id": "LOCACAO2",
                                           "title": "Locação"}},
                                {'type': "reply",
                                 'reply': {"id": "voltar",
                                           "title": "VOLTAR"}},
                                ]}}
        }

        try:
            response = requests.post(url, headers=headers, json=data)
            return response
        except requests.exceptions.RequestException as e:
            print(f"Erro ao enviar mensagem: {e}")

    def menu_comercial_cabeamento(numero, nome):

        url = f"{BASE_URL}/{PAGE_ID}/messages"

        headers = {
            "Authorization": f"Bearer {WHATSAPP_TOKEN}",
            "Content-Type": "application/json"
        }

        menu = "\n*O que podemos oferecer*:\n\n*CABEAMENTO*\n\nCabeamento Estruturado - Serviço de Cabeamento Estruturado"

        data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": numero,
            "type": "interactive",
            "interactive": {
                "type": "button",
                "body": {"text": menu},
                "action": {
                    "buttons": [{'type': "reply",
                                 'reply': {"id": "CABEAMENTO",
                                           "title": "Cabeamento"}},
                                {'type': "reply",
                                 'reply': {"id": "voltar",
                                           "title": "VOLTAR"}},
                                ]}}
        }

        try:
            response = requests.post(url, headers=headers, json=data)
            return response
        except requests.exceptions.RequestException as e:
            print(f"Erro ao enviar mensagem: {e}")

    def menu_comercial_dados(numero, nome):

        url = f"{BASE_URL}/{PAGE_ID}/messages"

        headers = {
            "Authorization": f"Bearer {WHATSAPP_TOKEN}",
            "Content-Type": "application/json"
        }

        data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": numero,
            "type": "interactive",
            "interactive": {
                "type": "list",
                "header": {
                    "type": "text",
                    "text": "DADOS"
                },
                "body": {
                    "text": "*O que podemos oferecer*:\n\n*DADOS*\n\nVPN - Serviço de Rede Privada Virtual\n\nFirewall - Serviço de Firewall de Segurança\n\nVirtualização - Serviço de Virtualização de Servidores"
                },
                "footer": {
                    "text": "Opções de serviço de voz abaixo:"
                },
                "action": {
                    "button": "Clique aqui",
                    "sections": [{
                        "title": "Opções de serviço",
                        "rows": [
                            {"id": "VPN", "title": "VPN"},
                            {"id": "FIREWALL", "title": "Firewall"},
                            {"id": "VIRTUALIZACAO", "title": "Virtualização"},
                        ]
                    }]
                }
            }
        }

        try:
            response = requests.post(url, headers=headers, json=data)
            return response
        except requests.exceptions.RequestException as e:
            print(f"Erro ao enviar mensagem: {e}")

    # menu adm

    def menu_adm(numero, nome):

        menu_escolhido = MenuOptions.ADM

        url = f"{BASE_URL}/{PAGE_ID}/messages"

        headers = {
            "Authorization": f"Bearer {WHATSAPP_TOKEN}",
            "Content-Type": "application/json"
        }

        data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": numero,
            "type": "interactive",
            "interactive": {
                "type": "list",
                "header": {
                    "type": "text",
                    "text": "MENU ADMINISTRATIVO"
                },
                "body": {
                    "text": f"BEM VINDO {nome}"
                },
                "footer": {
                    "text": "SELECIONE UMA DAS OPÇOES DE ADMINISTRAÇAO ABAIXO"
                },
                "action": {
                    "button": "Clique aqui",
                    "sections": [{
                        "title": "OPÇOES DE ADMINISTRADOR",
                        "rows": [
                            {"id": "row1", "title": "OBTER LOG DE CONVERSA"},
                            {"id": "row2", "title": "GERENCIAR APLICAÇAO"},
                            {"id": "row3", "title": "HORARIO COMERCIAL"},
                            {"id": "row4", "title": "OPÇOES DE MODERAÇAO"},
                            {"id": "row5", "title": "OPÇOES DE SEGURANÇA"},
                        ]
                    }]
                }
            }
        }

        try:
            response = requests.post(url, headers=headers, json=data)
            return response
        except requests.exceptions.RequestException as e:
            print(f"Erro ao enviar mensagem: {e}")

    # templates

    def menu_opçoes_lista_template(numero, nome):

        url = f"{BASE_URL}/{PAGE_ID}/messages"

        headers = {
            "Authorization": f"Bearer {WHATSAPP_TOKEN}",
            "Content-Type": "application/json"
        }

        data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": numero,
            "type": "interactive",
            "interactive": {
                "type": "list",
                "header": {
                    "type": "text",
                    "text": "TESTE"
                },
                "body": {
                    "text": "MENU TESTE"
                },
                "footer": {
                    "text": "MENU TESTE"
                },
                "action": {
                    "button": "Clique aqui",
                    "sections": [{
                        "title": "Opções do menu teste",
                        "rows": [
                            {"id": "row1", "title": "TESTE 1"},
                            {"id": "row2", "title": "TESTE 2"},
                            {"id": "row3", "title": "TESTE 3"},
                        ]
                    }]
                }
            }
        }

        try:
            response = requests.post(url, headers=headers, json=data)
            return response
        except requests.exceptions.RequestException as e:
            print(f"Erro ao enviar mensagem: {e}")

    def menu_opçao_botao_interativo_template(numero, nome):
        url = f"{BASE_URL}/{PAGE_ID}/messages"
        headers = {
            "Authorization": f"Bearer {WHATSAPP_TOKEN}",
            "Content-Type": "application/json"
        }
        menu = ("*TITULO*"
                "\n"
                "\n*TEXTO*"
                "\n"
                "\nDigite *voltar* para voltar ao *MENU INICIAL*")
        data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": numero,
            "type": "interactive",
            "interactive": {
                "type": "button",
                "body": {"text": menu},
                "action": {
                    "buttons": [{'type': "reply",
                                'reply': {"id": "ID do BOTAO",
                                          "title": "titulo bota"}},
                                {'type': "reply",
                                'reply': {"id": "ID do BOTAO",
                                          "title": "titulo bota"}},
                                {'type': "reply",
                                'reply': {"id": "ID do BOTAO",
                                          "title": "titulo bota"}},
                                ]}}
        }

        try:
            response = requests.post(url, headers=headers, json=data)
            return response
        except requests.exceptions.RequestException as e:
            print(f"Erro ao enviar mensagem: {e}")

    def enviar_link(numero, url):
        url = f"{BASE_URL}/{PAGE_ID}/messages"
        headers = {
            "Authorization": f"Bearer {WHATSAPP_TOKEN}",
            "Content-Type": "application/json"
        }
        menu = ("*NOSSO SITE*"
                "\n"
                "\n*Clique o Link abaixo para acessar nosso site*:")
        data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": numero,
            "type": "interactive",
            "interactive": {
                "type": "cta_url",
                "body": {"text": menu},
                "action": {
                    'name': "cta_url",
                    'parameters': {
                        "display_text": "Clique aqui",
                        "url": url
                    }
                }
            }
        }

        try:
            response = requests.post(url, headers=headers, json=data)
            return response
        except requests.exceptions.RequestException as e:
            print(f"Erro ao enviar mensagem: {e}")

    def enviar_contato(numero, nome_do_contato, numero_contato):
        url = f"{BASE_URL}/156154787575883/messages"
        headers = {
            "Authorization": f"Bearer {WHATSAPP_TOKEN}",
            "Content-Type": "application/json"
        }

        data = {
            "messaging_product": "whatsapp",
            "to": numero,
            "type": "contacts",
            "contacts": [{
                "name": {
                    "first_name": nome_do_contato,
                    "formatted_name": nome_do_contato
                },
                "phones": [{
                    "phone": numero_contato,
                    "wa_id": numero_contato,
                    "type": "Celular"
                }]
            }]
        }

        try:
            response = requests.post(url, headers=headers, json=data)
            return response
        except requests.exceptions.RequestException as e:
            print(f"Erro ao enviar mensagem: {e}")
