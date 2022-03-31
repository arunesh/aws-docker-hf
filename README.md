## Repo aws-docker-hf


This repo shows how to run a dockerized Huggingface transformer on EC2 instance with NVIDIA GPU support available for inferencing.

The container exposes an API externally as a JSON GET/POST interface.

Helpful links for educational purposes:
1. How to run docker nvidia: https://catalog.ngc.nvidia.com/orgs/nvidia/containers/pytorch
2. CUDA base images: https://hub.docker.com/r/nvidia/cuda
3. HuggingFace transformers docker file: https://github.com/huggingface/transformers/blob/main/docker/transformers-pytorch-gpu/Dockerfile
4. Amazon ECR in case we wish to save this image:
https://docs.aws.amazon.com/AmazonECR/latest/userguide/getting-started-cli.html



### Step 1: Clone and build a docker image.

```
git clone https://github.com/arunesh/aws-docker-hf
cd aws-docker-hf
docker build -t sentiment-hf:latest1 .
```

### Step 2: Run the docker
Run `docker version` to check if version > 19.03
```
docker run --gpus all -it --rm sentiment-hf:latest1
```
otherwise
```
nvidia-docker run -it --rm sentiment-hf:latest1
```

### Step 3: Test with a curl request
Get a shell into the docker: do `docker exec --it container_hash bash` where container_hash comes from `docker container ls`.

```
apt-get install curl
curl -X POST -H "Content-Type: application/json" -d @data.json http://127.0.0.1:8080/save
```

To test if GPU is available inside the container, get a shell into the docker and run python3 command line:
```
import torch
use_cuda = torch.cuda.is_available()
print(use_cuda)
```
