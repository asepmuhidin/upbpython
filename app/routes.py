from flask import render_template
from app import app


@app.route('/')
@app.route('/index')

def index():
    profile={
        'name' : 'Asep Muhidin',
        'email':'asep.muhidin@gmail.com',
        'photo':'profile1.png',
    }
    return render_template('index.html', title='Home', profile=profile)
