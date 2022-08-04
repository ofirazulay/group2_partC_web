from flask import Blueprint, render_template

# userHomePage blueprint definition
userHomePage = Blueprint('userHomePage', __name__, static_folder='static', static_url_path='/userHomePage', template_folder='templates')


# Routes
@userHomePage.route('/userHomePage')
def index():
    return render_template('userHomePage.html')
