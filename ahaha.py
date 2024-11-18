from flask import Flask

apps = Flask(__name__)

from views import *
if __name__ == '__main__':
    apps.run()