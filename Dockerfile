# Dockerfile

FROM debian:latest

# basic
RUN apt-get update && apt-get upgrade
RUN apt-get install -y python3-pip
RUN python3 -m pip install -U pip

COPY . .
# install requirements
RUN python3 -m pip install -U -r requirements.txt

# start the bot
CMD ["python3", "bot.py"]
