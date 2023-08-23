from flask import Flask

app = Flask(__name__)


@app.route('/')
def i_am_flask_app():
    return 'This is a demo project for a "Python Data / Back End Engineer"'
