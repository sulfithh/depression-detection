from flask import Flask, render_template, request, redirect,  flash, abort, url_for
# from vadhyakalakshethra import app,db,bcrypt,mail
from mad import app
from mad import app
from mad.models import *
# from mad.forms import *
from flask_login import login_user, current_user, logout_user, login_required
from random import randint
import os
from PIL import Image
from flask_mail import Message
import pandas as pd
import pickle
import re
import nltk
from nltk.corpus import stopwords
from requests.structures import CaseInsensitiveDict
import json
import requests
import preprocessor as p

# model = pickle.load(open("model.pkl", "rb"))
# contractions = pd.read_json('contractions.json', typ='series')
# contractions = contractions.to_dict()

# c_re = re.compile('(%s)' % '|'.join(contractions.keys()))

# def expandContractions(text, c_re=c_re):
#     def replace(match):
#         return contractions[match.group(0)]
#     return c_re.sub(replace, text)

# BAD_SYMBOLS_RE = re.compile('[^0-9a-z _]')

# def clean_tweets(tweets):
#     cleaned_tweets = []
#     for tweet in tweets:
#         tweet = str(tweet)
#         tweet = tweet.lower()
#         tweet = expandContractions(tweet)
#         tweet = re.sub(r"http\S+", "", tweet)
#         tweet = re.sub(r"www.\S+", "", tweet)
#         tweet = BAD_SYMBOLS_RE.sub(' ', tweet)
#         tweet = re.sub('\[.*?\]',' ', tweet)
       
        
#         # temp = re.sub("@[A-Za-z0-9_]+","", temp)
#         # temp = re.sub("#[A-Za-z0-9_]+","", temp)
        

#         #remove punctuation
#         tweet = ' '.join(re.sub("([^0-9A-Za-z \t])", " ", tweet).split())

#         #stop words
#         stop_words = set(stopwords.words('english'))
#         word_tokens = nltk.word_tokenize(tweet) 
#         filtered_sentence = [w for w in word_tokens if not w in stop_words]
#         tweet = ' '.join(filtered_sentence)
        
#         cleaned_tweets.append(tweet)
        
#     return cleaned_tweets







@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/appointment')
def appointment():
    return render_template("appointment.html")




@app.route('/layout')
def layout():
    return render_template("layout.html")






@app.route('/patient_reg',methods=['GET','POST'])
def patient_reg():

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        address=request.form['address']
        gender=request.form['gender']
        age=request.form['age']
        number = request.form['number']
        password = request.form['password']
        # Qualification=request.form['Qualification']
        # confirm_password = request.form['confirm_password']
        my_data = registration(name=name,email=email,number=number,address=address,gender=gender,age=age,password=password,usertype="patient")
        db.session.add(my_data) 
        db.session.commit()
        # ad_sendmail(email,password)
        return redirect('/login')
    return render_template("patient_reg.html")


@app.route('/Dr_reg',methods=['GET','POST'])
def Dr_reg():

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        Specialisation=request.form['Specialisation']
        Qualification=request.form['Qualification']
        location = request.form['location']
        hospital = request.form['hospital']

        img=request.files['image']
        pic_file = save_picture(img)
        view = pic_file
        print(view) 


        # address=request.form['address']
        number = request.form['number']
        password = request.form['password']
        # confirm_password = request.form['confirm_password']
        my_data = registration(name=name,email=email,location=location,hospital=hospital,Image=view,number=number,Qualification=Qualification,Specialisation=Specialisation,password=password,usertype="Dr")
        db.session.add(my_data) 
        db.session.commit()
        # ad_sendmail(email,password)
        return redirect('/viewDr')
    return render_template("Dr_reg.html")  


@app.route('/editDr/<int:id>',methods=["GET","POST"])
def edit_Dr(id):
    c= registration.query.get_or_404(id)
    if request.method == 'POST':
        c.name =  request.form['name']
        # c.address =  request.form['address']
        c.email =  request.form['email']
        c.number =  request.form['number']
        c.Specialisation =  request.form['Specialisation']
        c.Qualification =  request.form['Qualification']
        # c.address =  request.form['address']

        db.session.commit()
        return redirect('/viewDr')
    else:
        return render_template('editDr.html',c=c)   


@login_required
@app.route('/viewDr',methods=["GET","POST"])
def viewDr():
    obj = registration.query.filter_by(usertype="Dr").all()
    return render_template("viewDr.html",obj=obj)    



@app.route('/delete_Dr/<int:id>', methods = ['GET','POST'])
def delete_Dr(id):

    delet = registration.query.get_or_404(id)
    try:
        db.session.delete(delet)
        db.session.commit()
        return redirect('/viewDr')
    except:
        return 'There was a problem deleting that task'


@app.route('/adminpage',methods=['GET', 'POST'])
def adminindex():
    return render_template("adminpage.html")

@app.route('/patient_page/<int:id>',methods=['GET', 'POST'])
def patient(id):
    return render_template("patient_page.html")




@app.route('/Dr_page/<int:id>',methods=['GET', 'POST'])
def Drpage(id):
    return render_template("Dr_page.html")


@login_required
@app.route('/sugg',methods=['GET', 'POST'])
def sugg():
    return render_template("sugg.html")



@login_required
@app.route('/yoga',methods=['GET', 'POST'])
def yoga():
    return render_template("yoga.html")


@login_required
@app.route('/workout',methods=['GET', 'POST'])
def workout():
    return render_template("workout.html")



@login_required
@app.route('/music',methods=['GET', 'POST'])
def music():
    return render_template("music.html")


@login_required
@app.route('/diet',methods=['GET', 'POST'])
def diet():
    return render_template("diet.html")


@login_required
@app.route('/tamil',methods=['GET', 'POST'])
def tamil():
    return render_template("tamil.html")

@login_required
@app.route('/mal',methods=['GET', 'POST'])
def mal():
    return render_template("mal.html")


@login_required
@app.route('/hin',methods=['GET', 'POST'])
def hin():
    return render_template("hin.html")



@login_required
@app.route('/eng',methods=['GET', 'POST'])
def eng():
    return render_template("eng.html")

def save_picture(form_picture):
    random_hex = random_with_N_digits(14)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = str(random_hex) + f_ext
    picture_path = os.path.join(app.root_path, 'static/pics', picture_fn)
    
    output_size = (500, 500)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn




def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)


@login_required
@app.route('/patientview_Dr',methods=["GET","POST"])
def patientview_Dr():
    search=request.args.get('search')
    if search:
        obj=registration.query.filter((registration.location.contains(search)| registration.name.contains(search) | registration.hospital.contains(search))  & registration.usertype.contains("Dr") )
    else:
        obj = registration.query.filter_by(usertype="Dr").all()
    
    return render_template("patient view_Dr.html",obj=obj)    



@login_required
@app.route('/viewpatient',methods=["GET","POST"])
def viewpatient():
    obj = registration.query.filter_by(usertype="patient").all()
    return render_template("viewpatient.html",obj=obj)  



@app.route('/feedback',methods=['GET','POST'])
def feedback():
    f=registration.query.filter_by(id=current_user.id).first()
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        number = request.form['number']
        text = request.form['text']
        my_data = contact(name=name,email=email,number=number,text=text)
        db.session.add(my_data) 
        db.session.commit()
        d="Message Sent Successfully"
        return render_template("feedback.html",d=d,f=f)
    return render_template("feedback.html",f=f)



@login_required
@app.route('/feedbackview',methods=["GET","POST"])
def feedbackview():
    obj = contact.query.all()
    return render_template("feedbackview.html",obj=obj)

@login_required
@app.route('/feedbackview_dr',methods=["GET","POST"])
def feedbackviewdr():
    obj = contact.query.all()
    return render_template("feedbackview_dr.html",obj=obj)







@app.route('/login', methods=["GET","POST"])
def login():

   
    if request.method=="POST":


        username=request.form['email']
        password=request.form['password']
        admin = registration.query.filter_by(email=username, password=password,usertype='admin').first()
        patient=registration.query.filter_by(email=username,password=password,usertype='patient').first()
        # Dr=registration.query.filter_by(email=username,password=password, usertype='Dr').first()

        if admin:
            login_user(admin)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect('/adminpage') 
         
     

        elif patient:

            login_user(patient)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect('/patient_page/'+str(patient.id)) 

        # elif Dr:

        #     login_user(Dr)
        #     next_page = request.args.get('next')
        #     return redirect(next_page) if next_page else redirect('/Dr_page/'+str(Dr.id))          

        else:

            d="Invalid Username or Password!"
            return render_template("login.html",d=d)
    return render_template("login.html")



@login_required
@app.route("/logout")
def logout():
    logout_user()
    return redirect('/')

  




