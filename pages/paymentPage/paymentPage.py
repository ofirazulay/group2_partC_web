from flask import Blueprint, render_template, request, session, redirect
from utilities.db.db_classes.classes_connector import payment
from flask import flash

# paymentPage blueprint definition
paymentPage = Blueprint('paymentPage', __name__, static_folder='static', static_url_path='/paymentPage', template_folder='templates')


# Routes
@paymentPage.route('/paymentPage')
def index():
    return render_template('paymentPage.html')

@paymentPage.route('/add_new_payment', methods=['POST'])
def add_new_user():
    print(request.form['fname'])
    fullname = request.form['fname']
    email = request.form['email']
    address = request.form['address']
    city = request.form['city']
    zip = request.form['zip']
    cardname = request.form['cardname']
    cardnumber = request.form['cardnumber']
    expmonth = request.form['expmonth']
    expyear = request.form['expyear']
    cvv = request.form['cvv']
    print("UNTIL HERE")
    payment.new_payment_fun( fullname, email ,address, city, zip, cardname, cardnumber, expmonth, expyear, cvv)
    flash(fullname + " your payment has been done succssesfully ", 'success')
    return redirect('/membership')

@paymentPage.route('/back_to_home', methods=['POST'])
def move_to_user_homepage():
    return render_template('userHomePage.html')