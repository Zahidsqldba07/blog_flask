# syntax=docker/dockerfile:1

ARG VERSION=alpine
FROM python:3.11-rc-buster
LABEL key="nadiein-server"
WORKDIR /app
COPY . .
RUN python3 -m pip install -r requirements.txt && \
    chmod +x start.sh
EXPOSE 5001
CMD [ "./start.sh" ]
