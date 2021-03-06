# from crypt import methods
from distutils.log import debug
from email.policy import default
import json
import MySQLdb
from colorama import Cursor
from flask import Flask, redirect,render_template,url_for, request,flash
from flask_mysqldb import MySQL
from classes.dotDict import dotdict
from forms import LoginForm, RegistrationForm
from flask_wtf import FlaskForm
# import os



app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '' #nfakira
app.config['MYSQL_DB'] = 'FlaskAppDB'
 
mysql = MySQL(app)


app.config['SECRET_KEY'] = '9adda8bf738de307aea09ba4faebcb19140a6223'

data ={}

def get_results(db_cursor):
    desc = [d[0] for d in db_cursor.description]
    results = [dotdict(dict(zip(desc, res))) for res in db_cursor.fetchall()]
    return results

# -----------------------------------------------------------------
# -- home                                                    --
# -----------------------------------------------------------------

@app.route("/")
@app.route("/home")
def home():
    # filename = os.path.join(app.static_folder, 'data/data.json')
    with open("data/data.json","r") as file:
        data = json.load(file)

    cursor = mysql.connection.cursor()
    cursor.execute('select * from courses')
    courses = get_results(cursor)
    # courses = cursor.fetchall()
    cursor.close()
    cursor = mysql.connection.cursor()
    cursor.execute('select * from lessons')
    lessons = get_results(cursor)
    # lessons = cursor.fetchall()
    cursor.close()

    return render_template("home.html", lessons=lessons, courses=courses)

@app.route("/about")
def about():
    return render_template("about.html", title="About")

# -----------------------------------------------------------------
# -- register                                                    --
# -----------------------------------------------------------------

@app.route("/register" , methods=['GET','POST'])
def registration():
    form = RegistrationForm()
    return render_template('register.html' , title='register', form = form )

# -----------------------------------------------------------------
# -- login                                                    --
# -----------------------------------------------------------------

@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email     = request.form['email']
        password  = request.form['password']
        
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM users WHERE email = %s AND password = %s', (email, password,))
        # user = get_results(cursor)
        user = cursor.fetchone()

        cursor.close()

        if form.validate_on_submit():
            if user:
                flash(f"user {user['username']} connected",'success')
            else:
                flash(f"email or password not correct",'danger')

    return render_template('login.html' , title='login', form = form)


# -----------------------------------------------------------------
# -- insert                                                    --
# -----------------------------------------------------------------

@app.route("/insert" , methods=['POST'])
def insert():
    form = RegistrationForm()
    if request.method == 'POST':
        fname     = request.form['fname']
        lname     = request.form['lname']
        username  = request.form['username']
        email     = request.form['email']
        password  = request.form['password']
        
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO users VALUES(%s,%s,%s,%s,%s)',(fname,lname,username,email,password))
        mysql.connection.commit()
        cursor.close()
    if form.validate_on_submit():
        flash(f"user created successfully",'success')
        return redirect(url_for('registration'))


# -----------------------------------------------------------------
# -- sign in                                                    --
# -----------------------------------------------------------------

# @app.route("/select" , methods=['POST'])
# def select():
#     form = LoginForm()
#     if request.method == 'POST':
#         email     = request.form['email']
#         # password  = request.form['password']
        
#         cursor = mysql.connection.cursor()
#         cursor.execute(f"select * from users where email='{email}'")
#         # user = get_results(cursor)
#         user = cursor.fetchall()

#         cursor.close()

#     # if form.validate_on_submit():
#     if user[3] == email: # and user.password == password
#         flash(f"user connected")
    #     return redirect(url_for('login'))
    # else:
    #     flash(f"not connected")
    # return render_template('login.html' , title='login', form = form)











if __name__ == "__main__":
    app.run(debug=True)

 
# app.run(host='localhost', port=9000)





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



