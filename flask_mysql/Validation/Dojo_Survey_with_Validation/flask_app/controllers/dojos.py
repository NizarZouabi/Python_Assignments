from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.dojo import Dojo


@app.route('/')
def default():
    return render_template('main.html')


@app.route('/form', methods=['POST'])
def form():
    if not Dojo.validate_dojo(request.form):
        return redirect('/')
    data = {
        "name": request.form['name'],
        "location": request.form['location'],
        "language": request.form['language'],
        "comment": request.form['comment']
    }
    Dojo.save(data)
    return redirect('/result')


@app.route('/result', methods=['GET'])
def show():
    return render_template('info.html', name=session.get('name'), location=session.get('location'), language=session.get('language'), comment=session.get('comment'))
