from flask import render_template, request, redirect, url_for
from flask_login import current_user, login_manager, login_required
from sqlalchemy.sql import text

from application import app, db
from application.tracks.models import Track


@app.route("/tracks", methods=["GET"])
@login_required
def tracks_index():
    return render_template("tracks/listtracks.html", tracks=Track.query.all(), 
    basic_stats=Track.tracks_basic_stats(id=current_user.id))


@app.route("/delete_track/<int:id>", methods=["POST"])
@login_required
def tracks_deleteone(id):
    stmt = text("DELETE FROM favoriteTracks WHERE track_id = :id").params(id=id)
    db.engine.execute(stmt)
    Track.query.filter_by(id=id).delete()
    db.session.commit()

    return redirect(url_for("tracks_index"))
