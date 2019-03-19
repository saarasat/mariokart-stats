
from flask import render_template, request, redirect, url_for

from application import app, db
from application.players.models import Player

@app.route("/players", methods=["GET"])
def players_index():
    return render_template("players/list.html", players=Player.query.all())

@app.route("/players/new/")
def players_form():
    return render_template("players/new.html")

@app.route("/players/", methods=["POST"])
def players_create():
    p = Player(request.form.get("handle"))

    db.session().add(p)
    db.session().commit()

    return redirect(url_for("players_index"))

