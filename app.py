from flask import Flask
from datetime import timedelta
from flask import request, session, jsonify



###### App setup
app = Flask(__name__)
app.config.from_pyfile('settings.py')



###### Pages
## Homepage
from pages.homepage.homepage import homepage
app.register_blueprint(homepage)

## About
from pages.aboutUs.aboutUs import aboutUs
app.register_blueprint(aboutUs)

from pages.ContactUs.ContactUs import ContactUs
app.register_blueprint(ContactUs)

## Catalog
from pages.TreatmentMenu.TreatmentMenu import TreatmentMenu
app.register_blueprint(TreatmentMenu)

from pages.signUp.signUp import signUp
app.register_blueprint(signUp)

from pages.paymentPage.paymentPage import paymentPage
app.register_blueprint(paymentPage)

from pages.chooseTreatment.chooseTreatment import chooseTreatment
app.register_blueprint(chooseTreatment)


from pages.membership.membership import membership
app.register_blueprint(membership)

from pages.myTreatments.myTreatments import myTreatments
app.register_blueprint(myTreatments)

from pages.userHomePage.userHomePage import userHomePage
app.register_blueprint(userHomePage)

from pages.userNotFound.userNotFound import userNotFound
app.register_blueprint(userNotFound)

from pages.updateYourDetails.updateYourDetails import updateYourDetails
app.register_blueprint(updateYourDetails)

## Page error handlers
from pages.page_error_handlers.page_error_handlers import page_error_handlers
app.register_blueprint(page_error_handlers)

###### Components
## Main menu
from components.main_menu.main_menu import main_menu
app.register_blueprint(main_menu)

from components.footer.footer import footer
app.register_blueprint(footer)