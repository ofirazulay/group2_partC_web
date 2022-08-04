from flask import Blueprint,request, render_template,session,redirect
from utilities.db.db_classes.classes_connector import treatments
# myTreatments blueprint definition
from flask import  flash


myTreatments = Blueprint('myTreatments', __name__, static_folder='static', static_url_path='/myTreatments', template_folder='templates')


# Routes
@myTreatments.route('/myTreatments')
def index():
    email = session['userEmail']
    UsertreatmentsList = treatments.searchTreatments(email)
    return render_template('myTreatments.html', UsertreatmentsList=UsertreatmentsList)


@myTreatments.route('/orderTreatment', methods=['POST'])
def orderTreatment():
    email = session['userEmail']
    UsertreatmentsList = treatments.searchTreatments(email)
    session['type'] = request.form['Choosekind']
    treatment_Type= request.form['Choosekind']
    availableSlots= treatments.availableSlots(treatment_Type)
    return render_template('chooseTreatment.html', availableSlots=availableSlots,UsertreatmentsList=UsertreatmentsList)

@myTreatments.route('/deleteTreatment', methods=['POST'])
def deleteTreatment():
    dateToDelete = request.form['dateToDelete']
    dayToDelete = request.form['dayToDelete']
    hourToDelete = request.form['hourToDelete']
    branchToDelete = request.form['branchToDelete']
    TetapistToDelete = request.form['TetapistToDelete']
    deletedTreatment = treatments.deletedTreatment(dateToDelete, dayToDelete,hourToDelete, TetapistToDelete,
                                               branchToDelete)
    flash(
            "The  treatment has been successfully Deleted ",
            'success')
    return redirect('/myTreatments')







