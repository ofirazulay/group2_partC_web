from flask import Blueprint, render_template,session, request
from utilities.db.db_classes.classes_connector import membershipCard

# membership blueprint definition
membership = Blueprint('membership', __name__, static_folder='static', static_url_path='/membership', template_folder='templates')


# Routes
@membership.route('/membership')
def index():
    email = session['userEmail']
    membership_card = membershipCard.membership_card(email)
    return render_template('membership.html', membership_card=membership_card)

@membership.route('/moveToPayment', methods=['POST'])
def moveToPayment():
    session['numOfShiazu'] = request.form['streatment']
    session['numOfReflexology'] = request.form['rtreatment']
    session['numOfChinese'] = request.form['ctreatment']

    session['price'] = membershipCard.calculateFullPrice()
    return render_template('paymentPage.html')


