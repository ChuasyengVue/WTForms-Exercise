"""Adoption Agency"""

from flask import Flask, request, redirect, render_template, flash, url_for
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adoption'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
app.app_context().push()
db.create_all()


app.config['SECRET_KEY'] = 'SecretKey1!'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
toolbar = DebugToolbarExtension(app)




@app.route("/")
def list_pets():
    """Homepage that list pet name, shows photo, and availability"""

    pets = Pet.query.all()

    return render_template('list_pets.html', pets=pets)


@app.route("/add", methods=["GET","POST"])
def add_pet_form():
    """This should allow user to add pets"""

    form = AddPetForm()

    if form.validate_on_submit():
        new_pet = Pet(name = form.name.data,
                      species = form.species.data,
                      photo_url = form.photo_url.data,
                      age = form.age.data,
                      notes = form.notes.data)
        db.session.add(new_pet)
        db.session.commit()
        flash(f"Pet '{new_pet.name}' Added")
        return redirect(url_for('list_pets'))
    else:
        return render_template("add_new_pet.html", form=form)
    

@app.route("/<int:pet_id>", methods=["GET", "POST"])
def display_edit_form(pet_id):
    """This shows info on the pet and allows user to make edits"""

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)
    
    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        flash(f"Pet '{pet.name} updated!")

        return redirect (url_for("list_pets"))
    
    else:
        return render_template("pet_edit_form.html", form=form, pet=pet)

    
@app.route("/<int:pet_id>/delete", methods=["POST"])
def remove_pet(pet_id):
    """Removing bought or unavailable pet from list"""

    pet = Pet.query.get_or_404(pet_id)
    db.session.delete(pet)
    db.session.commit()

    flash(f"Pet {pet.name} Bought!")
    return redirect('/')

