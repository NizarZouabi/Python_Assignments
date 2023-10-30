from flask_app import app
from flask import render_template, request, redirect, session, make_response
from flask import flash
from flask_app.models import user, recipe
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
app.secret_key = "lmk2e1fz5re41fg63d"


@app.route('/')
def index():
    if 'user_id' in session:
        return redirect('/dashboard')
    
    return render_template('index.html')


@app.route('/dashboard')
def profile():
    if 'user_id' not in session:
        return redirect('/')
    
    recipes = recipe.Recipe.get_recipes_with_likes()
    
    return render_template('dashboard.html', username=session.get('first_name'), recipes=recipes)


@app.route('/registration', methods=['POST'])
def register():
    if not user.User.validate_user(request.form):
        return redirect('/')

    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': pw_hash
    }

    user.User.add(data)
    flash('Registration Complete','success')
    return redirect('/')


@app.route('/login', methods=['POST'])
def login():
    data = {"email": request.form['email']}
    user_exists = user.User.get_user_by_email(data)
    if not user_exists:
        flash("Invalid User Email")
        return redirect('/')
    if not bcrypt.check_password_hash(user_exists.password, request.form['password']):
        flash("Wrong Password")
        return redirect('/')
    
    session['user_id'] = user_exists.id
    session['first_name'] = user_exists.first_name
    
    return redirect('/dashboard')


@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    response = make_response(redirect('/'))

    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'

    return response