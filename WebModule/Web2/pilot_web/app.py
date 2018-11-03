from flask import Flask, render_template, request
import mlab
from random import choice
from poll import Poll

app = Flask(__name__)

mlab.connect()

@app.route('/')
def home():
    return render_template("home.html")


@app.route("/poll/<poll_code>")
def poll(poll_code):
  # 1. get poll
  poll_list = Poll.objects(code=poll_code) # filter : loc ra cai minh can
  poll = poll_list[0]
  # print(poll.question)
  # print(poll.options)

  # BTVN : object(yob__gt=1990) gt : lon hon, lt : nho hon

  # 2. render 
  return render_template("poll.html", p=poll)

@app.route('/polls')
def polls():
  # 1. read all polls
  poll_list = Poll.objects()

  # for p in poll_list:
  #   print(p.question)


  # 2. render all polls
  return render_template("polls.html", polls = poll_list)


@app.route("/new_poll", methods=['GET','POST']) # methods de nhan ca post neu k chi nhan get
def new_poll():
  if request.method == "GET":
    return render_template("new_poll.html")
  elif request.method == "POST":
    # 1. Unpack data(form)
    form = request.form
    question = form['question']
    option = []
    for k,v in form.items():
      if k != 'question':
        option.append(v)
    #print(question)
    #print(option)
    alphabet = 'abcdefghijklmnopqrstuvwxyz'.upper()
    code = ""
    for _ in range(6):
        code += choice(alphabet)
    p = Poll(question=question, options=option, code= code)
    p.save()
    return "Gotcha"

if __name__ == '__main__':
  app.run(debug=True)