from flask import Blueprint, render_template
from utilities.db.db_classes.classes_connector import treatmentsManue

# TreatmentMenu blueprint definition
TreatmentMenu = Blueprint('TreatmentMenu', __name__, static_folder='static', static_url_path='/TreatmentMenu', template_folder='templates')


# Routes
@TreatmentMenu.route('/TreatmentMenu')
def index():
    treatmentsDetails = treatmentsManue.getTreatmentsMenu_Details()
    return render_template('TreatmentMenu.html',treatmentsDetails=treatmentsDetails)
