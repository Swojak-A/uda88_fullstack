from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///restaurantmenu.db'
db = SQLAlchemy(app)


class Restaurant(db.Model):
    __tablename__ = 'restaurant'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)

class MenuItem(db.Model):
    __tablename__ = 'menu_item'

    name = db.Column(db.String(80), nullable=False)
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(250))
    price = db.Column(db.String(8))
    course = db.Column(db.String(250))
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'))
    restaurant = db.relationship(Restaurant)


@app.route('/')
def mainPage():
    restaurants = Restaurant.query.all()
    # print([i.name for i in restaurants])
    output = "<html><body>test</body></html>"

    return output


@app.route('/restaurant/<int:restaurant_id>')
def restaurantMenu(restaurant_id):
    restaurant = Restaurant.query.filter_by(id=restaurant_id).one()
    menu_items = MenuItem.query.filter_by(restaurant_id=restaurant_id).all()
    return render_template("menu.html", restaurant=restaurant, menu_items=menu_items)


@app.route('/restaurant/<int:restaurant_id>/item/new_item', methods=['GET', 'POST'])
def newMenuItem(restaurant_id):
    restaurant = Restaurant.query.filter_by(id=restaurant_id).one()

    if request.method == "POST":
        newItem = MenuItem(name=request.form['name'],
                                    description=request.form['description'],
                                    price=request.form['price'],
                                    course=request.form['course'],
                                    restaurant_id=restaurant.id)
        print(newItem.name, newItem.description,  newItem.course, newItem.price)
        # db.session.add(newItem)
        # db.session.commit()
        return redirect(url_for('restaurantMenu', restaurant_id=restaurant.id))


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