from main import app # para ele funcionar, ele precisa importar o app que esta presente no arquivo main

@app.route('/')
def homepage():
    return 'Ola mundo'

@app.route('/blog')
def blog():
    return 'bem vindo ao blog'