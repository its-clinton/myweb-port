
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
app = Flask(__name__)
from flask_admin.contrib.sqla import ModelView
from flask import current_app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.sqlite3'
app.config['SECRET_KEY'] = 'mysecret'

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
    type = db.Column(db.String(50), nullable = False)

    def __init__(self, title, description,type):
        self.title = title
        self.description = description
        type = type

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

class Social(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(50), nullable = False)  
    link = db.Column(db.String(50), nullable = False)
    
    def __init__(self, title, link):
        self.title = title
        self.link = link
        
    def __repr__(self):
        return '<Title %r>' % self.title
    
class Counter(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(50), nullable = False)
    count = db.Column(db.Integer, nullable = False)
    
    def __init__(self, title, count):
        self.title = title
        self.count = count
        
    def __repr__(self):
        return '<Title %r>' % self.title
    
class Testimonial(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable = False)
    testimonial = db.Column(db.Text, nullable = False)
    
    def __init__(self, name, title,testimonial):
        self.name = name
        self.title = title
        self.testimonial = testimonial
        
    def __repr__(self):
        return '<Title %r>' % self.name
    
    
# if __name__ == '__main__':
#     with app.app_context():
#       db.create_all()
#       db.session.commit()
#       db.session.close()
  