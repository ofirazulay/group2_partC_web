from flask import Blueprint, render_template,request, session
from utilities.db.db_classes.classes_connector import user
from flask import flash

# signUp blueprint definition
signUp = Blueprint('signUp', __name__, static_folder='static', static_url_path='/signUp', template_folder='templates')


# Routes
@signUp.route('/signUp')
def index():
    return render_template('signUp.html')

@signUp.route('/add_new_user', methods=['POST'])
def add_new_user():
    user_name = request.form['full name']
    birthDate = request.form['birthDate']
    email = request.form['email']
    phone = request.form['phone']
    usrname = request.form['usrname']
    psw = request.form['psw']

    userAded = user.sign_in_fun( user_name, birthDate, email, phone, usrname, psw)
    if userAded =='email Exist':
        flash("User with the same email: " + email + " already Exist", 'error')
        return render_template('signUp.html')
    if userAded == 'userName Exist':
        flash("User with the same user-Name: " + usrname + " already Exist", 'error')
        return render_template('signUp.html')
    else:
        flash( user_name + " , your registration has been Successfully completed, please sign in", 'success')
    return render_template('homepage.html')




