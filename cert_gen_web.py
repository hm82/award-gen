from flask import Flask, redirect, url_for, render_template, request
from flask.helpers import send_from_directory 
from certificate_generator import Certificate

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
        event_name = request.form["e-nm"]
        event_date = request.form["e-dt"]
        return redirect(url_for("show_certificate", cert_user=user_name, e_name=event_name, e_dt=event_date))
    else:
        return render_template("cert_gen.html")

## Generate & Render certificate
@app.route("/show", methods=["POST", "GET"])
def show_certificate():
    # Get Input Parameters from request
    cert_user=request.args.get('cert_user')
    e_name=request.args.get('e_name')
    e_dt=request.args.get('e_dt')
    # construct the output filename
    cert_file = "certificate_"+cert_user+"_"+e_dt+".png"

    # Generate Certificate Based on Inputs
    cert_gen_sts = gen_certificate_image(user_name=cert_user, event_name=e_name, event_date=e_dt, event_cert_file=cert_file)
    if cert_gen_sts == True:
        return render_template("show_cert.html",user_name=cert_user, user_cert=cert_file)
    else:
        return f"<h1>Certificate for {cert_user} Not Found</h1>"
    
# Generate Certificate based on input parameters & Upload to Image directory
def gen_certificate_image(user_name, event_name, event_date, event_cert_file):
    ct = Certificate(user_name,event_name,event_date,"images/"+event_cert_file)
    ct_gen_sts = ct.create()
    if ct_gen_sts==1:
        print("\nSTATUS : SUCCESSFUL\n")
        return True
    else:
        print("\nSTATUS: FAILED\n")
        return False
 
# Download certificate from Server 
@app.route("/show/<cert_filename>")
def get_certs(cert_filename):
    return send_from_directory("images", cert_filename)   

if __name__== "__main__":
    app.run(debug=True)