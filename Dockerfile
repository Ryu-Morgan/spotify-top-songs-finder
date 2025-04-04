FROM python:3.12

RUN apt-get update && apt-get upgrade -y

RUN apt install vim -y

RUN mkdir ./opt/src

COPY requirements.txt ./opt/src

RUN pip install --no-cache-dir -r ./opt/src/requirements.txt

COPY . /opt/src

WORKDIR ./opt/src

CMD ["/bin/bash", "-c", "sleep infinity"]