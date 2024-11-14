from main import app

@app.route('/')
def homepage():
    return 'meu site no flask'

@app.route('/blog')
def blog():
    return 'bem vindo ao boga'