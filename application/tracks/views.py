from flask import render_template, request, redirect, url_for
from flask_login import current_user, login_manager, login_required
from sqlalchemy.sql import text

from application import app, db
from application.tracks.models import Track
from application.tracks.forms import TrackForm

@app.route("/tracks", methods=["GET"])
@login_required
def tracks_index():
    return render_template("tracks/listtracks.html", tracks=Track.query.all(), basic_stats=Track.tracks_basic_stats(id=current_user.id))

@app.route("/tracks/new", methods=["GET","POST"])
@login_required
def tracks_create():

    form = TrackForm(request.form)

    if not form.validate():
        return render_template("tracks/newtrack.html", form=TrackForm())

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


@app.route("/tracks/all", methods=["GET","POST"])
@login_required
def tracks_create_all():

    track = Track.query.filter_by(name="Rainbow Road").first()

    if not track:
        a = Track(name="Luigi Raceway")
        b = Track(name="Moo Moo Farm")
        c = Track(name="Koopa Troopa Beach")
        d = Track(name="Kalimari Desert")
        e = Track(name="Toads Turnpike")
        f = Track(name="Frappe Snowland")
        g = Track(name="Choco Mountain")
        h = Track(name="Mario Raceway")
        i = Track(name="Wario Stadium")
        j = Track(name="Sherbet Land")
        k = Track(name="Royal Raceway")
        l = Track(name="Bowser Castle")
        m = Track(name="DKs Jungle Parkway")
        n = Track(name="Yoshi Valley")
        o = Track(name="Banshee Boardwalk")
        p = Track(name="Rainbow Road")

        db.session().add(a)
        db.session().add(b)
        db.session().add(c)
        db.session().add(d)
        db.session().add(e)
        db.session().add(f)
        db.session().add(g)
        db.session().add(h)
        db.session().add(i)
        db.session().add(j)
        db.session().add(k)
        db.session().add(l)
        db.session().add(m)
        db.session().add(n)
        db.session().add(o)
        db.session().add(p)
        db.session.commit()
        return redirect(url_for("tracks_index"))

    return redirect(url_for("tracks_index"))