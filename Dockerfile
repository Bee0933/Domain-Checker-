# base image
FROM python:3.8-slim-bullseye


# copy app files to docker container dir
COPY . /app

# define docker work directory
WORKDIR /app

# instal app dependencies
RUN pip install -r requirements.txt

# expose app port
EXPOSE 5000

# fun flask app as a module inside container 
CMD  ["python3", "-m", "flask", "run", "--host=0.0.0.0"]

