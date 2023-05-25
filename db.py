# a database - the the database will store my details, my projects,my skills,my projects,my services,my education,my contact details,my social media links,counter section details, testimonial details
# using sql alchemy
# create a database

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable = False)
    profile = db.Column(db.String(50), nullable = False)
    email = db.Column(db.String(50), nullable = False)
    phonenumber = db.Column(db.String(50), nullable = False)
 

    def __init__(self, name, profile, email, phonenumber):
        self.name = name
        self.profile = profile
        self.email = email
        self.phonenumber = phonenumber
       
    def __repr__(self):
        return '<Name %r>' % self.name
    
class Project(db.Model):
    __tablename__ = 'projects'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(50), nullable = False)
    description = db.Column(db.String(50), nullable = False)
    image = db.Column(db.String(50), nullable = False)
    type = db.Column(db.String(50), nullable = False)
    date_created = db.Column(db.DateTime, default = datetime.utcnow)

    def __init__(self, title, description, image,type, date_created):
        self.title = title
        self.description = description
        self.image = image
        type = type
        self.date_created = date_created

    def __repr__(self):
        return '<Title %r>' % self.title
    
class Skill(db.Model):
    __tablename__ = 'skills'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(50), nullable = False)

    def __init__(self, title):
        self.title = title
       

    def __repr__(self):
        return '<Title %r>' % self.title
    
class Service(db.Model):
    __tablename__ = 'services'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(50), nullable = False)
    description = db.Column(db.String(50), nullable = False)
  
    def __init__(self, title, description):
        self.title = title
        self.description = description
    
    def __repr__(self):
        return '<Title %r>' % self.title

    
class Education(db.Model):
    __tablename__ = 'educations'
    id = db.Column(db.Integer, primary_key = True)
    institution = db.Column(db.String(50), nullable = False)
    course = db.Column(db.String(50), nullable = False)
    year_range = db.Column(db.String(50), nullable = False)
    grade = db.Column(db.String(50), nullable = False)
    

    def __init__(self, institution, course, year_range, grade):
        self.institution = institution
        self.course = course
        self.year_range = year_range
        self.grade = grade

    def __repr__(self):
        return '<Title %r>' % self.institution
    
    
class Contact(db.Model):
    __tablename__ = 'contacts'
    id = db.Column(db.Integer, primary_key = True)
    location = db.Column(db.String(50), nullable = False)
    phonenumber = db.Column(db.String(50), nullable = False)
    email = db.Column(db.String(50), nullable = False)
    

    def __init__(self, location, phonenumber, email):
        self.location = location
        self.phonenumber = phonenumber
        self.email = email
        
    def __repr__(self):
        return '<Title %r>' % self.email

# create the database for the models
def create_db(app):
    db.init_app(app)
    db.create_all(app = app)
    print('Database created')

if __name__ == '__main__':
    create_db(app)

    

    
    