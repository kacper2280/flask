app.py
from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/aboutme')
def about():
    return app.send_static_file('aboutme.html')

@app.route('/contact')
def about():
    return app.send_static_file('contact.html')

@app.route('/gallery')
def about():
    return app.send_static_file('gallery.html')
