from random import random
from flask import Flask, flash,render_template, session, request, redirect
from flask_sock import Sock
import random
import urllib
import json
import requests
from pythonhelpers import imagehelping
from os.path import exists
app = Flask(__name__, static_folder='./static', template_folder='./templates')
app.config.update(TEMPLATES_AUTO_RELOAD=True)
sock = Sock(app)
app.secret_key = 'the random string'

database = r"C:\sqlite\db\pythonsqlite.db"
import myapi

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template(
        'index.html'
    )

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method== "POST":
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)

        file = request.files['file']
        print(file.filename)
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        name = request.form.get['Name']
        # images/" + name
        file.save("images/" + name)
        print(name)
        myapi.RegisterFace(name, file.read())
        # ADD students profiles
    db = json.loads(myapi.viewDB())
    return render_template('admin.html', db=db)

@app.route('/scan', methods=['GET', 'POST'])
def scanner():
    return render_template(
        'scan.html'
    )

@sock.route('/scan_websocket')
def scan_websocket(sock):
    while True:
        image_data = sock.receive()
        # save image as a random filename for 
        filename = 0
        while exists("temp_web_images/"+str(filename)+".jpeg"):
            filename = random.randint(0, 1000)
        with open("temp_web_images/"+str(filename)+".jpeg", "wb") as fh:
            response = urllib.request.urlopen(image_data)
            fh.write(response.file.read())
        fh.close()
        filename = "temp_web_images/"+str(filename)+".jpeg"
        imagehelping.getImageData(filename)

        sock.send("200")


@app.route('/personality_quiz', methods=['GET', 'POST'])
def quiz():
    if (request.method == 'POST'):

        pass
    return render_template(
        'quiz.html'
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='3000')

# useful modules
# picking -> method of database storage: can preserve classes
# www.MYURL/showcase.com#isFake?=True
