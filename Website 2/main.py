#Import Libraries
from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/aboutus/')
def about():
    return render_template('aboutus.html')
@app.route('/signup/')
def signup():
    return render_template('signup.html')
@app.route('/terms/')
def terms():
    return render_template('terms.html')
@app.route('/confirm/')
def confirm():
    return render_template('confirm.html')
@app.route('/cancelcomf/')
def cancelconf():
    return render_template('cancelconf.html')
if __name__ == '__main__':
    app.run(debug=True)