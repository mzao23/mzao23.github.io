from flask import Flask, render_template, redirect, request
import functions

app = Flask(__name__)

__email__ = ''
__psswd__ = ''
__vcode__ = ''

verification = False

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/registration', methods=['GET', 'POST'])
def registration():
    
    global verification, __email__, __psswd__, __vcode__

    error_msg = ""

    if request.method == 'POST':

        email = request.form.get('email')
        password = request.form.get('password')
        cpassword = request.form.get('cpassword')
        
        if password == cpassword:
            __v__ = functions.email_verification(email)

            print(__v__)

            if __v__[0]:
                verification = True
                __email__ = email
                __psswd__ = password
                __vcode__ = __v__[1]
                return redirect('/verification')

            else:
                error_msg = '<h3 style="color: red;">Invalid address.</h3>'

        else:
            error_msg = '<h3 style="color: red;">Please type the same password.</h3>'

    return render_template('registration.html', error_msg=error_msg)

@app.route('/login', methods=['GET', 'POST'])
def login():

    error_msg = ''

    if request.method == 'POST':

        email = request.form.get('email')
        password = request.form.get('password')

        if functions.verify_user(email, password):
            return redirect('/home')
        
        else:
            error_msg = '<h3 style="color: red;">Incorrect informations.</h3>'

    return render_template('login.html', error_msg=error_msg)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/ressources')
def ressources():
    return render_template('ressources.html')

@app.route('/committees')
def committees():
    return render_template('committees.html')

@app.route('/verification', methods=['GET', 'POST'])
def verification_route():

    global verification, __vcode__, __email__, __psswd__

    error_msg = ''

    if verification:
        email = __email__

        if request.method == 'POST':

            if request.form.get('code') == __vcode__:
                functions.add_user(email, __psswd__)
                verification = False
                __vcode__ = ''
                __email__ = ''
                __psswd__ = ''
                return redirect('/home')

            else:
                error_msg = '<h3 style="color: red;">Please verify that you typed the correct code.</h3>'
    
    else:
        return redirect('/home')
    
    return render_template('verification.html', error_msg=error_msg)

if __name__ == '__main__':
    app.run(debug=True)
