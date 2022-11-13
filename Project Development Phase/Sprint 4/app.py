from flask import *

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('welcome.html')

@app.route('/registration')
def registration():
    return render_template('registration.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/base')
def base():
    return render_template('base.html')

@app.route('/display')
def display():
    return render_template('display.html')

@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/expensechart')
def expensechart():
    return render_template('expensechart.html')

@app.route('/limit')
def limit():
    return render_template('limit.html')

if __name__ == '__main__':
    app.run(debug=True)
