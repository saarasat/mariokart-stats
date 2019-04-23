from flask import Flask, render_template, request, redirect, jsonify, url_for
from flask_login import current_user
from sqlalchemy.sql import text
from application import app, db, login_required
from application.players.models import Player, favoritetracks
from application.players.forms import PlayerForm, SearchForm
from application.character.models import Character
from application.tracks.models import Track

@app.route("/players", methods=["GET"])
@login_required(role="ADMIN")
def players_index():
    players = Player.query.filter_by(account_id = current_user.id).all()
    form = PlayerForm(request.form)
    form.firstTrack.choices = [(track.id, track.name) for track in Track.query.all()]
    form.secondTrack.choices = [(track.id, track.name) for track in Track.query.all()]
    form.character.choices = [(character.id, character.name) for character in Character.query.all()]

    return render_template("players/listplayers.html", players=players, form=form)


@app.route("/players", methods=["POST"])
@login_required(role="ADMIN")
def players_create():
    form = PlayerForm(request.form)

    firstTrack = Track.query.filter_by(id = form.firstTrack.data).first()
    character = Character.query.filter_by(id = form.character.data).first()
    character_id = character.id    
    secondTrack = Track.query.filter_by(id = form.secondTrack.data).first()

    player = Player(handle=form.handle.data, character_id=character_id)
    
    player.account_id = current_user.id

    db.session().add(player)
    db.session().commit()

    firstTrack.favoritetracks.append(player)
    db.session().commit()

    secondTrack.favoritetracks.append(player)
    db.session().commit()

    return redirect(url_for("players_index"))

@app.route("/secondtrack/<int:id>")
@login_required(role="ADMIN")
def players_secondTrack(id):

    tracks = []
    tracksFiltered = Track.query.all()
    track_not_wanted = Track.query.filter_by(id=id).first()
    name = track_not_wanted.name
    for track in tracksFiltered:
        if track.id != id:
            tracks.append(track)

    trackArray = []
    for track in tracks:
        trackObj = {}
        trackObj['id'] = track.id
        trackObj['name'] = track.name
        trackArray.append(trackObj)

    return jsonify({'tracks' : trackArray})

@app.route("/statistics/", methods=["GET", "POST"])
@login_required(role="ADMIN")
def players_statistics_search():
    form = SearchForm(request.form)
    form.handle.choices = [(player.id, player.handle) for player in Player.query.filter_by(account_id=current_user.id).all()]
    if request.method == "GET":
        return render_template("players/statisticsSearch.html", form = form)

    player = Player.query.filter_by(id = form.handle.data).first()
    id = player.id 

    return redirect(url_for("players_statisticsone", id=id))

@app.route("/delete_player/<int:id>", methods=["GET", "POST"])
@login_required(role="ADMIN")
def players_deleteone(id):
    player = Player.query.get(id)

    if request.method == "GET":
        return render_template("players/deletion.html", id=id, handle=player.handle)

    stmtFavorite = text("DELETE FROM favoritetracks WHERE player_id = :id").params(id=id)
    db.engine.execute(stmtFavorite)
    stmtRace = text("DELETE FROM Race WHERE player_id= :id").params(id=id)
    db.engine.execute(stmtRace)
    db.session.query(Player).filter_by(id=id).delete()
    db.session.commit()

    return redirect(url_for("players_index"))

@app.route("/update_player/<int:id>", methods=["GET","POST"])
@login_required(role="ADMIN")
def players_updateone(id):
    player = Player.query.get(id)
    if request.method == "GET":
        return render_template("players/updateplayer.html", form = PlayerForm(), id=id, handle=player.handle)
    form = PlayerForm(request.form)
    player.handle = form.handle.data
    db.session.commit()

    return redirect(url_for("players_index"))

@app.route("/statistics/<int:id>", methods=["GET"])
@login_required(role="ADMIN")
def players_statisticsone(id):

    return render_template("players/playerstatistics.html", players=Player.query.filter_by(account_id = current_user.id).all(),
    basic_stats=Player.player_basic_stats(id), races_won=Player.player_races_won(id), character_stats=Player.player_character_stats(id), favorite_tracks=Player.player_find_favoriteTracks(id),
    track_stats=Player.player_track_stats(id), race_stats=Player.player_all_race_stats(id))
