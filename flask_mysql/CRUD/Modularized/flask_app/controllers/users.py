from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.user import User


@app.route('/')
def main():
    return render_template("main.html")


@app.route('/display')
def info():
    users = User.get_all()
    return render_template("display.html", users=users)


@app.route('/create_form', methods=['POST'])
def create():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
    }

    User.save(data)
    return redirect('/display')