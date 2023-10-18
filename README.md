# Importação de módulos

## O código começa importando os módulos flask e requests:

  Flask: um framework web Python popular para construir aplicativos web e APIs
  Requests: uma biblioteca Python popular para fazer requests HTTP

## Configuração do Flask

### Um objeto app do Flask é criado para representar o aplicativo Flask.

O parâmetro name passado é um padrão do Flask que permite que ele saiba onde procurar por arquivos estáticos e templates.
Configurações

### Algumas configurações são definidas:

  - VERIFY_TOKEN: um token usado pelo Facebook para verificar a origem do webhook
  - WHATSAPP_TOKEN: um token de acesso do WhatsApp Business API para enviar mensagens
  - numero_user: armazenará o número do usuário que enviou a mensagem

## Rota para verificação do webhook

### Uma rota é definida para lidar com a verificação do webhook do Facebook:

 - É mapeada para a rota '/'
 - Aceita apenas solicitações GET
 - Verifica se o token de verificação enviado pelo Facebook corresponde ao configurado
 - Se sim, retorna o desafio enviado pelo Facebook
 - Se não, retorna um erro 403

### Isso permite que o Facebook valide que este é o endpoint correto para receber atualizações.
## Rota para receber mensagens

## Outra rota é definida para lidar com mensagens recebidas do webhook do Facebook:

 - Também mapeada para '/'
 - Aceita apenas solicitações POST
 - O JSON enviado pelo Facebook é obtido
 - As mensagens são extraídas e impressas
 - O número do remetente é salvo
 - Retorna "OK"

## Função para enviar mensagens

### A função enviar_msg é definida para enviar mensagens de volta para o usuário via WhatsApp API:

 - Recebe o número e a mensagem como parâmetros
 - Faz request POST para a API com os headers corretos
 - Envia o número, mensagem e token no payload
 - Retorna a resposta da API

## Inicialização

### Por fim, o app Flask é iniciado se o script for executado diretamente.

Isso permite receber mensagens do webhook do Facebook, responder pelo WhatsApp usando a API e iniciar um bot simples.
