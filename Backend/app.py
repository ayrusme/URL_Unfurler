"""The Flask endpoint for getting handling the requests from UI"""

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

import url_preview

APP = Flask(__name__)
CORS(APP)

@APP.route("/get-thumbnail", methods=["POST"])
def thumbnail_generator():
    """Route Function to handle the thumbnail request from the frontend"""
    website_url = request.json['url']
    webpage, message = url_preview.send_request(website_url)
    if webpage is not None:
        try:
            #Construct the soup object
            soup_object = url_preview.get_soup_object(webpage)
            #Get the title of the artcile
            title = url_preview.get_title(soup_object)
            #Get the website of the article
            website_name = url_preview.get_url(soup_object)
            if website_name is None:
                website_name = website_url.split("//", 1)[1].split("/", 1)[0]

            #Get the description of the article
            description = url_preview.get_description(soup_object)

            #Get the published date and time of the article
            date_time = url_preview.get_date_time(website_url)

            #Get the link to the preview image
            image_url = url_preview.get_preview_image(soup_object)['content']

            return jsonify({"status" : message,
                "content" : {
                    "title" : title,
                    "website_name" : website_name,
                    "description" : description,
                    "date_time" : date_time,
                    "preview_image" : image_url
                    }
                })
        except Exception as exp:
            return jsonify({"status": "error", "message": str(exp)}), 400

if __name__ == "__main__":
    """"Main function to start the Flask server"""
    APP.run(
        "0.0.0.0",
        "8080",
        debug=False,
        threaded=True
    )
