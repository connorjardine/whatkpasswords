from flask import Flask
from .blueprints.login import *


app = Flask(__name__)

app.register_blueprint(login)

if __name__ == "__main__":
    app.run()