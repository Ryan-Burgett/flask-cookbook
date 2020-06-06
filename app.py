from app import app
from flask_sqlalchemy import SQLAlchemy
from os import environ
from sqlalchemy import create_engine
from app.models import Base

if __name__ == '__main__':
    app.config.from_pyfile('config.py')

    db_uri = environ.get('SQLALCHEMY_DATABASE_URI')
    engine = create_engine(db_uri, echo=True)

    Base.metadata.create_all(engine)

    app.run()
