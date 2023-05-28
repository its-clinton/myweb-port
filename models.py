from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable = False)
    profile = db.Column(db.String(50), nullable = False)
    email = db.Column(db.String(50), nullable = False)
    phonenumber = db.Column(db.String(50), nullable = False)
    profile_image = db.Column(db.String(100))
 
class Project(db.Model):
    __tablename__ = 'projects'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(50), nullable = False)
    description = db.Column(db.String(50), nullable = False)
    type = db.Column(db.String(50), nullable = False)

    
class Skill(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(50), nullable = False)

    
class Service(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(50), nullable = False)
    description = db.Column(db.String(50), nullable = False)
  

    
class Education(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    institution = db.Column(db.String(50), nullable = False)
    course = db.Column(db.String(50), nullable = False)
    year_range = db.Column(db.String(50), nullable = False)
    grade = db.Column(db.String(50), nullable = False)
    
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    location = db.Column(db.String(50), nullable = False)
    phonenumber = db.Column(db.String(50), nullable = False)
    email = db.Column(db.String(50), nullable = False)
    

class Social(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(50), nullable = False)  
    link = db.Column(db.String(50), nullable = False)
    
    
class Counter(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(50), nullable = False)
    count = db.Column(db.Integer, nullable = False)
    
class Testimonial(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable = False)
    testimonial = db.Column(db.Text, nullable = False)




