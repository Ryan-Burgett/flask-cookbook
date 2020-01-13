from app import db


class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    description = db.Column(db.String(320))
    category = db.Column(db.String(20), index=True)
    ingredients = db.relationship('Ingredient', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<Recipe {}>'.format(self.name)


class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), index=True)
    amount = db.Column(db.String(20))
    recipe_id = db.Column(db.Integer, db.ForeignKey(Recipe.id))

    def __repr__(self):
        return '<Ingredient {}>'.format(self.name, self.amount)
