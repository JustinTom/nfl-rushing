FROM node:lts-alpine

# Simple http server for serving static content
RUN npm install -g http-server

WORKDIR /app

COPY package*.json ./

RUN npm install

# copy project files and folders to the current working directory (i.e. 'app' folder)
COPY . .

# build app for production with minification
RUN npm run build

EXPOSE 8080
CMD [ "http-server", "dist" ]
