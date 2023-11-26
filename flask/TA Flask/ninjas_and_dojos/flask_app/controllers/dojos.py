from flask_app import app
from flask import render_template, session,request, redirect
from flask_app.models.dojo import Dojo
@app.route("/")
def root():
    return redirect('/dojos')
@app.route("/create_dojo",methods=["POST"])
def add_dojo():
    Dojo.create_dojo(request.form)
    return redirect("/dojos")
@app.route("/dojos")
def index():
    all_dojo=Dojo.show_dojo()
    return render_template("index.html",all_dojo=all_dojo)
@app.route('/dojos/<int:dojo_id>')
def show_dojo(dojo_id):
    data={
        'id':dojo_id
    }
    show=Dojo.show_ninja_in_dojo(data)
    return render_template('show_dojo.html',show=show)
