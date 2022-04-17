from flask import Flask, render_template, session, request
app = Flask(__name__, static_folder='./static', template_folder='./templates')

app.config.update(TEMPLATES_AUTO_RELOAD=True)

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
@app.route('/personality_quiz', methods=['GET', 'POST'])
def quiz():
    if (request.method == 'POST'):
      
      pass
    return render_template(
      'quiz.html'
    )
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='3000')

#useful modules
#picking -> method of database storage: can preserve classes
#www.MYURL/showcase.com#isFake?=True