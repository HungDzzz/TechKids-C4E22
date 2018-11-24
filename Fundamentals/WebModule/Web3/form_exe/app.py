from flask import Flask, render_template, request
import mlab
from form import Form
app = Flask(__name__)

mlab.connect()

@app.route("/")
def homepage():
    return 'Welcome'

@app.route("/register", methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template("register.html")
    elif request.method == 'POST':
        form = request.form
        firstname = form['firstname']
        lastname = form['lastname']
        email = form['email']
        yob = form['yob']
        gender = form['gender']
        city = form['city']
        #print(firstname,lastname,email,yob,gender,city, sep= ' : ')
        F = Form(firstname=firstname, lastname= lastname, email= email, yob=yob, gender= gender,city=city)
        F.save()
    return 'Gotcha'


if __name__ == '__main__':
  app.run(debug=True)