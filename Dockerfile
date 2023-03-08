# syntax=docker/dockerfile:1

FROM python
WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt
CMD [ "python3", "app.py", "--host=0.0.0.0"]