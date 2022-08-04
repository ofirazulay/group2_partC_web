from flask import Blueprint,request, render_template,session,redirect
from utilities.db.db_classes.classes_connector import treatments
chooseTreatment = Blueprint('chooseTreatment', __name__, static_folder='static', static_url_path='/chooseTreatment', template_folder='templates')
from flask import  flash


@chooseTreatment.route('/chooseTreatment')
def index():
    return render_template('chooseTreatment.html')

@chooseTreatment.route('/filteredTreatment', methods=['POST'])
def filteredTreatment():
    email = session['userEmail']
    treatmemtType = session['type']
    print(session['type'])
    branch = request.form['branch']
    day = request.form['day']
    if branch == 'All':
        branch= '%'
    if day == 'All':
        day= '%'
    availableSlots = treatments.filteredSlots(treatmemtType, branch, day)
    print(availableSlots)
    return render_template('chooseTreatment.html', availableSlots=availableSlots)


@chooseTreatment.route('/orderNewTreatment', methods=['POST'])
def orderTreatment_func():
    dateToOrder = request.form['dateToOrder']
    dayToOrder = request.form['dayToOrder']
    hourToOrder = request.form['hourToOrder']
    branchToOrder = request.form['branchToOrder']
    TetapistToOrder = request.form['TetapistToOrder']

    orderTreatment=treatments.orderTreatment(session['type'], dateToOrder, hourToOrder, TetapistToOrder,branchToOrder)
    if orderTreatment:
        flash("The " + session['type']+ " treatment has been successfully scheduled and added to your treatments list ", 'success')
        return redirect('/myTreatments')
    else:
        flash("You have no tickets left for this treatment, tickets must be purchased", 'error')
        return redirect('/myTreatments')


