#setup server
from flask import Flask, render_template

app = Flask(__name__)# cho flask biet dang o vi tri o cung nao

@app.route("/")# neu ng dung truy cap trang chu thi goi ham ben duoi:
def homepage():
    return "Welcome to C4E Web module"

@app.route("/quan")
def hello_quan():
    return "hello quan"

@app.route("/praise/linh")
def praise_linh():
    return "hello linh"

@app.route("/praise/<name>")# bien la name dagt trong <>
def praise(name):
    return name + " is handsome"

@app.route("/add/<int:num1>/<int:num2>")
def add(num1, num2):
    return str(num1 + num2)

@app.route("/question")
def show_question():
    return render_template("question.html")

if __name__ == "__main__":
    app.run(debug=True) # debug khi sua code se reset server luon