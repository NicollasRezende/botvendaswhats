from flask import Flask, request
import requests

app = Flask(__name__)

VERIFY_TOKEN = "TAGVALUE"
WHATSAPP_TOKEN = "EAAcT7pjYZBf0BOyzjAhMrEipPqvoYvog9BjYcAS4YNaM23Lt4nZC3XFVeZCQaN750DW3lZCAZBMz9VHz0ZCUCMRYZA0hz0gEsLn7Hgcilc8NPxZBZBrIc7teNnQZCwvYazt4zDWpRgLruTOIYDCXYr6hrCJhYhyOZAwnu5D8xb5k0ZBbF6jmfT5biv5ul98kP2p9aJe7pgMgZBEx1EjC7v9vOy4xLnIla6qpZB"
numero_user = None
numero_user2 = '5561991769500'


@app.route('/', methods=['GET'])
def verify_webhook():
    if request.args.get("hub.verify_token") == "TAGVALUE":
        return request.args.get("hub.challenge")
    return "Verificação falhou", 403


@app.route('/', methods=['POST'])
def receive_messages():
    data = request.get_json()

    print("Recebido POST de WhatsApp:")
    messages = data['entry'][0]['changes'][0]['value']['messages']

    for message in messages:
        text = message['text']['body']
        numero_user = message['from']

        print(f"Mensagem recebida: {text}, de: {numero_user}")

    # if text == 'A':
    #     print()
    #     print(f'Menssagem sendo enviada para: {numero_user}')
    #     enviar_msg(numero_user, 'a')
    #     print()

    return "OK"


@app.route('/', methods=['POST'])
def enviar_msg(number: str, msg: str):
    url = "https://graph.facebook.com/v17.0/131513573373309/messages"
    headers = {
        "Authorization": "Bearer EAAcT7pjYZBf0BOyzjAhMrEipPqvoYvog9BjYcAS4YNaM23Lt4nZC3XFVeZCQaN750DW3lZCAZBMz9VHz0ZCUCMRYZA0hz0gEsLn7Hgcilc8NPxZBZBrIc7teNnQZCwvYazt4zDWpRgLruTOIYDCXYr6hrCJhYhyOZAwnu5D8xb5k0ZBbF6jmfT5biv5ul98kP2p9aJe7pgMgZBEx1EjC7v9vOy4xLnIla6qpZB",
        "Content-Type": "application/json",
    }
    data = {
        "messaging_product": "whatsapp",
        "to": f'{number}',
        "type": "text",
        "text": {"body": f'{msg}'},
    }
    return requests.post(url, headers=headers, json=data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
