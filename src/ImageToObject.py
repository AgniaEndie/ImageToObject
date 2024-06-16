import numpy as np
import requests
import cv2
from flask import *
import os

app = Flask(__name__)
os.environ["OPENCV_VIDEOIO_DEBUG"] = "1"
os.environ["OPENCV_LOG_LEVEL"] = "debug"


def neural(image):
    # test
    # convert

    # return Response(image, mimetype='multipart/x-mixed-replace; boundary=frame')
    return Response(image.tobytes(), mimetype='image/jpeg')



@app.route("/video/<id>")
def video(id):
    #address = f"http://image-resize-service/resize/{id}"
    address = f'http://localhost:30085/resize/{id}'
    localCamera = cv2.VideoCapture(address)
    success, frame = localCamera.read()
    if success:
        ret, jpeg = cv2.imencode('.jpg', frame)
        return neural(jpeg)
    else:
        return "none"


app.run("0.0.0.0", port=8082, debug=True)
