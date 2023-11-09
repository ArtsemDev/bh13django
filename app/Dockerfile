FROM python:3.11.6-alpine3.18

WORKDIR /web

COPY . /web

RUN cd /web
RUN python -m venv venv
RUN source venv/bin/activate
RUN pip install --no-cache-dir --upgrade -r requirements.txt

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

EXPOSE 8000