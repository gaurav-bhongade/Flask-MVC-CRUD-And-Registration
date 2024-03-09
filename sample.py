

# class Employee:
#     def __int__(self,eid,enm,eag,email,salary):
#         self.emp_id =eid
#         self.emp_name = enm
#         self.emp_eage = eag
#         self.epm_email = email
#         self.emp_salary = salary
#
#     def __str__(self):
#         return f'''\n {self.__dict__}'''
#
#     def __repr__(self):
#         return str(self)
#
# e1 = Employee(eid = 101,enm = 'AAAA',eag = 28,email = 'xyz@gmail.com',salary = 54000.00)

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root123@localhost/flask_db'
db = SQLAlchemy(app)

class Employee(db.Model):
    id = db.Column('emp_id',db.Integer(),primary_key=True)
    name = db.Column('emp_name',db.String(40))
    email = db.Column('emp_email',db.String(40),unique = True)
    salary = db.Column('emp_salary',db.Float())
    role = db.Column('emp_role',db.String(40))

#create Table
with app.app_context():
    db.create_all()


#insert
e1 = Employee(id = 101, name = 'AAAA', email = 'abc@gmail.com', salary = 54000.00, role = 'SSE')
with app.app_context():
    db.session.add(e1)
    db.session.commit()



#bulk insert
e2 = Employee(id = 102, name = 'AAAA1', email = 'abc1@gmail.com', salary = 54000.00, role = 'SSE')
e3 = Employee(id = 103, name = 'AAAA2', email = 'abc2@gmail.com', salary = 55000.00, role = 'SE')
e4 = Employee(id = 104, name = 'AAAA3', email = 'abc3@gmail.com', salary = 56000.00, role = 'Manager')
with app.app_context():
    db.session.add_all([e2,e3,e4])
    db.session.commit()

#select query
emp1 = Employee.query.filter_by(id=101).first()
print(emp1)

emplist = Employee.query.all()
print(emplist)

#delete
emp2 = Employee.query.filter_by(id=102).first()
if emp2:
    with app.app_context():
        db.session.delete(emp2)
        db.session.commit()

#update
emp3 = Employee.query.filter_by(id=103).first()
if emp3:
    emp3.name = 'Gaurav'
    with app.app_context():
        db.session.commit()



