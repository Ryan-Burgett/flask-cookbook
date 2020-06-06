from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Recipe(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64), index=True, unique=True)
    description = Column(String(320))
    category = Column(String(20), index=True)
    favorite = Column(Boolean, index=True)
    ingredients = relationship('Ingredient', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<Recipe {}>'.format(self.name)


class Ingredient(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(40), index=True)
    amount = Column(String(20))
    recipe_id = Column(Integer, ForeignKey(Recipe.id))

    def __repr__(self):
        return '<Ingredient {}>'.format(self.name, self.amount)


class User(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(40))
    user_name = Column(String(20), primary_key=True, index=True)
    password = Column(String(60))

    def __repr__(self):
        return '<User {}>'.format(self.name)
