"""The Flask endpoint for getting handling the requests from UI"""

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

import url_preview

APP = Flask(__name__)
CORS(APP)

@APP.route("/get-thumbnail", methods=["POST"])
def thumbnail_generator():
    """Route Function to handle the thumbnail request from the frontend"""
    request_json = request.get_json()

    webpage, message = url_preview.send_request(request_json['webpage_url'])
    if webpage is not None:
        #Construct the soup object
        soup = url_preview.get_soup_object(webpage)
        
    else:
        return jsonify({"status":"error", "message": message})

if __name__ == "__main__":
    """"Main function to start the Flask server"""
    APP.run(
        "0.0.0.0",
        "8080",
        debug=False,
        threaded=True
    )
