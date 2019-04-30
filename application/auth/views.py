from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm, UserForm
from application.character.forms import CharacterForm
from application.character.models import Character
from application.tracks.forms import TrackForm
from application.tracks.models import Track


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

@app.route("/auth/createall", methods=["GET","POST"])
def auth_create_initial_data():

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


