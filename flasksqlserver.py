# pip install flask
# pip install flask-sqlalchemy
# pip install pyodbc
from flask import Flask
import urllib
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
# usuario root
# https://docs.sqlalchemy.org/en/14/dialects/mssql.html#sql-server-data-types
params = urllib.parse.quote_plus(
    'DRIVER={SQL Server};SERVER=EDUARDO-PC\SQLEXPRESS;DATABASE=pruebas;UID=usuario;PWD=root;Trusted_Connection=yes;')
app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc:///?odbc_connect=%s" % params
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


class Prueba(db.Model):
    __tablename__ = 't_prueba'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)


db.create_all()

app.run(debug=True)
