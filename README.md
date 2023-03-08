# IrisClassification
MachineLearning on the famous Iris classification with an api from Flask

## How to run

Clone or download this repo.

Open a terminal and go to the repertory of this project.

Build a docker image with this command:\
```docker build -t appiris_img .```

Then run the container with this command:
```docker run --publish 8000:5000 appiris_img```
