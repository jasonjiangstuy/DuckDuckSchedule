from flask import Flask, render_template, session, request
from flask_sock import Sock
from binascii import a2b_base64

app = Flask(__name__, static_folder='./static', template_folder='./templates')
app.config.update(TEMPLATES_AUTO_RELOAD=True)
sock = Sock(app)


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template(
        'index.html'
    )


@app.route('/scan', methods=['GET', 'POST'])
def scanner():
    return render_template(
        'scan.html'
    )


@sock.route('/scan_websocket')
def scan_websocket(sock):
    while True:
        image_data = sock.receive()
        print(type(image_data))

        print(str(image_data))
        print("Websocket Request")

        # tempbytes = imagehelper.get_as_base64
        with open("imageToSave.jpeg", "wb") as fh:
            import urllib
            response = urllib.request.urlopen(image_data)
            fh.write(response.file.read())
        fh.close()
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
