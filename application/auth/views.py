from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm, UserForm
from application.tracks.forms import TrackForm


@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html", form = LoginForm())

    form = LoginForm(request.form)

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("index.html", form = form, error = "No such username or password")

    login_user(user)
    return render_template("auth/initiateapp.html", form=TrackForm(), admin=user.admin)

@app.route("/users/", methods=["GET", "POST"])
def auth_create_user():

    if request.method == "GET":
        return render_template("auth/userform.html", form = UserForm())

    form = UserForm(request.form)

    user = User(form.name.data, form.username.data, form.password.data, form.admin.data)    
    db.session().add(user)
    db.session().commit()

    return redirect(url_for("index"))
    

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))