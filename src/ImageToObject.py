import requests
from flask import *

app = Flask(__name__)


def neural(image):
    #test
    return image


@app.route("/video/<id>")
def video(id):
    image = requests.get(f"http://image-resize-deployment/resize/{id}")
    return neural(image)


app.run("0.0.0.0", port=8082, debug=True)
