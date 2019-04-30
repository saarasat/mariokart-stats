from flask import Flask, render_template, request, redirect, jsonify, url_for
from flask_login import current_user, login_required
from sqlalchemy.sql import text
from application import app, db
from application.character.models import Character
from application.character.forms import CharacterForm

@app.route("/characters", methods=["GET"])
@login_required
def characters_index():
    return render_template("characters/listcharacters.html", characters=Character.query.all())

@app.route("/characters/uusi", methods=["GET", "POST"])
@login_required
def characters_add_all():

    if request.method == "GET":
        return render_template("characters/newcharacter.html", form=CharacterForm())

    d = Character(name="Mariott")
    
    db.session().add(d)
    db.session().commit()

    return redirect(url_for("characters_index"))


@app.route("/characters/new", methods=["GET","POST"])
@login_required
def characters_create():

    form = CharacterForm(request.form)

    if not form.validate():
        return render_template("characters/newcharacter.html", form=CharacterForm())

    c = Character(name=form.name.data)
 
    db.session().add(c)
    db.session().commit()
    
    return redirect(url_for("characters_index"))

@app.route("/update_character/<int:id>", methods=["GET","POST"])
@login_required
def characters_updateone(id):
    character = Character.query.get(id)
    if request.method == "GET":
        return render_template("characters/updatecharacter.html", form = CharacterForm(), id=id, name=character.name)
    form = CharacterForm(request.form)
    character.name = form.name.data
    db.session.commit()

    return redirect(url_for("characters_index"))

@app.route("/delete_character/<int:id>", methods=["POST"])
@login_required
def characters_deleteone(id):
    Character.query.filter_by(id=id).delete()
    db.session.commit()

    return redirect(url_for("characters_index"))
