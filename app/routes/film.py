from app import app
from flask import render_template, redirect, url_for
from app.forms.film_form import FilmForm

films = []

@app.route('/film/add', methods=['GET', 'POST'])
def create_film():
    form = FilmForm()
    if form.validate_on_submit():
        film_to_add = {
            'title' : form.title.data,
            'description' : form.description.data,
            'release_date' : form.release_date.data
        }

        films.append(film_to_add)
        print(films)
        return redirect(url_for('index'))

    return render_template('/film/create_film.html', form=form)