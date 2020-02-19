from flask import Blueprint, render_template, request, redirect, url_for

from .blueprint_services.words import *

test = Blueprint('test', __name__, template_folder='templates')



@test.route('/test')
def test_blueprint():
    open('static/simple_storage.txt', 'w').close()
    file = open('static/simple_storage.txt', 'w')
    words = get_words()
    file.write(str(words).strip('[]'))
    file.close()
    return render_template('test.html', words=words)