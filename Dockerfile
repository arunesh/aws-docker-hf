# syntax=docker/dockerfile:1
# FROM nvidia/cuda:11.6.0-devel-ubuntu18.04
FROM nvidia/cuda:11.5.0-cudnn8-devel-ubuntu18.04

RUN apt update
RUN apt install -y git libsndfile1-dev tesseract-ocr espeak-ng python3 python3-pip ffmpeg
RUN python3 -m pip install --no-cache-dir --upgrade pip

COPY . /app
EXPOSE 8080
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python3", "main.py"]
