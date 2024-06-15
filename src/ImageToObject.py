import cv2
import numpy as np
from flask import Flask, Response
import requests

app = Flask(__name__)

def neural(image):
    # Convert the image to JPEG format
    ret, jpeg = cv2.imencode('.jpg', image)
    return Response(jpeg.tobytes(), mimetype='image/jpeg')

@app.route("/video/<id>")
def video(id):
    address = f"http://image-resize-service/resize/{id}"
    response = requests.get(address)
    frame = cv2.imdecode(np.frombuffer(response.content, np.uint8), cv2.IMREAD_COLOR)
    return neural(frame)

if __name__ == "__main__":
    app.run("0.0.0.0", port=8082, debug=True)
