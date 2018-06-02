from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = (sessionmaker(bind = engine))
session = DBSession()


class CRUD_Operator():

    @classmethod
    def get_restaurant(cls, id):
        restaurant = session.query(Restaurant).filter_by(id=id).one()
        return restaurant

    @classmethod
    def get_all_restaurants(cls):
        restaurants = [i.name for i in session.query(Restaurant).all()]
        return restaurants

    @classmethod
    def get_all_items(cls, restaurant_id):
        menu_items = session.query(MenuItem).filter_by(restaurant_id=restaurant_id).all()
        return menu_items

    @classmethod
    def add_menu_item(cls, name, description, price, course, restaurant_id, add=False):
        newItem = MenuItem(
            name = name,
            description = description,
            price = price,
            course = course,
            restaurant_id=restaurant_id)
        print(newItem.name, newItem.description, newItem.price, newItem.course, newItem.restaurant_id)
        if add == True:
            session.add(newItem)
            session.commit()
        else:
            pass


    @classmethod
    def delete_menu_item(cls, item_id):
        item_to_be_deleted = session.query(MenuItem).filter_by(id=item_id).one()
        print("i could totally delete item {}: {}".format(item_to_be_deleted.id, item_to_be_deleted.name))




