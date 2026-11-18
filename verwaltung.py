from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///beispiel.db", echo=True)
Session = sessionmaker(bind=engine)

# Basisklasse für die Datenklassen
Base = declarative_base()

class Person(Base):
    __tablename__ = "person"
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String)
    name = Column(String)
    nachname = Column(String)

Base.metadata.create_all(engine)

def add_person(email, name, nachname):
    with Session() as session:
        person = Person(name=name, email=email, nachname=nachname)
        session.add(person)
        session.commit()  # die id steht erst nach dem commit zur verfügung
        id = person.id
        return id  # id der person zurückgeben

def get_persons():
    with Session() as session:
        persons = session.query(Person).order_by(Person.name).all()
        return persons

def get_person_for_id(id):
    with Session() as session:
        person = session.query(Person).filter(Person.id == id).first()
        return person

def delete_person(id):
    with Session() as session:
        session.query(Person).filter(Person.id == id).delete()
        session.commit()

def update_person():
    with Session() as session:
        session.query(Person).update(Person.id == id)
        return get_persons
        