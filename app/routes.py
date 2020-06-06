from flask import render_template

from app import app


@app.route("/")
@app.route("/index")
def index():
    user = {'username': 'Ryan'}
    return render_template('index.html', title='Home', user=user)


@app.route("/favorites")
def favorites():
    return render_template('favorites.html')

@app.route("/add")
def add_page():
    return render_template('add.html')

@app.route("/recipe")
def get_recipe():
    recipe = {'name': 'Chicken Fried'}
    return render_template('recipe.html', recipe=recipe)

# @app.route("/add/recipe")
#     def add_recipe():
