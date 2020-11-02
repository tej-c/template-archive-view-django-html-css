FROM python:3
ENV PYTHONUNBUFFERED 1
WORKDIR /art
ADD . /art
COPY ./requirements.txt /art/requirements.txt
COPY ./pass.txt /art/pass.txt
RUN pip install -r requirements.txt
COPY . /art
