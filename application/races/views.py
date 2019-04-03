from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application import app, db
from application.races.models import Race, playersraces
from application.races.forms import RaceForm
from application.character.models import Character
from application.tracks.models import Track
from application.players.models import Player

@app.route("/races", methods=["GET"])
@login_required
def races_index():
    races = Race.query.all()
    for race in races:
        character = Character.query.filter_by(id=race.character_id).first()
        race.character = character.name
        track = Track.query.filter_by(id=race.track_id).first()
        race.track = track.name
    
    return render_template("races/listraces.html", races=Race.query.all(), character_races=Character.find_the_character_with_most_races())

@app.route("/races/new/", methods=["GET", "POST"])
@login_required
def races_create():
    form = RaceForm(request.form)
    form.track.choices = [(track.id, track.name) for track in Track.query.all()]
    form.character.choices = [(character.id, character.name) for character in Character.query.all()]
    form.player.choices = [(player.id, player.handle) for player in Player.query.all()]

    if request.method == "GET":
        return render_template("races/newrace.html", form = form)
 
    track = Track.query.filter_by(id = form.track.data).first()
    character = Character.query.filter_by(id = form.character.data).first()
    player = Player.query.filter_by(id = form.player.data).first()
  
    finish_time = form.finish_time.data
    placement = form.placement.data
    track_id = track.id
    character_id = character.id
    player_id = player.id 

    race = Race(finish_time=finish_time, placement=placement, track_id=track_id, character_id=character_id)
    race.account_id = current_user.id

    db.session().add(race)
    db.session().commit()

    player.playersraces.append(race)

    db.session().commit()

    return redirect(url_for("races_index"))

@app.route("/delete_race/<int:id>", methods=["POST"])
@login_required
def races_deleteone(id):
    Race.query.filter_by(id=id).delete()
    db.session.commit()

    return redirect(url_for("races_index"))
