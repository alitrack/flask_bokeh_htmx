FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED 1

RUN addgroup --system flask \
    && adduser --system --ingroup flask flask

COPY --chown=flask:flask ./requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY --chown=flask:flask ./start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

COPY --chown=flask:flask . /app

WORKDIR /app
