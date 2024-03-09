from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.template_folder = 'pages/'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root123@localhost/flask_db'
db = SQLAlchemy(app)
