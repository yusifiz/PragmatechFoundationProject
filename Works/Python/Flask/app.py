from flask import Flask,render_template

app = Flask(__name__,template_folder='templates')

workers=[
    {
        'ad':'Yusif',
        'soyad':'Osmanov',
        'email':'osmanov.yusif@gmail.com'
    },
    {
        'ad':'Filankes',
        'soyad':'Filankesov',
        'email':"ff@gmail.com"
    }
]

@app.route("/")
def index():
    return render_template('index.html')
@app.route("/workers")
def worker():
    return render_template('workers.html',workers=workers)

@app.route("/contact")
def cont():
    return render_template('contact.html')

if __name__=="__main__":
    app.run(debug=True)