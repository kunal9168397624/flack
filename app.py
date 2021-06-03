from flask import Flask,render_template,request,redirect,url_for

app = Flask(__name__,template_folder='template')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/joinus",methods=["GET","POST"])
def joinUs():
    if request.method == "POST":
        form = request.form["Email"]
        print(form)
        return redirect(url_for('home'))
    else:
        return render_template("join_us.html")

if __name__=='__main__':
    app.run(debug=True)