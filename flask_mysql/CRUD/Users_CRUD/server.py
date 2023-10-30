
from flask import Flask, render_template, request, redirect
from users import User
app = Flask(__name__)

@app.route('/users/new')
def main():
    return render_template("main.html")

@app.route('/users')
def info():
    users = User.get_all()
    return render_template("view_all.html", users=users)

@app.route('/users/new', methods=['POST'])
def create():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        }
    
    User.save(data)
    return redirect('/users')

@app.route('/users/<int:id>/edit')
def edit(id):
    data = {'id':id}
    
    user_data = User.get_one(data)
    return render_template('edit.html', user = user_data)

@app.route('/user/<int:id>/update', methods=['POST'])
def update(id):
    
    data = {'id': id,
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            }
    
    User.update(data)
    return redirect(f'/user/{id}')

@app.route('/user/<int:id>')
def show(id):
    data = {'id': id}
    
    user_data =  User.get_one(data)
    return render_template('view.html', user=user_data)

@app.route('/remove/<int:id>', methods=['POST'])
def delete(id):
    data = {'id': id}
    
    User.delete(data)
    return redirect('/users')


if __name__=="__main__":
    app.run(debug=True)