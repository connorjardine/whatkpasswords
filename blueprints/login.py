from flask import Blueprint, render_template, request
import random


login = Blueprint('login', __name__, template_folder='templates')


@login.route('/')
def login_blueprint():
    #TODO: get this data from user registration
    passwords = ['cat', 'dog', 'house', 'boat', 'golf', 'mike', 'hotel', 'sierra', 'tango', 'blue']
    random.shuffle(passwords)
    return render_template('login.html', pw=passwords)


@login.route('/submit_login', methods=["GET", "POST"])
def submit_user_login():
    if request.method == 'POST':
        #TODO: get this data from user registration
        correct_pw = ['cat', 'dog', 'house']
        a = request.form['code_zero']
        b = request.form['code_one']
        c = request.form['code_two']
        if a == correct_pw[0] and b == correct_pw[1] and c == correct_pw[2]:
            return "True"
        else:
            return "False"
