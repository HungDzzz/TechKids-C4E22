from flask import Flask, render_template,request, redirect, url_for
import mlab
from admin import Admin
app = Flask(__name__)

mlab.connect()

@app.route("/admin")
def admin():
    return render_template("admin.html")

@app.route("/admin/news", methods=['GET','POST'])
def news():
  if request.method == "GET":
    return render_template("news.html")
  elif request.method == "POST":
    form = request.form
    title = form['title']
    content = form['content']
    code = 'news'
    a = Admin(title=title, content=content, code= code)
    a.save()
    return redirect("/news_total")

@app.route("/admin/events", methods=['GET','POST'])
def events():
  if request.method == "GET":
    return render_template("events.html")
  elif request.method == "POST":
    form = request.form
    title = form['title']
    content = form['content']
    code = 'events'
    a = Admin(title=title, content=content, code=code)
    a.save()
    return redirect("/events_total")

@app.route("/news_total")
def news_total():
  news_list = Admin.objects(code='news')
  return render_template("news_total.html", news_total=news_list)

@app.route("/events_total")
def events_total():
  events_list = Admin.objects(code='events')
  return render_template("events_total.html", events_total=events_list)

if __name__ == '__main__':
  app.run(debug=True)