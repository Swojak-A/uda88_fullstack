from flask import Flask, render_template

from _CRUD import CRUD_Operator


app = Flask(__name__)




@app.route('/')
def mainPage():
    restaurants = CRUD_Operator.get_all_restaurants()
    print(restaurants)
    output = "<html><body>test</body></html>"

    return output


@app.route('/restaurant/<int:restaurant_id>')
def restaurantMenu(restaurant_id):
    restaurant = CRUD_Operator.get_restaurant(id=restaurant_id)
    menu_items = CRUD_Operator.get_all_items(restaurant_id=restaurant_id)
    return render_template("menu.html", restaurant=restaurant, menu_items=menu_items)


@app.route('/restaurant/<int:restaurant_id>/item/new_item')
def newMenuItem(restaurant_id):
    return "page to create a new menu item. Task 1 complete!"


@app.route('/restaurant/<int:restaurant_id>/item/<int:item_id>/edit')
def editMenuItem(restaurant_id, menu_id):
    return "page to edit a menu item. Task 2 complete!"


@app.route('/restaurant/<int:restaurant_id>/item/<int:item_id>/delete')
def deleteMenuItem(restaurant_id, menu_id):
    return "page to delete a menu item. Task 3 complete!"




if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5000, debug = True)