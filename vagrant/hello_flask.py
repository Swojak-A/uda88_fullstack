from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_flask():
    return "<html>This is test flask server</br><strong>Hello World!</strong></html>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5000, debug = True)