FROM python:3.9
# Run commands from /app directory inside container
WORKDIR /app

# Copy requirements from local to docker image
COPY requirements.txt /app

# INSTALL TOOLS
RUN apt-get update \
 && apt-get -y install sqlite3

# Install the dependencies in the docker image
RUN pip3 install -r requirements.txt --no-cache-dir

# Copy everything from the current dir to the image
COPY . .

CMD ["uwsgi", "uwsgi.ini"]