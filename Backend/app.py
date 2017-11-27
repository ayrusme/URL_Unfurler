"""The Flask endpoint for getting handling the requests from UI"""

import json

from flask import Flask, jsonify, render_template, request
from flask_cors import CORS

import url_preview

APP = Flask(__name__)
CORS(APP)

@APP.route("/get-thumbnail", methods=["POST"])
def thumbnail_generator():
    """Route Function to handle the thumbnail request from the frontend"""
    website_url = json.loads(request.data.decode())['url']
    try:
        webpage, message = url_preview.send_request(website_url)
        if webpage is not None:
            #Construct the soup object
            soup_object = url_preview.get_soup_object(webpage)
            #Get the title of the artcile
            title = url_preview.get_title(soup_object)
            #Get the website of the article
            website_name = url_preview.get_url(soup_object).rsplit(".", 1)[0]
            if website_name is None:
                website_name = website_url.split("//", 1)[1].split("/", 1)[0].rsplit(".", 1)[0]

            #Get the description of the article
            description = url_preview.get_description(soup_object)

            #Get the published date and time of the article
            date_time = url_preview.get_date_time(website_url)

            #Get the link to the preview image
            image_url = url_preview.get_preview_image(soup_object)['content']

            #Get the link to the favicon
            favicon_url = url_preview. get_favicon(soup_object)

            return render_template(
                "success.html",
                urlx=website_url,
                title=title,
                site_name=website_name,
                description=description,
                date_time=date_time,
                preview_image=image_url,
                favicon=favicon_url
                )
    except Exception as exp:
        return render_template('error.html', msg=str(exp))

if __name__ == "__main__":
    """"Main function to start the Flask server"""
    APP.run(
        "0.0.0.0",
        "8080",
        debug=False,
        threaded=True
    )
