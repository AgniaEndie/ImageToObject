import requests
import cv2
from flask import *

app = Flask(__name__)


def neural(image):
    # test
    return Response(image, mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route("/video/<id>")
def video(id):
    localCamera = cv2.VideoCapture(f"http://image-resize-service/resize/{id}")
    success, frame = localCamera.read()

    return neural(frame)


app.run("0.0.0.0", port=8082, debug=True)
