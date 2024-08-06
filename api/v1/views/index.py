#!/usr/bin/python3
""" module containing the status route """
from api.v1.views import app_views

@app_views.route("/status")
def status():
    return jsonify({"status": "OK"})
