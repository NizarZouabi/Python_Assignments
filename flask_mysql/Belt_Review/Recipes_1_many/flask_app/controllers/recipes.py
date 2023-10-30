from flask_app import app
from flask import render_template, request, redirect, session, make_response
from flask import flash
from flask_app.models import recipe, user
from flask_app.controllers import users


@app.route('/create')
def create():
    if not 'user_id' in session:
        return redirect('/')
    
    return render_template('/create.html')


@app.route('/update/<int:id>')
def up(id):
    data = {'id': id}
    if not 'user_id' in session:
        return redirect('/')
    user_id = session['user_id']
    recipe_data = recipe.Recipe.get_recipe(data)
    if not recipe_data:
        return redirect('/dashboard')
    if user_id != recipe_data.user_id:
        return redirect('/dashboard')
    
    
    return render_template('edit.html', id=id)


@app.route('/show/recipe/<int:id>')
def view(id):
    if not 'user_id' in session:
        return redirect('/')
    data = {'id': id}
    this_recipe = recipe.Recipe.get_recipe_with_owner(data)
    return render_template('view.html', recipe = this_recipe)



@app.route('/add', methods=['POST'])
def add():
    if not recipe.Recipe.validate_recipe(request.form):
        return redirect('/create')
    user_id = session['user_id']
    
    data = {'name': request.form['name'],
            'description': request.form['description'],
            'instructions': request.form['instructions'],
            'date': request.form['date'],
            'under_30_min': request.form['under_30_min'],
            'user_id': user_id
            }
    
    recipe.Recipe.create(data)
    return redirect('/dashboard')



@app.route('/edit/<int:id>', methods=['POST'])
def edit(id):
    if not recipe.Recipe.validate_recipe(request.form):
        return redirect(f'/update/{id}')
    
    data = {'id':id,
            'name': request.form['name'],
            'description': request.form['description'],
            'instructions': request.form['instructions'],
            'date': request.form['date'],
            'under_30_min': request.form['under_30_min'],
            }
    
    recipe.Recipe.update(data)
    return redirect('/dashboard')




@app.route('/remove/<int:id>', methods=['POST'])
def remove(id):
    
    data = {'id':id}
    recipe.Recipe.delete(data)
    return redirect('/dashboard')
