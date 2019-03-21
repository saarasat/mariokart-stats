
from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application import app, db
from application.players.models import Player
from application.players.forms import PlayerForm

@app.route("/players", methods=["GET"])
@login_required
def players_index():
    return render_template("players/listplayers.html", players=Player.query.all())

@app.route("/players/new/")
@login_required
def players_form():
    return render_template("players/newplayer.html", form = PlayerForm())

@app.route("/players/", methods=["POST"])
@login_required
def players_create():
    form = PlayerForm(request.form)

    if not form.validate():
        return render_template("players/newplayer.html", form = form)
        
    p = Player(form.handle.data)
    p.account_id = current_user.id

    db.session().add(p)
    db.session().commit()

    return redirect(url_for("players_index"))

@app.route("/delete_player/<int:id>", methods=["POST"])
@login_required
def players_deleteone(id):
    Player.query.filter_by(id=id).delete()
    db.session.commit()

    return redirect(url_for("players_index"))

@app.route("/update_player/<int:id>", methods=["GET","POST"])
@login_required
def players_updateone(id):
    player = Player.query.get(id)
    if request.method == "GET":
        return render_template("players/updateplayer.html", form = PlayerForm(), id=id, handle=player.handle)
    form = PlayerForm(request.form)
    player.handle = form.handle.data
    db.session.commit()

    return redirect(url_for("players_index"))