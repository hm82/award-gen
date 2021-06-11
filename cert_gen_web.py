from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

## Load flask App configurations / env variables
app.config.from_object('config.DevelopmentConfig')

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/certs",methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user_name = request.form["f-nm"]+" "+request.form["l-nm"]
        return redirect(url_for("user", usr=user_name))
    else:
        return render_template("cert_gen.html")


## Insert logic for generating certificate and embedding it on the page here
@app.route("/<usr>")
def user(usr):
    return f"<h1>Welcome {usr}</h1>"

if __name__== "__main__":
    app.run(debug=True)
