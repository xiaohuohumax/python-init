FROM python:3.8-slim-buster
COPY . /app
WORKDIR /app
RUN sh init_env.sh
