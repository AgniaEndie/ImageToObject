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


#
# @app.route("/video/<id>")
# def video(id):
#     #address = f"http://image-resize-service/resize/{id}"
#     address = f'http://localhost:30085/resize/{id}'
#     localCamera = cv2.VideoCapture(address)
#     success, frame = localCamera.read()
#     if success:
#         ret, jpeg = cv2.imencode('.jpg', frame)
#         return neural(jpeg)
#     else:
#         return "none"

@app.route("/video/<id>")
def video(id):
    # Replace 'url' with the actual MJPEG URL
    url = f"http://image-resize-service/resize/{id}"

    # Send a GET request to the MJPEG URL
    response = requests.get(url, stream=True)

    # Check if the response is successful
    if response.status_code == 200:
        # Read the response content as bytes
        bytes = bytes()
        for chunk in response.iter_content(chunk_size=1024):
            bytes += chunk

        # Find the start and end markers of each JPEG image in the response
        start_marker = bytes.find(b'\xff\xd8')
        end_marker = bytes.find(b'\xff\xd9')

        # Extract the JPEG image bytes
        jpeg_bytes = bytes[start_marker:end_marker + 2]

        # Decode the JPEG image bytes into a NumPy array
        image = cv2.imdecode(np.frombuffer(jpeg_bytes, dtype=np.uint8), cv2.IMREAD_COLOR)
        return Response(image,mimetype="image/jpg")

app.run("0.0.0.0", port=8082, debug=True)
