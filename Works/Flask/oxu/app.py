from flask import Flask,redirect,url_for,render_template,request
import random
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///newsdb.db'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

db = SQLAlchemy(app)

class News(db.Model):
    news_id=db.Column(db.Integer, primary_key=True)
    news_title=db.Column(db.String(100))
    news_content=db.Column(db.Text)
    news_img=db.Column(db.String(100))

@app.route("/")
def index():
    nws = News.query.all()
    return render_template("index.html",nws=nws)
    
@app.route("/admin",methods=["GET","POST"])
def admin():
    nws = News.query.all()
    if request.method=='POST':
        file = request.files['news_img']
        filename = secure_filename(file.filename)
        randomName = random.randint(1,1000)
        filename = str(randomName)+ '.'  +filename.split('.')[1]
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        title=request.form["news_title"]
        content=request.form["news_content"]
        newss= News(
            news_title = title,
            news_content = content,
            news_img = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        )
        db.session.add(newss)
        db.session.commit()
        return redirect("/")
    return render_template("admin.html", nws=nws)

@app.route("/delete/<int:id>")
def delete(id):
    nws=News.query.filter_by(news_id=id).first()
    db.session.delete(nws)
    db.session.commit()
    return redirect("/admin")

@app.route("/update/<int:id>", methods=["GET","POST"])
def update(id):
    nws=News.query.filter_by(news_id=id).first()
    if request.method=="POST":
        nws=News.query.filter_by(news_id=id).first()
        nws.news_title=request.form['news_title']
        nws.news_content=request.form['news_content']
        db.session.commit()
        return redirect("/")
    return render_template("update.html", nws=nws)

@app.route("/show/<int:id>")
def show(id):
    nws=News.query.filter_by(news_id=id).first()
    if nws==id:

        return render_template("show.html",nws=nws)
    return render_template("show.html",nws=nws)

# db.create_all()
if __name__ == '__main__':
    app.run(debug=True)