# Repo aws-docker-hf


This repo shows how to run a dockerized Huggingface transformer on EC2 instance with NVIDIA GPU support available for inferencing.

The container exposes an API externally as a JSON GET/POST interface.


##Step 1: Clone and build a docker image.

```
git clone https://github.com/arunesh/aws-docker-hf
cd aws-docker-hf
docker build -t sentiment-hf:latest-1 .
```

