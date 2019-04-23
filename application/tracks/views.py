from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user
from sqlalchemy.sql import text

from application import app, db
from application.tracks.models import Track
from application.tracks.forms import TrackForm

@app.route("/tracks", methods=["GET"])
@login_required
def tracks_index():
    return render_template("tracks/listtracks.html", tracks=Track.query.all(), basic_stats=Track.tracks_basic_stats())


@app.route("/tracks", methods=["POST"])
@login_required
def tracks_create():

    form = TrackForm(request.form)

    if not form.validate():
        return render_template("tracks/newtrack.html", tracks=Track.query.all(), form = TrackForm())

    t = Track(name=form.name.data)
    t.account_id = current_user.id

    db.session().add(t)
    db.session().commit()

    return redirect(url_for("tracks_index"))


@app.route("/delete_track/<int:id>", methods=["POST"])
@login_required
def tracks_deleteone(id):
    stmt = text("DELETE FROM favoriteTracks WHERE track_id = :id").params(id=id)
    db.engine.execute(stmt)
    Track.query.filter_by(id=id).delete()
    db.session.commit()

    return redirect(url_for("tracks_index"))
