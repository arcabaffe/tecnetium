from aux import aux
from flask import Flask, request, render_template
 
app = Flask(__name__)  

@app.route('/', methods =["GET", "POST"])
def form():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == "POST":
       LOGO = request.form.get("LOGO")
       NAME = request.form.get("NAME")
       BIO = request.form.get("BIO")
       DESC = request.form.get("DESC")
       IMG0 = request.form.get("IMG0")
       IMG1 = request.form.get("IMG1")
       IMG2 = request.form.get("IMG2")
       IMG3 = request.form.get("IMG3")
       IMG4 = request.form.get("IMG4")
       IMG5 = request.form.get("IMG5")
       IMG6 = request.form.get("IMG6")
       IMG7 = request.form.get("IMG7")
       IMG8 = request.form.get("IMG8")
       SOCIAL1_NAME = request.form.get("SOCIAL1_NAME")
       SOCIAL1_LINK = request.form.get("SOCIAL1_LINK")
       SOCIAL2_NAME = request.form.get("SOCIAL2_NAME")
       SOCIAL2_LINK = request.form.get("SOCIAL2_LINK")
       SOCIAL3_NAME = request.form.get("SOCIAL3_NAME")
       SOCIAL3_LINK = request.form.get("SOCIAL3_LINK")
       SOCIAL4_NAME = request.form.get("SOCIAL4_NAME")
       SOCIAL4_LINK = request.form.get("SOCIAL4_LINK")
       LANG_INPUT = request.form['LANG']
       POLICE_INPUT = request.form['POLICE']
       BACKGROUND_INPUT = request.form['BACKGROUND']
       LOGO_NAME_PLACEMENT_INPUT = request.form['LOGO_NAME_PLACEMENT']
       IMG0_BIO_PLACEMENT_INPUT = request.form['IMG0_BIO_PLACEMENT']
       SOCIALS_PLACEMENT_INPUT = request.form['SOCIALS_PLACEMENT']
       aux(LOGO, NAME, BIO, DESC, IMG0, IMG1, IMG2, IMG3, IMG4, IMG5, IMG6, IMG7, IMG8, SOCIAL1_NAME, SOCIAL1_LINK, SOCIAL2_NAME, SOCIAL2_LINK, SOCIAL3_NAME, SOCIAL3_LINK, SOCIAL4_NAME, SOCIAL4_LINK, LANG_INPUT, POLICE_INPUT, BACKGROUND_INPUT, LOGO_NAME_PLACEMENT_INPUT, IMG0_BIO_PLACEMENT_INPUT, SOCIALS_PLACEMENT_INPUT)
       return render_template('confirmation.html')

import webbrowser
webbrowser.open('http://localhost:5000')
app.run(host='localhost', port=5000)