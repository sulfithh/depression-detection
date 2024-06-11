from mad import app
from mad import db,app




from mad import db,app,login_manager
from flask_login import UserMixin
from flask_table import Table, Col, LinkCol
# from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

@login_manager.user_loader
def load_user(id):
    return registration.query.get(int(id))

class registration(db.Model, UserMixin):
    id=db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    lid = db.Column(db.String(80))
    address= db.Column(db.String (80))
    email= db.Column(db.String(80))
    number= db.Column(db.String (10))
    password = db.Column(db.String(80))
    usertype = db.Column(db.String(80))
    age = db.Column(db.String(80))
    gender = db.Column(db.String(80))
    dob = db.Column(db.String(80))
    Specialisation=db.Column(db.String(80))
    Qualification=db.Column(db.String(80)) 
    Image=db.Column(db.String(80))
    location=db.Column(db.String(80))
    hospital=db.Column(db.String(80))

    

class contact(db.Model, UserMixin):
    id=db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80)) 
    email= db.Column(db.String(80))
    number= db.Column(db.String (10))
    text= db.Column(db.String (80))


   


 





