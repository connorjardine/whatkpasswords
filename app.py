from flask import Flask
from .blueprints.login import *
from .blueprints.authenticated import *


app = Flask(__name__)

app.register_blueprint(login)
app.register_blueprint(authenticated)


if __name__ == "__main__":
    app.run()