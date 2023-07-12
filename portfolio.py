from flask import Flask, render_template,request,request
import requests
from bs4 import BeautifulSoup
import requests
import datetime
from datetime import datetime
from flask_mail import Mail, Message
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from models import *
from flask_migrate import Migrate

# app name

app = Flask(__name__)

#db configuration
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///admin.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.app_context().push()
db.init_app(app)

migrate = Migrate(app, db)

#admin view
admin = Admin(app)
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Project, db.session))
admin.add_view(ModelView(Skill, db.session))
admin.add_view(ModelView(Service, db.session))
admin.add_view(ModelView(Education, db.session))
admin.add_view(ModelView(Contact, db.session))
admin.add_view(ModelView(Social, db.session))
admin.add_view(ModelView(Counter, db.session))
admin.add_view(ModelView(Testimonial, db.session))

# configure mail server
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'clintondeveloper6@gmail.com'
app.config['MAIL_PASSWORD'] = 'ahgcmnoykytzpqlm'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

# initialize mail server
mail = Mail(app)


@app.route('/send_email', methods=['POST'])
def send_email():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']

        with app.app_context():
            app.config['MAIL_DEFAULT_SENDER'] = (name, email)
            msg = Message(subject, recipients=['clintondeveloper6@gmail.com'], sender=email)
            msg.body = f"Name: {name}\nEmail: {email}\nMessage: {message}"

            success = 'Message sent successfully'
            mail.send(msg)

            return render_template('success.html', success=success)


# # home page
@app.route('/')
def index():

    # about me
    users = User.query.all()
    user = users[0]

    # skills
    skills = Skill.query.all()
    #services
    services = Service.query.all()
    #counter
    counters = Counter.query.all()
    #contact
    mycontacts = Contact.query.all()
    Contacts = mycontacts[0]
    sociallinks = Social.query.all()
    # testimonial
    Connfessions = Testimonial.query.all()
    Projects = Project.query.all()


    return render_template('index.html',
                           user=user,skills=skills,services=services,counters=counters,Contacts=Contacts,sociallinks=sociallinks,
                           Connfessions=Connfessions,Projects=Projects)


# project details
@app.route('/project_details')
def portfolio_details():
    return render_template('project_details.html')

# education details
@app.route('/education_details')
def education_details():
    #education
    myeducation = Education.query.all()
    return render_template('education.html', myeducation=myeducation)


# certifications
@app.route('/certifications')
def certifications():
     return render_template('certifications.html')

# main function

if __name__ == '__main__':
    app.run(debug=True)






