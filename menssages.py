from config_bot import BASE_URL, PAGE_ID, WHATSAPP_TOKEN
import requests
from enum import Enum
import random
import string


def gerar_codigo_aleatorio(tamanho):
    caracteres = string.ascii_letters + string.digits  # Letras maiúsculas, minúsculas e dígitos
    codigo = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return codigo


codigo_aleatorio = gerar_codigo_aleatorio(8)


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

    # ---------------------------------privacidade---------------------------------

    def menu_privacidade(numero):


        url = f"{BASE_URL}/{PAGE_ID}/messages"

        headers = {
            "Authorization": f"Bearer {WHATSAPP_TOKEN}",
            "Content-Type": "application/json"
        }

        menu = ("*MENU INICIAL*"
                "\n"
                "\n*TELETRON INDUSTRIA E COMERCIO LTDA.*\n\nOlá! Seja bem-vindo à Teletron. Antes de começar sua interação, gostaríamos que você desse uma lida na nossa política de privacidade:"
                "\n"
                "\nLink: "
                "\n"
                '\nSe você concorda com nossos termos, por favor, selecione "Aceito". Caso contrário, selecione "Não aceito".'
                "\n"
                "\nLembre-se de que aceitar os termos vai melhorar e personalizar sua experiência."
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
                                           "title": "EU NÃO CONCORDO"}},
                                ]}}
        }

        try:
            response = requests.post(url, headers=headers, json=data)
            return response
        except requests.exceptions.RequestException as e:
            print(f"Erro ao enviar mensagem: {e}")

    # ---------------------------------inicial---------------------------------

    def menu_inicial(numero, nome):


        url = f"{BASE_URL}/{PAGE_ID}/messages"

        headers = {
            "Authorization": f"Bearer {WHATSAPP_TOKEN}",
            "Content-Type": "application/json"
        }

        menu = ("*MENU INICIAL*"
                "\n"
                "\n*TELETRON INDUSTRIA E COMERCIO LTDA.*\n\nOlá! Seja bem-vindo à Teletron. Para acessar qualquer um dos menus abaixo, basta escolher a opção desejada:"
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
                                           "title": "SUPORTE TÉCNICO"}},
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
                "\nAperte o botão *VOLTAR* para retornar ao *MENU INICIAL**"
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

# -------------------------------------financeiro-------------------------------------

    def menu_financeiro2(numero, nome):

        url = f"{BASE_URL}/{PAGE_ID}/messages"

        headers = {
            "Authorization": f"Bearer {WHATSAPP_TOKEN}",
            "Content-Type": "application/json"
        }

        menu = ("*FINANCEIRO*"
                "\n"
                "\n*BEM-VINDO AO FINANCEIRO. ESCOLHA UMA DAS OPÇÕES ABAIXO*"
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
                                 'reply': {"id": "1FINANCEIRO",
                                           "title": "RESUMO DE CONTAS"}},
                                {'type': "reply",
                                 'reply': {"id": "2FINANCEIRO",
                                           "title": "SUPORTE FINANCEIRO"}},
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

    # ---------------------------------suporte tecnico---------------------------------

    def menu_voltar_suporte(numero, nome):

        url = f"{BASE_URL}/{PAGE_ID}/messages"

        headers = {
            "Authorization": f"Bearer {WHATSAPP_TOKEN}",
            "Content-Type": "application/json"
        }

        menu = (
                "\n"
                "\nPara voltar ao Menu Inicial ou entrar em contato, por favor, pressione um dos botões abaixo:"
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

    def menu_supote_tecnico(numero, nome):

        url = f"{BASE_URL}/{PAGE_ID}/messages"

        headers = {
            "Authorization": f"Bearer {WHATSAPP_TOKEN}",
            "Content-Type": "application/json"
        }

        menu = ("*SUPORTE*"
                "\n"
                "\n*PARA SUPORTE, PEDIMOS QUE CONFIRME SE JÁ TEM CONTRATO CONOSCO*"
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
                                           "title": "NÃO"}},
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

    def menu_suporte_opcoes2(numero, nome):

        url = f"{BASE_URL}/{PAGE_ID}/messages"

        headers = {
            "Authorization": f"Bearer {WHATSAPP_TOKEN}",
            "Content-Type": "application/json"
        }

        mensagem = ("*SUPORTE*"
                    "\n"
                    "\nInfelizmente, a opção de suporte não está disponível para você, já que você não é um de nossos clientes. Por favor, vá ao MENU COMERCIAL para começar a usar nossos serviços."
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
                    "\n\n*FORMULÁRIO*"
                    f"\n\nNÚMERO do formulário: *{codigo_aleatorio}*"
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

        mensagem = (
                    "*SUPORTE*"
                    "\n"
                    "\nPor favor, envie uma mensagem detalhando seu problema:"
                    "\n"
                    "\nPara descrever o problema, copie e preencha o formulário a seguir:"
                    "\n\n*FORMULÁRIO*:"
                    "\n(*COPIE O NÚMERO DO FORMULÁRIO E NÃO O ALTERE*)"
                    f"\n\nNÚMERO do formulário: *{codigo_aleatorio}*"
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

    # -------------------------------------comercial-------------------------------------

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
                    "text": "*O que podemos oferecer*:\n\n*Voz*\n\n    SIP Server\n    Gravador de Chamadas\n    Aparelhos IP\n    URA\n    Gateways\n    Correio de Voz\n    Relatórios\n\n*Dados*\n\n    VPN\n    Firewall\n    Virtualização\n\n*Segurança*\n\n    CFTV\n    Central de Cerca Elétrica\n    Central de Alarme\n\n*Cabeamento*\n\n    Cabeamento Estruturado\n\n*Locação*\n\n    Locação de Equipamentos"
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
                            {"id": "LOCACAO", "title": "LOCAÇÃO"},
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

# ---------------------------------------------------------------------------------------------------------

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
                    "text": "*O que podemos oferecer*:\n\n*Voz*\n\nSIP Server - Serviço de servidor de voz SIP\n\nGravador de Chamadas - Serviço de gravação de chamadas\n\nAparelhos IP - Serviço de telefonia com aparelhos IP\n\nURA - Atendimento automático de voz\n\nGateways - Serviço de integração de rede\n\nCorreio de Voz - Serviço de caixa de correio de voz\n\nRelatórios - Geração de relatórios de chamadas"
                },
                "footer": {
                    "text": "Opções de serviço de voz abaixo:"
                },
                "action": {
                    "button": "Clique aqui",
                    "sections": [{
                        "title": "Opções de serviço",
                        "rows": [
                            {"id": "SIP_SERVER", "title": "SIP Server"},
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

    def enviar_msg_SipServer(numero):

        url = f"{BASE_URL}/{PAGE_ID}/messages"

        headers = {
            "Authorization": f"Bearer {WHATSAPP_TOKEN}",
            "Content-Type": "application/json"
        }

        mensagem = (
                    "*SipServer*"
                    "\n\nPara solicitar esse serviço, você deve enviar uma mensagem contendo as seguintes informações:"
                    "\n\nNo topo da mensagem, obrigatoriamente deve conter o código do formulário"
                    f"\n\nCódigo do formulário: {codigo_aleatorio}"
                    "\n\nInformações que precisam estar na mensagem:"
                    "\n\nInformações do contratante:"
                    "\n   Nome: [Seu Nome]"
                    "\n   Nome da empresa: [Nome da empresa]"
                    "\n   Setor da empresa: [Setor da empresa]"
                    "\n\n   Tamanho da empresa: [número de funcionários]"
                    "\n\nDetalhes técnicos:"
                    "\n   Número de linhas SIP necessárias"
                    "\n   Necessidades específicas de chamadas (ex.: videoconferência)"
                    "\n   Requisitos de segurança"
                    "\n\nPreferências de serviço:"
                    "\n   Tipo de serviço (hospedagem de SIP, SIP trunking)"
                    "\n   Duração do contrato desejada"
                    "\n   Suporte técnico"
                    "\n   Integração com outros sistemas"
                    "\n\nTráfego estimado:"
                    "\n   Número estimado de chamadas simultâneas"
                    "\n   Volume de tráfego de voz ou dados"
                    )

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

    def enviar_msg_exemplo(numero):

        url = f"{BASE_URL}/{PAGE_ID}/messages"

        headers = {
            "Authorization": f"Bearer {WHATSAPP_TOKEN}",
            "Content-Type": "application/json"
        }

        mensagem = (
                    "*Exemplo*:"
                    f"\n\n{codigo_aleatorio}\n\n[Texto com as informaçoes pedidas faça do jeito que preferir]\n\nCaso voce nao saiba algumas das infomaçoes pedidas basta ignorar e continuar com as que voce pode fornecer, essa menssagem vai servir apenas para termos uma breve descriçao sobre o serviço requisitado"
                    )

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

    def enviar_msg_Gravador(numero):

        url = f"{BASE_URL}/{PAGE_ID}/messages"

        headers = {
            "Authorization": f"Bearer {WHATSAPP_TOKEN}",
            "Content-Type": "application/json"
        }

        mensagem = (
                    "*Gravador de chamadas*"
                    "\n\nPara solicitar esse serviço, você deve enviar uma mensagem contendo as seguintes informações:"
                    "\n\nNo topo da mensagem, obrigatoriamente deve conter o código do formulário"
                    f"\n\nCódigo do formulário: {codigo_aleatorio}"
                    "\n\nInformações que precisam estar na mensagem:"
                    "\n\nInformações do contratante:"
                    "\n   Nome: [Seu Nome]"
                    "\n   Nome da empresa: [Nome da empresa]"
                    "\n   Setor da empresa: [Setor da empresa]"
                    "\n   Tamanho da empresa: [número de funcionários]"
                    "\n\nDetalhes do serviço:"
                    "\n   Estimativa de usuários do serviço de gravação"
                    "\n   Tipo de linha telefônica (análogica, digital, VoIP, etc.)"
                    "\n   Número de linhas a serem gravadas"
                    "\n   Duração esperada das gravações (horas por dia)"
                    "\n\nRequisitos específicos:"
                    "\n   Integrações necessárias (ex.: integração com CRM)"
                    "\n   Funcionalidades desejadas (marcação de chamadas importantes, pesquisa de palavras-chave, etc.)"
                    "\n\nArmazenamento e retenção dos dados:"
                    "\n   Duração de retenção das gravações (meses, anos)"
                    "\n   Capacidade de armazenamento necessária"
                    "\n\nComentários ou observações adicionais: (Opcional)"
                    )

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

    def enviar_msg_AparelhoIP(numero):

        url = f"{BASE_URL}/{PAGE_ID}/messages"

        headers = {
            "Authorization": f"Bearer {WHATSAPP_TOKEN}",
            "Content-Type": "application/json"
        }

        mensagem = (
                    "*Aparelhos IP*"
                    "\n\nPara solicitar esse serviço, você deve enviar uma mensagem contendo as seguintes informações:"
                    "\n\nNo topo da mensagem, obrigatoriamente deve conter o código do formulário"
                    f"\n\nCódigo do formulário: {codigo_aleatorio}"
                    "\n\nInformações que precisam estar na mensagem:"
                    "\n\nInformações do contratante:"
                    "\n   Nome: [Seu Nome]"
                    "\n   Nome da empresa: [Nome da empresa]"
                    "\n   Setor da empresa: [Setor da empresa]"
                    "\n   Tamanho da empresa: [número de funcionários]"
                    "\n\nTipo de serviço:"
                    "\n   Tipo de aparelho IP desejado (VoIP, SIP, softphone, etc.)"
                    "\n\nNecessidades de hardware:"
                    "\n   Número ou estimativa de aparelhos IP necessários"
                    "\n   Modelo ou especificações desejadas (opcional)"
                    "\n\nLocalização e rede:"
                    "\n   Localização da instalação (se houver várias filiais)"
                    "\n   Detalhes sobre a infraestrutura de rede existente (opcional)"
                    "\n\nIntegrações e recursos:"
                    "\n   Integrações com outros sistemas ou aplicativos"
                    "\n   Recursos desejados (conferência, gravação de chamadas, transferência de chamadas, etc.)"
                    "\n\nRequisitos de segurança:"
                    "\n   Medidas de segurança necessárias (criptografia, autenticação de chamadas)"
                    "\n\nVolume de chamadas:"
                    "\n   Número estimado de chamadas por dia/semana/mês"
                    "\n\nNecessidades de suporte:"
                    "\n   Nível de suporte desejado (ex.: suporte presencial)"
                    "\n\nComentários ou observações adicionais: (Opcional)"
                    )

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

    def enviar_msg_Gateways(numero):

        url = f"{BASE_URL}/{PAGE_ID}/messages"

        headers = {
            "Authorization": f"Bearer {WHATSAPP_TOKEN}",
            "Content-Type": "application/json"
        }

        mensagem = (
                    "*Gateways*"
                    "\n\nPara solicitar esse serviço, você deve enviar uma mensagem contendo as seguintes informações:"
                    "\n\nNo topo da mensagem, obrigatoriamente deve conter o código do formulário"
                    f"\n\nCódigo do formulário: {codigo_aleatorio}"
                    "\n\nInformações que precisam estar na mensagem:"
                    "\n\nInformações do contratante:"
                    "\n   Nome: [Seu Nome]"
                    "\n   Nome da empresa: [Nome da empresa]"
                    "\n   Setor da empresa: [Setor da empresa]"
                    "\n   Tamanho da empresa: [número de funcionários]"
                    "\n\nDetalhes do serviço:"
                    "\n   Tipo de serviço de gateways (integração de pagamento, SMS, API, etc.)"
                    "\n   Descrição das necessidades do projeto"
                    "\n   Plataformas ou sistemas com os quais o gateway deve ser compatível"
                    "\n\nVolume de transações:"
                    "\n   Número médio de transações por mês"
                    "\n   Valor médio por transação"
                    "\n\nRequisitos técnicos:"
                    "\n   Integração necessária (REST API, Webhooks, etc.)"
                    "\n   Recursos específicos (segurança, criptografia)"
                    "\n   Plataformas ou linguagens de programação usadas"
                    "\n\nComentários ou observações adicionais: (Opcional)"
                    )

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

    def enviar_msg_URA(numero):

        url = f"{BASE_URL}/{PAGE_ID}/messages"

        headers = {
            "Authorization": f"Bearer {WHATSAPP_TOKEN}",
            "Content-Type": "application/json"
        }

        mensagem = (
                    "*URA*"
                    "\n\nPara solicitar esse serviço, você deve enviar uma mensagem contendo as seguintes informações:"
                    "\n\nNo topo da mensagem, obrigatoriamente deve conter o código do formulário"
                    f"\n\nCódigo do formulário: {codigo_aleatorio}"
                    "\n\nInformações que precisam estar na mensagem:"
                    "\n\nInformações do contratante:"
                    "\n   Nome: [Seu Nome]"
                    "\n   Nome da empresa: [Nome da empresa]"
                    "\n   Setor da empresa: [Setor da empresa]"
                    "\n   Tamanho da empresa: [número de funcionários]"
                    "\n\nDetalhes do serviço:"
                    "\n   Tipo de serviço de URA desejado (menu de atendimento, resposta a FAQs, pesquisa de satisfação, etc.)"
                    "\n   Número estimado de ramais ou extensões necessárias"
                    "\n   Complexidade do menu (simples, intermediária, avançada)"
                    "\n   Integração com sistemas existentes (opcional)"
                    "\n\nVolume de chamadas:"
                    "\n   Estimativa do número de chamadas recebidas por dia/semana/mês"
                    "\n   Horário de pico das chamadas"
                    "\n\nOutros recursos:"
                    "\n   Necessidade de encaminhamento de chamadas para atendentes humanos"
                    "\n   Integração com serviços de atendimento ao cliente (CRM)"
                    "\n\nComentários ou observações adicionais: (Opcional)"
                    )

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

    def enviar_msg_Correio_de_voz(numero):

        url = f"{BASE_URL}/{PAGE_ID}/messages"

        headers = {
            "Authorization": f"Bearer {WHATSAPP_TOKEN}",
            "Content-Type": "application/json"
        }

        mensagem = (
                    "*Correio de voz*"
                    "\n\nPara solicitar esse serviço, você deve enviar uma mensagem contendo as seguintes informações:"
                    "\n\nNo topo da mensagem, obrigatoriamente deve conter o código do formulário"
                    f"\n\nCódigo do formulário: {codigo_aleatorio}"
                    "\n\nInformações que precisam estar na mensagem:"
                    "\n\nInformações do contratante:"
                    "\n   Nome: [Seu Nome]"
                    "\n   Nome da empresa: [Nome da empresa]"
                    "\n   Setor da empresa: [Setor da empresa]"
                    "\n   Tamanho da empresa: [número de funcionários]"
                    "\n\nDetalhes do serviço de Correio de Voz:"
                    "\n   Número de usuários"
                    "\n   Necessidade de integração com e-mail"
                    "\n   Fuso horário preferido para receber mensagens de voz"
                    "\n\nPreferências de mensagem:"
                    "\n   Formato do arquivo de áudio preferido (MP3, WAV, etc.)"
                    "\n   Informações a serem incluídas no corpo do e-mail (data, hora, duração, número identificado)"
                    "\n\nComentários ou observações adicionais: (Opcional)"
                    )

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

    def enviar_msg_Relatorios(numero):

        url = f"{BASE_URL}/{PAGE_ID}/messages"

        headers = {
            "Authorization": f"Bearer {WHATSAPP_TOKEN}",
            "Content-Type": "application/json"
        }

        mensagem = (
                    "*Relatórios*"
                    "\n\nPara solicitar esse serviço, você deve enviar uma mensagem contendo as seguintes informações:"
                    "\n\nNo topo da mensagem, obrigatoriamente deve conter o código do formulário"
                    f"\n\nCódigo do formulário: {codigo_aleatorio}"
                    "\n\nInformações que precisam estar na mensagem:"
                    "\n\nInformações do contratante:"
                    "\n   Nome: [Seu Nome]"
                    "\n   Nome da empresa: [Nome da empresa]"
                    "\n   Setor da empresa: [Setor da empresa]"
                    "\n   Tamanho da empresa: [número de funcionários]"
                    "\n\nDetalhes do Serviço Desejado:"
                    "\n   Tipo de relatório (relatório de desempenho, fluxo de chamadas, custos, etc.)"
                    "\n   Abrangência (chamadas internas, chamadas externas, entrada, saída)"
                    "\n   Objetivos do relatório (aprimoramento na distribuição de chamadas, redução de custos, etc.)"
                    "\n\nInformações sobre a infraestrutura de telecomunicações:"
                    "\n   Tipo de sistema telefônico (por exemplo, PBX, VoIP)"
                    "\n   Número de linhas telefônicas"
                    "\n   Número de ramais"
                    "\n   Integrações com outros sistemas (opcional)"
                    "\n\nRequisitos Específicos:"
                    "\n   Período de análise desejado"
                    "\n   Necessidades de customização"
                    "\n\nComentários ou observações adicionais: (Opcional)"
                    )

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

# ---------------------------------------------------------------------------------------------------------

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

    def enviar_msg_CFTV(numero):

        url = f"{BASE_URL}/{PAGE_ID}/messages"

        headers = {
            "Authorization": f"Bearer {WHATSAPP_TOKEN}",
            "Content-Type": "application/json"
        }

        mensagem = (
                    "*CFTV*"
                    "\n\nPara solicitar esse serviço voce deve enviar uma menssagem contendo as seguintes infomaçoes:"
                    "\n\nNo topo da menssagem obrigatoriamente deve conter o codigo do formulario"
                    f"\n\nCodigo do formulario {codigo_aleatorio}"
                    "\n\nInformaçoes que precisam estar na menssagem:"
                    "\n\nInformações do contratante:"
                    "\n   Nome: [Seu Nome]"
                    "\n   Nome da empresa: [Nome da empresa]"
                    "\n   Setor da empresa: [Setor da empresa]"
                    "\n   Tamanho da empresa: [número de funcionários]"
                    "\n\nDetalhes do serviço:"
                    "\n   Virtualizacao"
                    "\n   Tipo de câmeras (interna, externa, infravermelho, etc.)"
                    "\n   Resolução das câmeras (SD, HD, Full HD, 4K)"
                    "\n   Necessidade de gravação contínua ou por detecção de movimento"
                    "\n\nInstalação:"
                    "\n   Localização da instalação (endereço)"
                    "\n   Tipo de propriedade (residencial, comercial, industrial)"
                    "\n   Necessidade de fiação ou preferência por câmeras sem fio"
                    "\n\nMonitoramento:"
                    "\n   Necessidade de monitoramento remoto (via smartphone ou computador)"
                    "\n   Necessidade de serviço de monitoramento profissional"
                    "\n\nRecursos adicionais:"
                    "\n   Visão noturna"
                    "\n   Armazenamento em nuvem"
                    "\n\nManutenção:"
                    "\n   Frequência desejada de manutenção (mensal, trimestral, anual)"
                    "\n\nComentários ou observações adicionais:(Opcional)"
                    )

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

    def enviar_msg_Central_de_Cerca_Eletrica(numero):

        url = f"{BASE_URL}/{PAGE_ID}/messages"

        headers = {
            "Authorization": f"Bearer {WHATSAPP_TOKEN}",
            "Content-Type": "application/json"
        }

        mensagem = (
                    "*Central de Cerca Elétrica*"
                    "\n\nPara solicitar esse serviço, você deve enviar uma mensagem contendo as seguintes informações:"
                    "\n\nNo topo da mensagem, obrigatoriamente deve conter o código do formulário"
                    f"\n\nCódigo do formulário {codigo_aleatorio}"
                    "\n\nInformações que precisam estar na mensagem:"
                    "\n\nInformações do contratante:"
                    "\n   Nome: [Seu Nome]"
                    "\n   Nome da empresa: [Nome da empresa]"
                    "\n   Setor da empresa: [Setor da empresa]"
                    "\n   Tamanho da empresa: [número de funcionários]"
                    "\n\nDetalhes do serviço:"
                    "\n   Comprimento total da cerca elétrica (em metros)"
                    "\n   Altura da cerca elétrica (em metros)"
                    "\n   Número de linhas de fio na cerca"
                    "\n   Tipo de propriedade (residencial, comercial, industrial)"
                    "\n   Tipo de cerca (convencional, com alarme, etc.)"
                    "\n\nRecursos adicionais:"
                    "\n   Controle remoto (opcional)"
                    "\n   Sistema de alerta"
                    "\n\nInstalação:"
                    "\n   Localização da instalação (endereço)"
                    "\n   Necessidade de remoção de uma cerca existente"
                    "\n\nManutenção:"
                    "\n   Frequência desejada de manutenção (mensal, trimestral, anual)"
                    "\n\nComentários ou observações adicionais: (Opcional)"
                    )

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

    def enviar_msg_Central_de_Alarme(numero):

        url = f"{BASE_URL}/{PAGE_ID}/messages"

        headers = {
            "Authorization": f"Bearer {WHATSAPP_TOKEN}",
            "Content-Type": "application/json"
        }

        mensagem = (
                    "*Central de Alarme*"
                    "\n\nPara solicitar esse serviço, você deve enviar uma mensagem contendo as seguintes informações:"
                    "\n\nNo topo da mensagem, obrigatoriamente deve conter o código do formulário"
                    f"\n\nCódigo do formulário {codigo_aleatorio}"
                    "\n\nInformações que precisam estar na mensagem:"
                    "\n\nInformações do contratante:"
                    "\n   Nome: [Seu Nome]"
                    "\n   Nome da empresa: [Nome da empresa]"
                    "\n   Setor da empresa: [Setor da empresa]"
                    "\n   Tamanho da empresa: [número de funcionários]"
                    "\n\nDetalhes do serviço:"
                    "\n   Tipo de propriedade (residencial, comercial, industrial)"
                    "\n   Tamanho da propriedade (em metros quadrados)"
                    "\n   Número de Entradas/Saídas"
                    "\n   Número de Janelas"
                    "\n   Existência de áreas sensíveis (como cofres, áreas restritas)"
                    "\n\nPreferências do sistema de alarme:"
                    "\n   Tipo de sistema de alarme (Monitorado ou Não Monitorado)"
                    "\n   Números de telefone para alertas (se o sistema não for monitorado)"
                    "\n   Preferência por sensores sem fio ou com fio"
                    "\n   Integração com CFTV"
                    "\n\nComentários ou observações adicionais: (Opcional)"
                    )

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

# -----------------------------------------------------------------------------------------
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

        try:
            response = requests.post(url, headers=headers, json=data)
            return response
        except requests.exceptions.RequestException as e:
            print(f"Erro ao enviar mensagem: {e}")

    def enviar_msg_Locação_de_equipamentos(numero):

        url = f"{BASE_URL}/{PAGE_ID}/messages"

        headers = {
            "Authorization": f"Bearer {WHATSAPP_TOKEN}",
            "Content-Type": "application/json"
        }

        mensagem = (
                    "*Locação*"
                    "\n\nPara solicitar esse serviço, você deve enviar uma mensagem contendo as seguintes informações:"
                    "\n\nNo topo da mensagem, obrigatoriamente deve conter o código do formulário"
                    f"\n\nCódigo do formulário {codigo_aleatorio}"
                    "\n\nInformações que precisam estar na mensagem:"
                    "\n\nInformações do contratante:"
                    "\n   Nome: [Seu Nome]"
                    "\n   Nome da empresa: [Nome da empresa]"
                    "\n   Setor da empresa: [Setor da empresa]"
                    "\n   Tamanho da empresa: [número de funcionários]"
                    "\n\nDetalhes do serviço:"
                    "\n   Tipo de Serviço (Dados, Voz ou Ambos)"
                    "\n   Número de Usuários"
                    "\n   Número de Locais"
                    "\n\nEquipamentos e Serviços Necessários:"
                    "\n   Equipamentos de Dados (VPN, Firewall, Servidores Virtuais)"
                    "\n   Equipamentos de Voz (Sip Server, Gravador de Chamadas, Aparelhos IP, URA, Gateways, Correio de Voz ou Relatórios)"
                    "\n\nDescrição da infraestrutura desejada: (Descreva a infraestrutura desejada)"
                    "\n\nComentários ou observações adicionais: (Opcional)"
                    )

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

# -----------------------------------------------------------------------------------------

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

    def enviar_msg_Cabeamento_estruturado(numero):

        url = f"{BASE_URL}/{PAGE_ID}/messages"

        headers = {
            "Authorization": f"Bearer {WHATSAPP_TOKEN}",
            "Content-Type": "application/json"
        }

        mensagem = (
                    "*Cabeamento*"
                    "\n\nPara solicitar esse serviço, você deve enviar uma mensagem contendo as seguintes informações:"
                    "\n\nNo topo da mensagem obrigatoriamente deve conter o código do formulário"
                    f"\n\nCódigo do formulário {codigo_aleatorio}"
                    "\n\nInformações que precisam estar na mensagem:"
                    "\n\nInformações do contratante:"
                    "\n   Nome: [Seu Nome]"
                    "\n   Nome da empresa: [Nome da empresa]"
                    "\n   Setor da empresa: [Setor da empresa]"
                    "\n   Tamanho da empresa: [número de funcionários]"
                    "\n\nDetalhes do projeto:"
                    "\n   Tipo de propriedade (residencial, comercial, industrial)"
                    "\n   Tamanho da propriedade (em metros quadrados)"
                    "\n   Número de andares/pisos"
                    "\n   Número de salas/áreas de trabalho"
                    "\n   Número de pontos de rede por sala/área"
                    "\n\nNecessidades de Rede:"
                    "\n   Velocidade de transmissão desejada (1 Gbps, 10 Gbps, etc.)"
                    "\n   Tipo de serviço (voz, dados, vídeo)"
                    "\n\nPreferências do sistema:"
                    "\n   Tipo de cabo (UTP, STP, etc.)"
                    "\n   Categoria do cabo (Cat5e, Cat6, Cat6a, etc.)"
                    "\n   Tipo de conector (RJ45, etc.)"
                    "\n   Necessidade de Patch Panels"
                    "\n   Necessidade de racks ou armários"
                    "\n\nComentários ou observações adicionais:(Opcional)"
                    )

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

# -----------------------------------------------------------------------------------------

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

    def enviar_msg_VPN(numero):

        url = f"{BASE_URL}/{PAGE_ID}/messages"

        headers = {
            "Authorization": f"Bearer {WHATSAPP_TOKEN}",
            "Content-Type": "application/json"
        }

        mensagem = (
                    "*VPN*"
                    "\n\nPara solicitar esse serviço voce deve enviar uma menssagem contendo as seguintes infomaçoes:"
                    "\n\nNo topo da menssagem obrigatoriamente deve conter o codigo do formulario"
                    f"\n\nCodigo do formulario {codigo_aleatorio}"
                    "\n\nInformaçoes que precisam estar na menssagem:"
                    "\n\nInformações do contratante:"
                    "\n   Nome: [Seu Nome]"
                    "\n   Nome da empresa: [Nome da empresa]"
                    "\n   Setor da empresa: [Setor da empresa]"
                    "\n   Tamanho da empresa: [número de funcionários]"
                    "\n\nDetalhes do serviço:"
                    "\n   Número de usuários da VPN"
                    "\n   Localização dos usuários (local, nacional, internacional)"
                    "\n   Tipo de dispositivos a serem usados (desktop, celular, ambos)"
                    "\n   Integração com infraestrutura existente (opcional)"
                    "\n\nRequisitos de segurança:"
                    "\n   Requisitos específicos de conformidade (por exemplo, GDPR, LGPD)"
                    "\n\nRecursos adicionais:"
                    "\n   Velocidade de conexão desejada"
                    "\n   Serviços adicionais (ex.: proteção contra malware)"
                    "\n\nComentários ou observações adicionais:(Opcional)"
                    )

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

    def enviar_msg_Firewall(numero):

        url = f"{BASE_URL}/{PAGE_ID}/messages"

        headers = {
            "Authorization": f"Bearer {WHATSAPP_TOKEN}",
            "Content-Type": "application/json"
        }

        mensagem = (
                    "*Firewall*"
                    "\n\nPara solicitar esse serviço voce deve enviar uma menssagem contendo as seguintes infomaçoes:"
                    "\n\nNo topo da menssagem obrigatoriamente deve conter o codigo do formulario"
                    f"\n\nCodigo do formulario {codigo_aleatorio}"
                    "\n\nInformaçoes que precisam estar na menssagem:"
                    "\n\nInformações do contratante:"
                    "\n   Nome: [Seu Nome]"
                    "\n   Nome da empresa: [Nome da empresa]"
                    "\n   Setor da empresa: [Setor da empresa]"
                    "\n   Tamanho da empresa: [número de funcionários]"
                    "\n\nDetalhes do serviço:"
                    "\n   Número de usuários do firewall"
                    "\n   Localização dos usuários (local, nacional, internacional)"
                    "\n   Tipo de dispositivos a serem usados (desktop, celular, ambos)"
                    "\n   Integração com infraestrutura existente (opcional)"
                    "\n\nRequisitos de segurança:"
                    "\n   Requisitos específicos de conformidade (por exemplo, GDPR, LGPD)"
                    "\n\nRecursos adicionais:"
                    "\n   Captive Portal para HOTSPOT (Check-in em redes sociais, personalização da página de login)"
                    "\n   VPN para atividades EXTRA OFFICE ou HOME OFFICE (Número de conexões VPN necessárias, tipo de VPN (por exemplo, PPTP, L2TP/IPsec, OpenVPN))"
                    "\n\nComentários ou observações adicionais:(Opcional)"
                    )

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

    def enviar_msg_Virtualizacao(numero):

        url = f"{BASE_URL}/{PAGE_ID}/messages"

        headers = {
            "Authorization": f"Bearer {WHATSAPP_TOKEN}",
            "Content-Type": "application/json"
        }

        mensagem = (
                    "*Virtualizacao*"
                    "\n\nPara solicitar esse serviço voce deve enviar uma menssagem contendo as seguintes infomaçoes:"
                    "\n\nNo topo da menssagem obrigatoriamente deve conter o codigo do formulario"
                    f"\n\nCodigo do formulario {codigo_aleatorio}"
                    "\n\nInformaçoes que precisam estar na menssagem:"
                    "\n\nInformações do contratante:"
                    "\n   Nome: [Seu Nome]"
                    "\n   Nome da empresa: [Nome da empresa]"
                    "\n   Setor da empresa: [Setor da empresa]"
                    "\n   Tamanho da empresa: [número de funcionários]"
                    "\n\nDetalhes do serviço:"
                    "\n   Número de servidores a serem virtualizados"
                    "\n   Sistema operacional dos servidores"
                    "\n   Recursos necessários por servidor (CPU, RAM, armazenamento)"
                    "\n\nServiço de Virtualização PVE:"
                    "\n   Número de usuários da interface web"
                    "\n   Quantidade de VMs necessárias"
                    "\n   Sistema operacional"
                    "\n\nCLUSTER:"
                    "\n   Número de processos com alta complexidade"
                    "\n   Requisitos de alta disponibilidade"
                    "\n   Necessidade de configuração de cluster"
                    "\n\nServiço de autoconfiguração – WPAD"
                    "\n   Controlador de Domínio + GPOs + FileServer"
                    "\n     Número de máquinas Windows na rede"
                    "\n     Políticas de segurança específicas"
                    "\n     File Server"
                    "\n     Capacidade de armazenamento"
                    "\n     Número de grupos"
                    "\n     Restrições de acesso específicas"
                    "\n   Servidor de e-mails:"
                    "\n     Número de contas de e-mail"
                    "\n     Políticas anti-spam específicas"
                    "\n   Backup"
                    "\n     Frequência do backup (diário, semanal, mensal)"
                    "\n     Tamanho dos dados para backup"
                    "\n\nComentários ou observações adicionais:(Opcional)"
                    )

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

    # ---------------------------------------menu adm---------------------------------------

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

    # ---------------------------------------templates---------------------------------------

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

    def enviar_imagem(numero, url):
        url = f"{BASE_URL}/{PAGE_ID}/messages"
        headers = {
            "Authorization": f"Bearer {WHATSAPP_TOKEN}",
            "Content-Type": "application/json"
        }

        data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": numero,
            "type": "image",
            "image": {
                "link": url,
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
