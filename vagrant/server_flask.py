from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///restaurantmenu.db'
db = SQLAlchemy(app)


""" CLASSES """

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


""" METHODS """

@app.route('/')
def mainPage():
    restaurants = Restaurant.query.all()
    # print([i.name for i in restaurants])

    return render_template("index.html")


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
        db.session.add(newItem)
        db.session.commit()
        flash("New menu item created!")
        print("Item edited: {}, {}".format(newItem.name, newItem.description,  newItem.course, newItem.price))
        return redirect(url_for('restaurantMenu', restaurant_id=restaurant.id))


    else:
        return render_template("newmenuitem.html", restaurant=restaurant)


@app.route('/restaurant/<int:restaurant_id>/item/<int:item_id>/edit', methods=['GET', 'POST'])
def editMenuItem(restaurant_id, item_id):
    restaurant = Restaurant.query.filter_by(id=restaurant_id).one()
    editedItem = MenuItem.query.filter_by(id=item_id).one()

    if request.method == "POST":
        editedItem.name = request.form['name'] if request.form['name'] != "" else editedItem.name
        editedItem.description = request.form['description'] if request.form['description'] != "" else editedItem.description
        editedItem.price = request.form['price'] if request.form['price'] != "" else editedItem.price
        editedItem.course = request.form['course'] if request.form['course'] != "" else editedItem.course

        db.session.add(editedItem)
        db.session.commit()
        flash("Menu item successfully edited!")
        print("Item edited: {}, {}".format(editedItem.name, editedItem.description, editedItem.course, editedItem.price))
        return redirect(url_for('restaurantMenu', restaurant_id=restaurant.id))


    else:
        return render_template("editmenuitem.html", restaurant=restaurant, item=editedItem)


@app.route('/restaurant/<int:restaurant_id>/item/<int:item_id>/delete', methods=['GET', 'POST'])
def deleteMenuItem(restaurant_id, item_id):
    restaurant = Restaurant.query.filter_by(id=restaurant_id).one()
    toBeDeletedItem = MenuItem.query.filter_by(id=item_id).one()

    if request.method == "POST":
        if request.form['confirmation'] == "DELETE":
            db.session.delete(toBeDeletedItem)
            db.session.commit()
            flash("Menu item successfully erased!")
            print("Item deleted: {}, {}".format(toBeDeletedItem.id, toBeDeletedItem.name))
        return redirect(url_for('restaurantMenu', restaurant_id=restaurant.id))

    else:
        return render_template("deletemenuitem.html", restaurant=restaurant, item=toBeDeletedItem)




if __name__ == '__main__':
    app.secret_key = "ss_key"
    app.run(host='0.0.0.0', port = 5000, debug = True)