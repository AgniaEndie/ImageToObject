import requests
import cv2
from flask import *

app = Flask(__name__)


def neural(image):
    # test
    # convert

    # return Response(image, mimetype='multipart/x-mixed-replace; boundary=frame')
    return Response(image, mimetype='image/jpeg')


@app.route("/video/<id>")
def video(id):
    localCamera = cv2.VideoCapture(f"http://image-resize-service/resize/{id}")
    success, frame = localCamera.read()
    ret, jpeg = cv2.imencode('.jpg', frame)
    return neural(jpeg)


app.run("0.0.0.0", port=8082, debug=True)
