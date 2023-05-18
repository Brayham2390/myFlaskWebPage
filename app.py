import gspread
from flask import Flask, render_template,request
from markupsafe import Markup
import datetime

current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

gc=gspread.service_account(filename='flask-profile.json')
sh=gc.open('flask-profile')
shProfile=sh.get_worksheet(0)
shContacts=sh.get_worksheet(1)


app=Flask(__name__)
@app.route('/',methods=['POST','GET'])
def home():
#    return "Hello World!!!-Comme Cà--"
    if request.method=='POST':
        shContacts.append_row([request.form['name'],request.form['email'],request.form['message'],current_time])

    
    profile = {
        'about':Markup(shProfile.acell('B1').value),
        'interests':Markup(shProfile.acell('B2').value),
        'experience':Markup(shProfile.acell('B3').value),
        'education':Markup(shProfile.acell('B4').value),
        'life1':Markup(shProfile.acell('B5').value),
        'life2':Markup(shProfile.acell('B6').value),
        'life3':Markup(shProfile.acell('B7').value),
        'life4':Markup(shProfile.acell('B8').value)

    }

    return render_template('index.html',profile=profile)

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)


 