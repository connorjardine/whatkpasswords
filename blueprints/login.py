from flask import Blueprint, render_template

login = Blueprint('login', __name__)

passwords = ['cat', 'dog', 'house', 'boat', 'golf', 'mike', 'hotel', 'sierra', 'tango', 'blue']


@login.route('/')
def login_blueprint():
    return "whatkpasswords"
