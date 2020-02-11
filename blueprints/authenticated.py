from flask import Blueprint, render_template

authenticated = Blueprint('authenticated', __name__, template_folder='templates')


@authenticated.route('/authenticated/auth', methods=['GET', 'POST'])
def authenticated_blueprint():
    print("here")
    return render_template('authenticated.html')


