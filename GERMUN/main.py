from flask import Flask, render_template
import functions

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/registration')
def registration():
    return render_template('registration.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/ressources')
def ressources():
    return render_template('ressources.html')

@app.route('/committees')
def committees():
    return render_template('committees.html')

if __name__ == '__main__':
    app.run(debug=True)
