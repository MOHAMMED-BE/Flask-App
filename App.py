# from crypt import methods
from distutils.log import debug
from email.policy import default
import json
from flask import Flask, redirect,render_template,url_for, request,flash
from flask_mysqldb import MySQL
from forms import RegistrationForm, LoginForm
from flask_wtf import FlaskForm
# import os


app = Flask(__name__)

app.config['SECRET_KEY'] = '9adda8bf738de307aea09ba4faebcb19140a6223'

data ={}

@app.route("/")
@app.route("/home")
def home():
    # filename = os.path.join(app.static_folder, 'data/data.json')
    with open("data/data.json","r") as file:
        data = json.load(file)

    return render_template("home.html", lessons=data['lessons'], courses=data['courses'])

@app.route("/about")
def about():
    return render_template("about.html", title="About")

@app.route("/register" , methods=['GET','POST'])
def registration():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created successfully for {form.lname.data} {form.fname.data}", 'success ')
        return redirect(url_for('home'))
    return render_template('register.html' , title='register', form = form , defaultpass= '&aA123456')

@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    return render_template('login.html' , title='login', form = form)


if __name__ == "__main__":
    app.run(debug=True)

 
# app.run(host='localhost', port=9000)



# lessons = [
#     {
#         "title": "Request Library Course",
#         "course": "Python",
#         "author": "Omar",
#         "thumbnail": "thumbnail.jpg",
#     },
#     {
#         "title": "Request Library Course",
#         "course": "Python",
#         "author": "Omar",
#         "thumbnail": "thumbnail.jpg",
#     },
#     {
#         "title": "Request Library Course",
#         "course": "Python",
#         "author": "Omar",
#         "thumbnail": "thumbnail.jpg",
#     },
#     {
#         "title": "Request Library Course",
#         "course": "Python",
#         "author": "Omar",
#         "thumbnail": "thumbnail.jpg",
#     },
#     {
#         "title": "Request Library Course",
#         "course": "Python",
#         "author": "Omar",
#         "thumbnail": "thumbnail.jpg",
#     },
#     {
#         "title": "Request Library Course",
#         "course": "Python",
#         "author": "Omar",
#         "thumbnail": "thumbnail.jpg",
#     },
# ]

# courses = [
#     {
#         "name": "Python",
#         "icon": "python.svg",
#         "description": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Neque quidem nihil dolor officiis at magni!",
#     },
#     {
#         "name": "Data Analysis",
#         "icon": "analysis.png",
#         "description": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Neque quidem nihil dolor officiis at magni!",
#     },
#     {
#         "name": "Machine Learning",
#         "icon": "machine-learning.png",
#         "description": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Neque quidem nihil dolor officiis at magni!",
#     },
#     {
#         "name": "Web Design",
#         "icon": "web.png",
#         "description": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Neque quidem nihil dolor officiis at magni!",
#     },
#     {
#         "name": "Blockchain",
#         "icon": "blockchain.png",
#         "description": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Neque quidem nihil dolor officiis at magni!",
#     },
#     {
#         "name": "Tips & Tricks",
#         "icon": "idea.png",
#         "description": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Neque quidem nihil dolor officiis at magni!",
#     },
# ]



"""
from distutils.log import debug
from flask import Flask,render_template, request
from flask_mysqldb import MySQL
 
app = Flask(__name__)
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flaskDB'
 
mysql = MySQL(app)

# #Creating a connection cursor
# with app.app_context():
#     cursor = mysql.connection.cursor()
 
# #Executing SQL Statements
# # cursor.execute('CREATE TABLE table_name(field1 int, field2 int)')
#     cursor.execute('INSERT INTO Test VALUES(1,"ZZ","DD")')
# # cursor.execute(' DELETE FROM table_name WHERE condition ')
 
# #Saving the Actions performed on the DB
#     mysql.connection.commit()
 
# #Closing the cursor
#     cursor.close()

@app.route('/form')
def form():
    return render_template('form.html')
 
@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'GET':
        return "Login via the login Form"
     
    if request.method == 'POST':
        id     = request.form['id']
        name   = request.form['name']
        prenom = request.form['prenom']
        
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO Test VALUES(%s,%s,%s)',(id,name,prenom))
        mysql.connection.commit()
        cursor.close()
        return f"Done!!"
 
app.run(host='localhost', port=5000)
"""




