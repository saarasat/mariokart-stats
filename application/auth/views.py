from flask import render_template, request, redirect, url_for
from flask_login import current_user, login_user, logout_user

from application import app, db, login_required
from application.auth.models import User
from application.auth.forms import LoginForm, UserForm
from application.character.models import Character
from application.tracks.models import Track


@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html", form = LoginForm())

    form = LoginForm(request.form)

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("index.html", form=form, error = "No such username or password")

    login_user(user)
    return redirect(url_for("index"))

@app.route("/users/", methods=["GET", "POST"])
def auth_create_user():

    if request.method == "GET":
        return render_template("auth/userform.html", form = UserForm())

    form = UserForm(request.form)

    name = form.name.data
    username = form.username.data
    password = form.password.data

    if len(name) < 3 or len(name) > 100 or len(username) < 3 or len(username) > 100 or len(password) < 3 or len(password) > 100:
        return render_template("auth/userform.html", form=form, error = "All fields must be between 3-100 characters")

    if User.query.filter_by(username=username).first():
        return render_template("auth/userform.html", form=form, error = "Username already taken")

    user = User(form.name.data, form.username.data, form.password.data)
        
    db.session().add(user)
    db.session().commit()

    track = Track.query.filter_by(name="Rainbow Road").first()

    if not track:
        a = Track(name="Luigi Raceway")
        b = Track(name="Moo Moo Farm")
        c = Track(name="Koopa Troopa Beach")
        d = Track(name="Kalimari Desert")
        e = Track(name="Toads Turnpike")
        f = Track(name="Frappe Snowland")
        g = Track(name="Choco Mountain")
        h = Track(name="Mario Raceway")
        i = Track(name="Wario Stadium")
        j = Track(name="Sherbet Land")
        k = Track(name="Royal Raceway")
        l = Track(name="Bowser Castle")
        m = Track(name="DKs Jungle Parkway")
        n = Track(name="Yoshi Valley")
        o = Track(name="Banshee Boardwalk")
        p = Track(name="Rainbow Road")

        db.session().add(a)
        db.session().add(b)
        db.session().add(c)
        db.session().add(d)
        db.session().add(e)
        db.session().add(f)
        db.session().add(g)
        db.session().add(h)
        db.session().add(i)
        db.session().add(j)
        db.session().add(k)
        db.session().add(l)
        db.session().add(m)
        db.session().add(n)
        db.session().add(o)
        db.session().add(p)
        db.session.commit()

    character = Character.query.filter_by(name="Yoshi").first()

    if not character:
        q = Character(name="Mario")
        r = Character(name="Luigi")
        s = Character(name="Toad")
        t = Character(name="Peach")
        u = Character(name="DK")
        v = Character(name="Bowser")
        x = Character(name="Wario")
        y = Character(name="Yoshi")
        db.session().add(q)
        db.session().add(r)
        db.session().add(s)
        db.session().add(t)
        db.session().add(u)
        db.session().add(v)
        db.session().add(x)
        db.session().add(y)
        db.session().commit()

        return redirect(url_for("index"))

    return redirect(url_for("index"))    

@app.route("/update_user/", methods=["GET","POST"])
def auth_users_updateone():   
    if request.method == "GET":
        return render_template("auth/updateuser.html", form = UserForm())
    
    if request.method == "POST":
        form = UserForm(request.form)

        newName = form.name.data
        newUsername = form.username.data
        newPassword = form.password.data

        if User.query.filter_by(username=newUsername).first():
            if current_user.username != newUsername:
                return render_template("auth/updateuser.html", form=form, error = "Username already taken")

        if newName:
            if len(newName) < 3 or len(newName) > 100:
                return render_template("auth/updateuser.html", form=form, error = "Name must be between 3-100 characters")
            current_user.name = newName

        if newUsername:
            if len(newUsername) < 3 or len(newUsername) > 100:
                return render_template("auth/updateuser.html", form=form, error = "Username must be between 3-100 characters")
            current_user.username = newUsername
        
        if newPassword:
            if len(newPassword) < 3 or len(newPassword) > 100:
                return render_template("auth/updateuser.html", form=form, error = "Password must be between 3-100 characters")
            current_user.password = newPassword
        
        if not newName and not newUsername and not newPassword:
            return render_template("auth/updateuser.html", form=form, error = "Add some data first!")

        db.session().commit()

        return render_template("auth/updateuser.html", form=form, error = "Account info updated!", username=newUsername, name=newName)


@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))


