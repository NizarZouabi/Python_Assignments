from flask_app import app
from flask import render_template, request, redirect, session, make_response
from flask_bcrypt import Bcrypt
from flask import flash
from flask_app.models import user
bcrypt = Bcrypt(app)
app.secret_key = "jh44erzf321ez1"



@app.route('/')
def main():
    return render_template("login_page.html")


@app.route('/profile/<int:id>')
def profile(id):
    if not session['user_id'] == id:
        flash('Unauthorized Access')
        return redirect('/')
    
    response = make_response(render_template('profile.html', user_id=session['user_id'], username=session.get('username')))
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    
    session['user_id'] = id
    session['username'] = session.get('username')
    
    return response



@app.route('/update_profile/<int:id>')
def update_profile(id):
    if not session['user_id'] == id:
        flash('Unauthorized Access')
        return redirect('/')
    
    session['user_id'] = id
    return render_template("edit_profile.html", user_id=session['user_id'], username=session['username'])




@app.route('/registration', methods=['POST'])
def submit():
    if not user.User.validate_user(request.form):
        return redirect('/')
    
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    data = {
        'username': request.form['username'],
        'email': request.form['email'],
        'password': pw_hash
    }
    
    user.User.save(data)
    return redirect('/')



@app.route('/login', methods=['POST'])
def log():
    data = {"email": request.form['email']}
    user_exist = user.User.get_by_email(data)
    if not user_exist:
        flash("Invalid User Email")
        return redirect('/')
    if not bcrypt.check_password_hash(user_exist.password, request.form['password']):
        flash("Invalid User Password")
        return redirect('/')
    
    session['username'] = user_exist.username
    session['user_id'] = user_exist.id
    user_exist.logged_in = True
    session['logged_in'] = user_exist.logged_in
    if session['logged_in'] is True:
        print("User In Session")
    return redirect(f'/profile/{user_exist.id}')



@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    user_id = session.get('user_id')
    
    if not user.User.validate_user(request.form):
        return redirect(f'/update_profile/{id}')
    
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    data = {
        'id': id,
        'username': request.form['username'],
        'email': request.form['email'],
        'password': pw_hash
    }
    
    session['user_id'] = user_id
    session['username'] = request.form['username']
    user.User.update(data)
    return redirect(f'/profile/{id}')



@app.route('/logout', methods=['POST'])
def clear_session():
    session.clear()
    print('User Left the Session')
    return redirect('/')
