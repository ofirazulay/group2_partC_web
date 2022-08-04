from flask import Blueprint, render_template, redirect, url_for
from flask import request, session, jsonify

from utilities.db.db_classes.classes_connector import user


# main_menu blueprint definition
main_menu = Blueprint('main_menu', __name__, static_folder='static', static_url_path='/main_menu', template_folder='templates')

@main_menu.route('/homepage')
def home_page():
    return render_template('homepage.html')

@main_menu.route('/aboutUs')
def about_us_page():
    return render_template('aboutUs.html')

@main_menu.route('/ContactUs')
def ContactUs():
    return render_template('ContactUs.html')

@main_menu.route('/TreatmentMenu')
def TreatmentMenu():
    return render_template('TreatmentMenu.html')

# Routes
@main_menu.route('/updateYourDetails')
def updateuser():
    return render_template('updateYourDetails.html')

@main_menu.route('/signUp')
def signUp():
    return render_template('signUp.html')

@main_menu.route('/userHomePage', methods=['POST'])
def signIn_page():
    if request.method == 'POST':
        userEmail=request.form['uemail']
        userPassword = request.form['psw']
        returndUser=user.login(userEmail,userPassword)
        if returndUser!='notFound':
            session['username'] = returndUser[0]
            session['userEmail'] = userEmail
            session['registered'] = True
            session['notFound'] = False
            return render_template('userHomePage.html')
        else:
            session['notFound'] = True
            return render_template('userNotFound.html')

@main_menu.route('/log_out')
def logout_func():
    session['registered'] = False
    session.clear()
    return redirect('/homepage')