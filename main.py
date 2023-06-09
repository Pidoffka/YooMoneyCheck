from flask import Flask, request

app = Flask('myapp')

client_id = '5DF8AB812B99F7D63DC8B0E040532CAAF4239B274A69E5C0341AC80D9BCC9808'

client_secret = 'C21490F43D028DBEF1951943B1B66D93D1BDB6F7DA56891C61C8DC71F0F2B26B50DC9B97660C21F488694B354655048DC8E1E19C41B7887A1577752493CE6FDE'

url = f'https://yoomoney.ru/oauth/authorize?response_type=code&client_id={client_id}&redirect_uri=http://127.0.0.1:8000/redirect=&scope=payment'
print(url)

@app.route('/redirect', methods=['GET'])
def handle_redirect():
    # Обработка перенаправления от Юмани
    code = request.args.get('code')
    print(code)
    # Дальнейшая обработка полученного авторизационного кода


@app.route('/notification', methods=['POST'])
def handle_notification():
    # Обработка уведомления об успешной операции перевода
    data = request.get_json()
    # Дальнейшая обработка информации об операции


if __name__ == '__main__':
    app.run(port=8000)
