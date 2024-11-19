from flask import Flask

app = Flask(__name__)

from views import*

if __name__=="__main__":  # se, _name_ ou app for igual a main, ele irá iniciar #todo o codigo que estiver aqui dentro, ou seja, as janelas app. Só podem ser executado.
    app.run()