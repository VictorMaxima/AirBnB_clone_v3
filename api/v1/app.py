#usr/bin/python3
""" module for api """


import flask
from flask import Flask
from models import storage
from app.v1.views import app_views
import os


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()


host_name = os.getenv("HBNB_API_HOST") if os.getenv("HBNB_API_HOST") else "0.0.0.0"
port_name = os.getenv("HBNB_API_PORT") if os.getenv("HBNB_API_PORT") else "5000"


if __name__ == '__main__':
    app.run(host=host_name, port=port_name, threaded=True)
