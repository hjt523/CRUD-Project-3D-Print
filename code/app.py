from flask import Flask, redirect, render_template, request,url_for # Import Flask class
from flask_sqlalchemy import SQLAlchemy # Import SQLAlchemy class
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
app = Flask(__name__) # create Flask object

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db" # Set the connection string to connect to the database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['SECRET_KEY'] = 'edfghjkl'

db = SQLAlchemy(app) # create SQLALchemy object