from flask import Blueprint, render_template

login = Blueprint('login', __name__, template_folder='templates')



@login.route('/')
def login_blueprint():
    passwords = ['cat', 'dog', 'house', 'boat', 'golf', 'mike', 'hotel', 'sierra', 'tango', 'blue']
    return render_template('login.html', pw=passwords)

