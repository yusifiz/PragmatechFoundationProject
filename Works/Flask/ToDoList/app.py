import re
from flask import Flask,redirect,url_for,render_template,request
from flask_sqlalchemy import SQLAlchemy



app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(50))
    content=db.Column(db.Text)
    complete=db.Column(db.Boolean)

@app.route("/")
def index():
    todos = Todo.query.all()

    return render_template("index.html", todos=todos)

@app.route("/add",methods=["GET","POST"])
def addTodo():
    title=request.form.get("title")
    content=request.form.get("content")
    newTodo = Todo(title=title,content=content,complete = False)
    db.session.add(newTodo)
    db.session.commit()
    return redirect("/")

@app.route("/complete/<string:id>")
def complete(id):
    todo = Todo.query.filter_by(id=id).first()
    if (todo.complete == False):
        todo.complete = True
    else:
        todo.complete = False
    db.session.commit()
    return redirect("/")

@app.route("/delete/<string:id>")
def delete(id):
    todo = Todo.query.filter_by(id=id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect("/")
if __name__ == '__main__':
    app.run(port=5000,debug=True)
