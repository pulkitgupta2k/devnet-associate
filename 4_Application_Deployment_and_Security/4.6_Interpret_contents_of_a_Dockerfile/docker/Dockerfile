#specify the os for the docker
FROM ubuntu:18:04

# specify the maintainer
MAINTAINER Pulkit Gupta "pulkitgupta2k@gmail.com"

# commands to install pip3 in the container
RUN apt-get update -y && apt-get install -y python3-pip python3-dev

# command to allow traffic in port 5000
CMD ["ufw allow 5000"]

# copy the dependencies from local to the docker container
COPY ./requirements.txt /app/requirements.txt

# making app as the container directory
WORKDIR /app

# installing dependencies
RUN pip3 install -r requirements.txt

# copying the script to the container folder
COPY ./myAPI/myAPI.py /app

# program to run
ENTRYPOINT ["python3"]

# what to run
CMD ["myAPI.py"]
