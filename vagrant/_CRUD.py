from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()


class CRUD_Operator():

    @classmethod
    def get_restaurant(cls, id):
        restaurant = session.query(Restaurant).filter_by(id=id).first()
        return restaurant.name

    @classmethod
    def get_all_restaurants(cls):
        restaurants = [i.name for i in session.query(Restaurant).all()]
        return restaurants







