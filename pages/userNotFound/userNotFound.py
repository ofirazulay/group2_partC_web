from flask import Blueprint, render_template
from utilities.db.db_manager import dbManager

# userNotFound blueprint definition
userNotFound = Blueprint('userNotFound', __name__, static_folder='static', static_url_path='/userNotFound', template_folder='templates')


# Routes
@userNotFound.route('/userNotFound')
def index():
    return render_template('userNotFound.html')
