from  configuration import db as ORM,app
from datetime import datetime
from sqlalchemy import  DateTime
class Employee(ORM.Model):
    __tablename__ = 'EMPLOYEE_MASTER'  #overrite table name
    id = ORM.Column('id',ORM.Integer,primary_key = True)
    f_name = ORM.Column('first_name', ORM.String(30))
    m_name = ORM.Column('middle_name', ORM.String(30))
    l_name = ORM.Column('last_name', ORM.String(30))
    gender = ORM.Column('gender', ORM.String(30))
    age = ORM.Column('age', ORM.Integer)
    email = ORM.Column('email', ORM.String(30))
    photo = ORM.Column('photo', ORM.String(30))
    dob = ORM.Column('dob', ORM.String(30))
    created_at = ORM.Column(DateTime, default=datetime.now)
    updated_at = ORM.Column(DateTime, default=datetime.now, onupdate=datetime.now)

print('Tables are created......')
with app.app_context():
    ORM.create_all()
