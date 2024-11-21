from main import apps

@apps.views('/')
def homepage():
    return 'bosta'

@apps.views('/blog')
def homepage():
    return 'bem vindo'