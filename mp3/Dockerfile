# https://hub.docker.com/r/amd64/python
FROM amd64/python:3
WORKDIR /usr/src/app

COPY classify.py .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

ARG dataset

ENV DATASET=mnist
ENV TYPE=ff

CMD [ "python", "./classify.py" ]