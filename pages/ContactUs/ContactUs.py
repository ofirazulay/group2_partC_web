from flask import Blueprint, render_template,request, session
from utilities.db.db_classes.classes_connector import contact
from flask import flash
import datetime

# ContactUs blueprint definition
ContactUs = Blueprint('ContactUs', __name__, static_folder='static', static_url_path='/ContactUs', template_folder='templates')


# Routes
@ContactUs.route('/ContactUs')
def index():
    return render_template('ContactUs.html')

@ContactUs.route('/add_contact_Data', methods=['POST'])
def add_contact_Data():
        full_name=request.form['Full name']
        email = request.form['email']
        phone_number = request.form['phone']
        review = request.form['freeTextContact']
        now = datetime.datetime.now()
        contactAdded=contact.Add_contact(full_name,email,phone_number,review,now)
        flash(full_name + ", your request sent succssesfully! our agents will call you back ASAP ", 'success')
        return render_template('homepage.html')