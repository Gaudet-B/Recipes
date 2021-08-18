from flask import app
from recipes_app import app
from flask import render_template, redirect, request, session, flash
from recipes_app.models.user import User
from recipes_app.models.recipe import Recipe
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/users/register", methods=['POST'])
def register_user():
    pw_hash = bcrypt.generate_password_hash(request.form['password_input'])
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email":request.form['email_input'],
        "password": pw_hash
    }
    check = User.validate_user(request.form)
    if not check:
        return redirect("/")
    user = User.new_user(data)
    print(user)
    session['user_id'] = user
    return redirect("/users/dashboard")


@app.route("/users/login", methods=['POST'])
def login_user():
    data = {
            "email": request.form['email_login']
        }
    user = User.get_user_by_email(data)
    if not user:
        flash("Invalid Email/Password")
        return redirect("/")
    if not bcrypt.check_password_hash(user[0]['password'], request.form['password_login']):
        flash("Invalid Email/Password")
        return redirect("/")
    session['user_id'] = user[0]['id']
    return redirect("/users/dashboard")

@app.route("/users/dashboard")
def dashboard():
    print(session)
    if "user_id" not in session:
        return redirect("/")
    data = {
        "id": session['user_id']
    }
    user = User.get_user_by_id(data)
    print(f'**********{user}')
    recipes = Recipe.get_recipes_by_user(data)
    print(f'**********{recipes}')
    return render_template("dashboard.html", user = user, recipes = recipes)

@app.route("/users/logout")
def logout_user():
    session.clear()
    return redirect("/")