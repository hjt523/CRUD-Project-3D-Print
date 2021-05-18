from flask import Flask, redirect, render_template, request,url_for 
from flask_sqlalchemy import SQLAlchemy 
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
app = Flask(__name__) # create Flask object

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db" # Set the connection string to connect to the database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['SECRET_KEY'] = 'YAAAASSSSSSSSPRINT3D'

db = SQLAlchemy(app) # create SQLALchemy object

@app.route("/") # The first page people will see on my project
def index():

    return render_template("index.html")

@app.route("/current_projects") # A list of ongoing 3d Prints
def current_projects():

    return ""
@app.route("/add_project") # Add a new 3d print
def add_project():

    return ""
'''
@app.route("add_task") # Add a new task for a print / several prints
def add_task():
    return ""
@app.route("update_project") # Update existing prints
def up_project():
    return ""
@app.route("update_task") # Update existing tasks
def up_task():
    return ""
'''
# My Tables

class project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    description = db.Column(db.String(60), nullable = True)
    staatus = db.Column(db.Boolean, nullable=False, default=False)

class task(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30), nullable = False)
    details = db.Column(db.String(60), nullable = True)
    progress = db.Column(db.String(30), nullable = True, default = "Not Started") # Turn into drop down options?
    complete = db.Column(db.Boolean, nullable=False, default=False)

class jointable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, nullable = False)
    task_id = db.Column(db.Integer,nullable = False)

class projadd(FlaskForm):
    name = StringField("Project Name")
    description = StringField("Project Description ( optional)")
    submit = SubmitField("Submit")

class taskadd(FlaskForm):
    name = StringField("Task")
    details = StringField("Project Details ( optional)")
    submit = SubmitField("Submit")

if __name__=='__main__':
    app.run(debug=True)
