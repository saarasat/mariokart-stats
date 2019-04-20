from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application import app, db
from application.races.models import Race
from application.races.forms import RaceForm
from application.character.models import Character
from application.tracks.models import Track
from application.players.models import Player

@app.route("/races", methods=["GET"])
@login_required
def races_index():
    races = Race.query.filter_by(account_id = current_user.id).all()
    for race in races:
        character = Character.query.filter_by(id=race.character_id).first()
        race.character = character.name
        track = Track.query.filter_by(id=race.track_id).first()
        race.track = track.name
        player = Player.query.filter_by(id=race.player_id).first()
        race.player = player.handle
    
    return render_template("races/listraces.html", races=races)

@app.route("/races/new/", methods=["GET", "POST"])
@login_required
def races_create():
    form = RaceForm(request.form)
    form.track.choices = [(track.id, track.name) for track in Track.query.all()]
    form.character.choices = [(character.id, character.name) for character in Character.query.all()]
    form.player.choices = [(player.id, player.handle) for player in Player.query.filter_by(account_id = current_user.id).all()]

    if request.method == "GET":
        return render_template("races/newrace.html", form = form)

    player = Player.query.filter_by(id = form.player.data).first()
    track = Track.query.filter_by(id = form.track.data).first()
    character = Character.query.filter_by(id = form.character.data).first()
  
    finish_time = form.finish_time.data
    placement = form.placement.data
    player_id = player.id
    track_id = track.id
    character_id = character.id
 
    race = Race(finish_time=finish_time, placement=placement, player_id=player_id, track_id=track_id, character_id=character_id)
    race.account_id = current_user.id

    db.session().add(race)
    db.session().commit()

    return render_template("races/moreplayers.html")

@app.route("/delete_race/<int:id>", methods=["POST"])
@login_required
def races_deleteone(id):
    Race.query.filter_by(id=id).delete()
    db.session.commit()

    return redirect(url_for("races_index"))
