from flask import Flask
from .blueprints.login import *
from .blueprints.authenticated import *
from .blueprints.registration import *
from .blueprints.test import *


app = Flask(__name__)

app.register_blueprint(login)
app.register_blueprint(authenticated)
app.register_blueprint(registration)
app.register_blueprint(test)

if __name__ == '__main__':
    app.debug = True
    app.run()