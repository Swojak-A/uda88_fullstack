from flask import Flask

from _CRUD import  CRUD_Operator


app = Flask(__name__)




@app.route('/')
def mainPage():

    output = "<html><body>test</body></html>"

    return output


@app.route('/restaurant/<int:restaurant_id>')
def restaurantMenu(restaurant_id):

    restaurant = CRUD_Operator.get_restaurant(restaurant_id)
    output = "<html><body>restaurant test: {}</body></html>".format(restaurant)

    return output




if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5000, debug = True)