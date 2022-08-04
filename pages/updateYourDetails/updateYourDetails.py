from datetime import timedelta
from flask import Blueprint, render_template, session, Flask
from flask import request, flash
from utilities.db.db_classes.classes_connector import user

updateYourDetails = Flask(__name__)
# updateYourDetails.register_blueprint(user)
updateYourDetails.secret_key = '123'
updateYourDetails.config['SESSION_PERMANENT'] = True
updateYourDetails.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=5)

# updateYourDetails blueprint definition


updateYourDetails = Blueprint('updateYourDetails', __name__, static_folder='static', static_url_path='/updateYourDetails', template_folder='templates')




# Routes
@updateYourDetails.route('/updateYourDetails')
def index():
    return render_template('updateYourDetails.html')

@updateYourDetails.route('/update_user', methods=['POST'])
def update_user():
    userEmail = request.form['email']

    fullname = request.form['full name']
    phone = request.form['phone']
    psw = request.form['psw']
    session['username'] = fullname
    updatedUser = user.update_user(userEmail,fullname,phone,psw)
    flash("your details updateded", 'success')
    return render_template('userHomePage.html')
