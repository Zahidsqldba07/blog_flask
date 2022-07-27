ARG VERSION=latest
FROM node:18.4.0
LABEL key="nadiein-client"
WORKDIR /app
COPY . .
RUN npm install
EXPOSE 3001
CMD [ "npm run start" ]