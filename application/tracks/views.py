from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application import app, db
from application.tracks.models import Track
from application.tracks.forms import TrackForm

@app.route("/tracks", methods=["GET"])
@login_required
def tracks_index():
    return render_template("tracks/list.html", tracks=Track.query.all())


@app.route("/tracks", methods=["POST"])
@login_required
def tracks_create():

    form = TrackForm(request.form)

    if not form.validate():
        return render_template("tracks/list.html", tracks=Track.query.all(), form = TrackForm())

    t = Track(name=form.name.data, cup=form.cup.data)
    t.account_id = current_user.id

    db.session().add(t)
    db.session().commit()

    return redirect(url_for("tracks_index"))


@app.route("/delete_track/<int:id>", methods=["POST"])
@login_required
def tracks_deleteone(id):
    Track.query.filter_by(id=id).delete()
    db.session.commit()

    return redirect(url_for("tracks_index"))

@app.route("/tracks/choose_track", methods=["GET", "POST"])
def tracks_choose():
    form = TrackForm(request.form)
    form.name.choices = [(track.id, track.name) for track in Track.query.filter_by(cup="Special Cup").all()]

    return render_template("tracks/choose.html", form = form)

    if request.method == "POST":
        t = Track(name=form.name.data, cup=form.cup.data)
        t.account_id = current_user.id
        db.session().add(t)
        db.session().commit()

        return render_template("tracks/list", tracks=Track.query.all(), form = TrackForm())