# syntax=docker/dockerfile:1

ARG VERSION=alpine
FROM python:3.11-rc-buster
LABEL key="nadiein-server"
WORKDIR /app
COPY . .
RUN python3 -m pip install -r requirements.txt && \
    chmod +x start.sh && \
    ./start.sh
EXPOSE ${FLASK_RUN_PORT}
ENTRYPOINT [ "python3" ]
CMD [ "main.py" ]
