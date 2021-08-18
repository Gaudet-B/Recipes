from flask import app
from recipes_app import app
from flask import render_template, redirect, request, session, flash
from recipes_app.models.user import User
from recipes_app.models.recipe import Recipe
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route("/recipes/<int:recipe_id>")
def view_recipe(recipe_id):
    if "user_id" not in session:
        return redirect("/")
    data = {
        "id": recipe_id
    }
    data2 = {
        "id": session['user_id']
    }
    user = User.get_user_by_id(data2)
    recipe = Recipe.get_recipe_by_id(data)
    print(f'$$$$$$$$$$$$$ {recipe}')
    return render_template("view_recipe.html", recipe = recipe, user = user)

@app.route("/recipes/new")
def create_recipe():
    return render_template("add_recipe.html")

@app.route("/recipes/create", methods=['POST'])
def add_recipe():
    if "user_id" not in session:
        return redirect("/")
    data = {
        "name": request.form['name'],
        "description": request.form['description'],
        "instructions": request.form['instructions'],
        "under_30": request.form['under_30'],
        "user_id": session['user_id'],
        "created_on": request.form['created_on']
    }
    Recipe.new(data)
    return redirect("/users/dashboard")

@app.route("/recipes/edit/<int:recipe_id>")
def edit_recipe(recipe_id):
    if "user_id" not in session:
        return redirect("/")
    data = {
        "id": recipe_id
    }
    recipe = Recipe.get_recipe_by_id(data)
    return render_template("edit_recipe.html", recipe = recipe)

@app.route("/recipes/update", methods=['POST'])
def update_recipe():
    if "user_id" not in session:
        return redirect("/")
    data = {
        "id": request.form['recipe_id'],
        "name": request.form['name'],
        "description": request.form['description'],
        "instructions": request.form['instructions'],
        "under_30": request.form['under_30'],
        "user_id": session['user_id'],
        "created_at": request.form['created_on']
    }
    Recipe.update_recipe(data)
    return redirect("/users/dashboard")

@app.route("/recipes/delete/<int:recipe_id>")
def destroy_recipe(recipe_id):
    if "user_id" not in session:
        return redirect("/")
    data = {
        "id": recipe_id,
        "user_id": session['user_id']
    }
    Recipe.delete_recipe(data)
    return redirect("/users/dashboard")
