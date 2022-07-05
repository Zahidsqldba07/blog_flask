# syntax=docker/dockerfile:1

ARG VERSION=latest
FROM python:3.8-slim-buster
LABEL key="app"
WORKDIR /app
COPY . .
RUN python3 -m pip install -r /app/requirements.txt
RUN export FLASK_APP=main
RUN export FLASK_ENV=development
EXPOSE 5001
# CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
CMD ["python3 -m flask init-db && python3 -m run flask run -h localhost -p 5001"]
# CMD ["python3", "-m", "flask", "init-db", "&&", "python3", "-m", "flask", "run", "-h", "localhost", "-p", "5001"]