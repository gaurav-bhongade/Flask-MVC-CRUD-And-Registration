from configuration import app, db
from flask import request, render_template
from models import Employee

@app.route('/')
@app.route('/employee')
@app.route('/employee/')
@app.route('/employee/index')
def welcome_page():
    return render_template('index.html')

@app.route('/employee/save', methods = ['GET','POST'])
def save_employee():
    # formdata = request.args
    # print(formdata)

    message = ''
    if request.method=='POST':
        formdata = request.form

        email = formdata.get('empemail')
        if len(email)<10:
            message = 'invalid email address'
            return render_template('add.html', error=message)

        print(formdata)

        emp = Employee(f_name=formdata.get('empfnm'),
                       m_name=formdata.get('empmnm'),
                       l_name=formdata.get('emplnm'),
                       gender=formdata.get('gender'),
                       age=formdata.get('empage'),
                       email=formdata.get('empemail'),
                       photo=formdata.get('empphoto'),
                       dob=formdata.get('empdob'))
        db.session.add(emp)
        db.session.commit()

        message = 'Employee Saved Successfully.....'
    return render_template('add.html',result = message)

@app.route('/emp/edit/<int:empid>')
def edit_employee(empid):
    emprecord = Employee.query.filter_by(id=empid).first()
    return render_template('update.html',employee = emprecord)

@app.route('/emp/delete/<int:empid>')
def delete_employee(empid):
    emprecord = Employee.query.filter_by(id=empid).first()
    if emprecord:
        db.session.delete(emprecord)
        db.session.commit()

    emp_list = Employee.query.all()
    return render_template('list.html', result_list=emp_list)

@app.route('/employee/update', methods = ['GET','POST'])
def update_employee():
    formdata = request.form
    empid = formdata.get('empid')
    emp = Employee.query.filter_by(id=empid).first()
    emp.f_name = formdata.get('empfnm')
    emp.m_name = formdata.get('empmnm')
    emp.l_name = formdata.get('emplnm')
    emp.gender = formdata.get('gender')
    emp.age = formdata.get('empage')
    emp.email = formdata.get('empemail')
    emp.photo = formdata.get('empphoto')
    emp.dob = formdata.get('empdob')
    db.session.commit()
    emp_list = Employee.query.all()
    return render_template('list.html', result_list=emp_list)

@app.route('/employee/list')
def list_of_employees():
    emp_list = Employee.query.all()
    return render_template('list.html',result_list = emp_list)

@app.route('/employee/photo' , methods = ['GET','POST'])
def upload_file():
    error = ''
    if request.method == 'POST':
        formdata = request.form   #html content
        name = formdata.get('emp_name')
        print('name',name)
        form_multimedia = request.files     #multimedia content
        print(form_multimedia)
        file = form_multimedia.get('emp_dp')
        print(file.filename)


        filename = file.filename
        if filename.split('.')[-1] in ['png','jpg','jpeg']:
            file.save(filename)
        else:
            error = 'Invalid file type'

        file.save(f"{name}.png")

    return render_template('upload_multimedia.html',error=error)

if __name__ == '__main__':
    app.run(debug=True)