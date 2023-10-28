# Chatbot WhatsApp com Python e Flask

## Este projeto consiste em um chatbot para o WhatsApp desenvolvido em Python utilizando o framework Flask.
Módulos Importados

O código inicia importando os seguintes módulos:
  - flask - Framework web Python para construir APIs e aplicativos
  - request - Para lidar com requisições HTTP
  - requests - Cliente HTTP Python para fazer requests
  - config_bot - Arquivo de configuração
  - menssages - Arquivo com as mensagens e menus
  - funcs - Funções úteis

## Configuração do Flask

Um objeto app do Flask é criado para representar o aplicativo:

app = Flask(__name__)

O parâmetro __name__ é padrão e permite que o Flask saiba onde procurar arquivos estáticos e templates.
Configurações

Algumas configurações importantes são definidas no arquivo config_bot.py:

    VERIFY_TOKEN - Token de verificação do webhook do Facebook
    WHATSAPP_TOKEN - Token de acesso à API do WhatsApp
    BASE_URL - URL base da API do WhatsApp
    PAGE_ID - ID da página do WhatsApp

Rota para Verificação do Webhook

Uma rota é definida para lidar com a verificação do webhook pelo Facebook:
@app.route('/', methods=['GET'])
def verify_webhook():

  - Mapeada para raiz '/'
  - Aceita apenas GET
  - Verifica se o token recebido corresponde ao configurado
  - Retorna o desafio se verdadeiro ou 403 se falso

Isso permite que o Facebook valide o endpoint para receber atualizações.
Rota para Receber Mensagens

Outra rota recebe mensagens do webhook:

@app.route('/', methods=['POST'])
def receive_messages():

  - Mapeada para raiz '/'
  - Aceita apenas POST
  - Obtém o JSON e extrai mensagens e contatos
  - Salva número do remetente
  - Retorna "OK"

Função para Enviar Mensagens

A função send_message() envia mensagens para o usuário via API:

def send_message(number, message):

  url = BASE_URL + PAGE_ID + '/messages'  

  headers = {    
    "Authorization": "Bearer " + WHATSAPP_TOKEN
  }
   
  data = {
     "messaging_product": "whatsapp",
     "to": number,
     "text": {"body": message} 
  }

  requests.post(url, headers=headers, json=data)

    Faz request POST para a API
    Adiciona headers e payload
    Envia número, mensagem e token

## Inicialização

Por fim, o app é iniciado:


if __name__ == '__main__':
    app.run(debug=True)

Isso permite receber mensagens do webhook, responder pelo WhatsApp usando a API e ter um chatbot funcional.
Funcionalidades

O chatbot conta com as seguintes funcionalidades:
Menus Interativos

  - Menu inicial
  - Menu de suporte
  - Menu comercial

Com opções na forma de botões e listas.
Fluxo de Conversação

Existe uma lógica para guiar o usuário:

  - Detecção de saudação para mostrar menu inicial
  - Navegação entre menus
  - Respostas personalizadas

Envio de Mensagens

O bot consegue enviar:

  - Texto
  - Botões interativos
  - Listas selecionáveis
  - Links
  - Contatos

Usando a API do WhatsApp.
Registro de Logs

As mensagens do usuário são salvas em arquivos de log.
## Conclusão

O projeto implementa um chatbot funcional no WhatsApp usando Python e Flask. Possui fluxo de conversação, menus interativos, envio de mensagens e logs. Uma ótima base para construir bots mais avançados.
