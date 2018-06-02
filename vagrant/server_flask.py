from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

from _CRUD import CRUD_Operator, get_all_rest


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


@app.route('/restaurant/<int:restaurant_id>/item/new_item', methods=['GET', 'POST'])
def newMenuItem(restaurant_id):
    restaurant = CRUD_Operator.get_restaurant(id=restaurant_id)

    if request.method == "POST":
        CRUD_Operator.add_menu_item(name=request.form['name'],
                                    description=request.form['name'],
                                    price=request.form['name'],
                                    course=request.form['name'],
                                    restaurant_id=restaurant.id,
                                    add=False)
        return redirect(url_for('restaurantMenu', restaurant=restaurant))


    else:
        return render_template("newmenuitem.html", restaurant=restaurant)


@app.route('/restaurant/<int:restaurant_id>/item/<int:item_id>/edit')
def editMenuItem(restaurant_id, item_id):
    return "page to edit a menu item. Task 2 complete!"


@app.route('/restaurant/<int:restaurant_id>/item/<int:item_id>/delete')
def deleteMenuItem(restaurant_id, item_id):
    return "page to delete a menu item. Task 3 complete!"




if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5000, debug = True)