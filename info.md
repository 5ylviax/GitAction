## Build Docker Image Locally

```txt
docker build -t <your-dockerhub-username>/<image-name>:<tag>
```
Example:
```txt 
docker build -t orky/pyt:v0.1 .
```

## Test Image Locally 
```txt
docker run -it --rm orky/pyt:v0.1 bash
```
(with out the **bash** opens *Python* not the shell)
- to exit the container type **exit** 
- Then inside the container check that pytest is installed 

```txt 
pytest --version 
```
## Push the Image to Docker Hub 
1. First log in
```txt 
docker login
```

2. Push the image 
``` docker push orky/pyt:v0.1
```
this uploads your image so GitHub Actions can pull it 

## GitHub Actions Will Now Use Your Image 
```yaml 
conatiner: 
    image: orly/pyt:v0.1 
```
GitHub Actions will automatically:

pull orky/pyt:v0.1 from Docker Hub

use it as the environment

run your tests inside it

No building happens on GitHub — everything is already inside your published image.

GitHub Action work flow should look it 
```yaml
name: Python CI

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test-in-container:
    runs-on: ubuntu-latest
    container:
      image: orky/pyt:v0.1  # <-- your pushed image

    steps:
      - name: Check out code
        uses: actions/checkout@v4

      - name: Run tests in container
        run: pytest
```

# Extra info

## Difference 
| Command | What it Means | When to use it |
| -------- | -------- | -------- |
| docker commit  | Save changes from a running container into a new image | When you manually install stuff inside a container |
|docker push  | Upload an image to Docker Hub| After you have a final image you want to share or use in GitHub ActionsV
### Summary 
- docker commit 
    - save your changes 
    - creates a new image 
    - only used when you manually change stuff in the contaienr 
- docker push 
    - uploads your image to Docker Hub 
    - Used AFTER your image to Docker Hub
    - Needed for GitHub Actions 
## Commit the container -> new image 
```txt
 docker ps -a (find the container ID)
```

```txt 
docker commit <id> orky/pyt:v0.1
```
