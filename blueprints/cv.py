from flask import Blueprint, render_template

cv_app = Blueprint('cv_app', __name__)

@cv_app.route('/cv')
def cv():
    return render_template ('cv.jinja')

@cv_app.route('/cv/exp1')
def cv_exp1():
    return render_template ('exp1.jinja')

@cv_app.route('/cv/exp2')
def cv_exp2():
    return render_template ('exp2.jinja')
