from flask import Flask, render_template, request, redirect, jsonify, url_for
from flask_login import current_user
from sqlalchemy.sql import text
from application import app, db, login_required
from application.players.models import Player, favoritetracks
from application.players.forms import PlayerForm, SearchForm
from application.character.models import Character
from application.tracks.models import Track

@app.route("/players", methods=["GET", "POST"])
@login_required(role="USER")
def players_create():

    players = Player.query.filter_by(account_id = current_user.id).all()
    form = PlayerForm(request.form)
    form.firstTrack.choices = [(track.id, track.name) for track in Track.query.all()]
    form.secondTrack.choices = [(track.id, track.name) for track in Track.query.all()]
    form.character.choices = [(character.id, character.name) for character in Character.query.all()]

    if request.method == "GET":
        return render_template("players/listplayers.html", players=players, form=form)

    if request.method == "POST":

        if not form.character.data or not form.firstTrack.data or not form.secondTrack.data or not form.handle.data:        
            return render_template("players/listplayers.html", players=players, form=form, error="All fields must be filled out")

        firstTrack = Track.query.filter_by(id = form.firstTrack.data).first()
        character = Character.query.filter_by(id = form.character.data).first()
        secondTrack = Track.query.filter_by(id = form.secondTrack.data).first()

        handle = Player.query.filter_by(handle=form.handle.data).first()   

        if len(form.handle.data) < 3 or len(form.handle.data) > 100 or handle:
            return render_template("players/listplayers.html", players=players, form=form, error="Name must be unique and 3-100 characters")
    
        player = Player(handle=form.handle.data, character_id=character.id)
    
        player.account_id = current_user.id

        db.session().add(player)
        db.session().commit()

        firstTrack.favoritetracks.append(player)
        db.session().commit()

        secondTrack.favoritetracks.append(player)
        db.session().commit()

    return redirect(url_for("players_create"))

@app.route("/secondtrack/<int:id>")
@login_required(role="USER")
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
@login_required(role="USER")
def players_statistics_search():
    form = SearchForm(request.form)
    form.handle.choices = [(player.id, player.handle) for player in Player.query.filter_by(account_id=current_user.id).all()]
    if request.method == "GET":
        return render_template("players/statisticsSearch.html", form = form, player_ranking=Player.player_ranking())

    if request.method == "POST":

        if not form.handle.data:
            return render_template("players/statisticsSearch.html", form = form, player_ranking=Player.player_ranking(), error="Go create some stats first!")
        
        if not form.handle.choices:
            return render_template("players/statisticsSearch.html", form = form, player_ranking=Player.player_ranking(), error="Go create some stats first!")

        player = Player.query.filter_by(id=form.handle.data).first()
        return redirect(url_for("players_statisticsone", id=player.id))

    return render_template("players/statisticsSearch.html", form = form, player_ranking=Player.player_ranking())

@app.route("/delete_player/<int:id>", methods=["GET", "POST"])
@login_required(role="USER")
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

    return redirect(url_for("players_create"))

@app.route("/update_player/<int:id>", methods=["GET","POST"])
@login_required(role="USER")
def players_updateone(id):
    player = Player.query.get(id)
    if request.method == "GET":
        return render_template("players/updateplayer.html", form = PlayerForm(), id=id, handle=player.handle)
    form = PlayerForm(request.form)

    handle = Player.query.filter_by(handle=form.handle.data).first()
    if len(form.handle.data) < 3 or len(form.handle.data) > 100 or handle:
        return render_template("players/updateplayer.html", form = PlayerForm(), id=id, handle=player.handle, error="Name must be between 3-100 characters")

    player.handle = form.handle.data
    db.session.commit()

    return redirect(url_for("players_create"))

@app.route("/statistics/<int:id>", methods=["GET"])
@login_required(role="USER")
def players_statisticsone(id):

    return render_template("players/playerstatistics.html", players=Player.query.filter_by(account_id = current_user.id).all(),
    basic_stats=Player.player_basic_stats(id), races_won=Player.player_races_won(id), character_stats=Player.player_character_stats(id), favorite_tracks=Player.player_find_favoriteTracks(id),
    track_stats=Player.player_track_stats(id), race_stats=Player.player_all_race_stats(id))
