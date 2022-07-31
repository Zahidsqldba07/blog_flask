ARG VERSION=latest
FROM node:18.4.0
LABEL key="nadiein-client"
WORKDIR /app
COPY . .
RUN npm i
EXPOSE 3001
CMD [ "npm", "start" ]