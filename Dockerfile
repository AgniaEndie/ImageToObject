FROM ubuntu:22.04
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
RUN apt install -y libgl1-mesa-glx

FROM python:3.12-slim
LABEL authors="agniaendie"

COPY /src /tmp
WORKDIR /tmp
RUN pip install -r requirements.txt
ENTRYPOINT ["python","ImageToObject.py"]