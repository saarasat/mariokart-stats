from flask import Flask, render_template, request, redirect, jsonify, url_for
from flask_login import login_required, current_user
from application import app, db
from application.players.models import Player
from application.players.forms import PlayerForm, SearchForm
from application.character.models import Character
from application.tracks.models import Track

@app.route("/players", methods=["GET"])
@login_required
def players_index():
    return render_template("players/listplayers.html", players=Player.query.all())


@app.route("/players/new/", methods=["POST", "GET"])
@login_required
def players_create():
    form = PlayerForm(request.form)
    form.firstTrack.choices = [(track.id, track.name) for track in Track.query.all()]
    form.character.choices = [(character.id, character.name) for character in Character.query.all()]

    firstTrack = Track.query.filter_by(id = form.firstTrack.data).first()
    form.secondTrack.choices = [(track.id, track.name) for track in Track.query.all()]

    if request.method == "GET":
        return render_template("players/newplayer.html", form = form)

    firstTrack = Track.query.filter_by(id = form.firstTrack.data).first()
    character = Character.query.filter_by(id = form.character.data).first()
    character_id = character.id    
    secondTrack = Track.query.filter_by(id = form.secondTrack.data).first()

    player = Player(handle=form.handle.data, character_id=character_id)
    
    player.account_id = current_user.id

    db.session().add(player)
    db.session().commit()

    firstTrack.favoriteTracks.append(player)
    db.session().commit()

    secondTrack.favoriteTracks.append(player)
    db.session().commit()

    return redirect(url_for("races_create"))

@app.route("/secondtrack/<int:id>")
def secondTrack(id):
    print('id', id)
    
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

@app.route("/statistics/", methods=["GET", "POST"])
@login_required
def player_statistics_search():
    form = SearchForm(request.form)
    form.handle.choices = [(player.id, player.handle) for player in Player.query.all()]
    if request.method == "GET":
        return render_template("players/statisticsSearch.html", form = form)

    player = Player.query.filter_by(id = form.handle.data).first()
    id = player.id 

    return redirect(url_for("player_statistics", id=id))

@app.route("/statistics/<int:id>", methods=["GET"])
@login_required
def player_statistics(id):
   
    return render_template("players/playerstatistics.html", players=Player.query.all(),  races_played=Player.how_many_races_played(id))
