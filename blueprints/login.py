from flask import Blueprint, render_template, request, url_for

from .blueprint_services.word_colours import *


login = Blueprint('login', __name__, template_folder='templates')


@login.route('/')
def login_blueprint():
    file = open('static/simple_storage.txt', 'r')
    passwords = file.read().strip(' ')
    file.close()
    passwords = passwords.split()
    passwords = [i.strip(",") for i in passwords]
    passwords = [i.strip("'") for i in passwords]
    random.shuffle(passwords)
    passwords = colour_words(passwords)
    return render_template('login.html', pw=passwords)


@login.route('/submit_login', methods=["GET", "POST"])
def submit_user_login():
    if request.method == 'POST':
        file = open('static/passwords.txt', 'r')
        passwords = file.read().strip(' ')
        file.close()
        passwords = passwords.split()
        passwords = [i.strip(",") for i in passwords]
        correct_pw = [i.strip("'") for i in passwords]
        a = request.form['code_zero']
        b = request.form['code_one']
        c = request.form['code_two']
        if a == correct_pw[0] and b == correct_pw[1] and c == correct_pw[2]:
            return url_for('authenticated.authenticated_blueprint')
        else:
            return "False"
