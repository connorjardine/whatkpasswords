from flask import Blueprint, render_template, request, redirect, url_for

from .blueprint_services.words import *

registration = Blueprint('registration', __name__, template_folder='templates')


@registration.route('/register')
def registration_blueprint():
    open('static/simple_storage.txt', 'w').close()
    file = open('static/simple_storage.txt', 'w')
    words = get_words()
    print(words)
    file.write(str(words).strip('[]'))
    return render_template('registration.html', words=words)


@registration.route('/submit_registration', methods=["GET", "POST"])
def submit_user_registration():
    print("hello")
    if request.method == 'POST':
        a = request.form['code_zero']
        b = request.form['code_one']
        c = request.form['code_two']
        file = open('static/passwords.txt', 'w')
        file.write(str([a, b, c]).strip('[]'))
    return url_for('login.login_blueprint')
