import os
import datetime
from config_bot import voltar
from menssages import MenuOptions

log_directory = r'C:\Users\nicollas\Desktop\bot\PROJETO\logs'
os.makedirs(log_directory, exist_ok=True)

# menu inicial
menu_inicial_message = ("*MENU INICIAL*\n\n*TELETRON INDUSTRIA E COMERCIO LTDA.*\n\nOlá! seja Bem-vindo a Teletron, Para acessar qualquer um dos menus abaixo apenas escolha a opção desejada\n")
# Financeiro Menu
menu_financeiro_message = ("*FINANCEIRO*\n\n*BEM VINDO AO FINANCEIRO ESCOLHA UMA DAS OPÇOES ABAIXO*\nDigite *voltar* para voltar ao *MENU INICIAL*")
# Suporte Técnico Menu
menu_suporte_tecnico_message1 = ("*SUPORTE*\n\n*PARA SUPORTE PEDIMOS QUE CONFIRME SE JA TEM CONTRATO COM A GENTE*")
menu_suporte_tecnico_message2 = ("SELECIONE UMA DAS OPÇOES DE SUPORTE ABAIXO")
menu_suporte_tecnico_message3 = ("Por favor envie uma menssagem detalhando seu problema:")
# Comercial Menu
menu_comercial_message = ("*COMERCIAL*\n\n*BEM VINDO AO COMERCIAL ESCOLHA UMA DAS OPÇOES ABAIXO*\nDigite *voltar* para voltar ao *MENU INICIAL*")


def registrar_mensagem(numero_user, nome, mensagem, opcao_menu=None):
    log_filename = f"{log_directory}/{numero_user}_log.txt"

    current_time = datetime.datetime.now()
    log_entry = f"\nAs: {current_time}\n \nDe: {nome} ({numero_user})\n \nMensagem: {mensagem}\n"

    if opcao_menu == "inicial":
        log_entry += f"\nAs: {current_time}\n \nDe: BOT\nMENU:\n" + f"\n{menu_inicial_message}\n"

    if opcao_menu == "suporte1":
        log_entry += f"\nAs: {current_time}\n \nDe: BOT\nMENU:\n" + f"\n{menu_suporte_tecnico_message1}\n"

    if opcao_menu == "suporte2":
        log_entry += f"\nAs: {current_time}\n \nDe: BOT\nMENU:\n" + f"\n{menu_suporte_tecnico_message2}\n"

    if opcao_menu == "suporte3":
        log_entry += f"\nAs: {current_time}\n \nDe: BOT\nMENU:\n" + f"\n{menu_suporte_tecnico_message3}\n"

    if opcao_menu == "financeiro":
        log_entry += f"\nAs: {current_time}\n \nDe: BOT\nMENU:\n" + f"\n{menu_financeiro_message}\n"

    if opcao_menu == "comercial":
        log_entry += f"\nAs: {current_time}\n \nDe: BOT\nMENU:\n" + f"\n{menu_comercial_message}"

    with open(log_filename, 'a') as log_file:
        log_file.write(log_entry + '\n')
