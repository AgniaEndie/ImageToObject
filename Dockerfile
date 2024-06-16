
FROM python:3.12-slim
LABEL authors="agniaendie"
RUN apt update; apt install -y libgl1 && apt-get install -y libglib2.0-0 libsm6 libxrender1 libxext6
COPY /src /tmp
WORKDIR /tmp
RUN pip install -r requirements.txt
ENTRYPOINT ["python","ImageToObject.py"]