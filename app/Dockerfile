# syntax=docker/dockerfile:1

ARG VERSION=latest
FROM python:3.8-slim-buster
LABEL key="app"
WORKDIR /app
COPY . .
RUN python3 -m pip install -r /app/requirements.txt
ENTRYPOINT ["/bin/bash", "/app/start.sh"]
RUN chmod +x /app/profile.sh
RUN chmod +x /app/start.sh
EXPOSE 5001
