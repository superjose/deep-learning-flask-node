FROM node:10.8

# The qq is for silent output in the console
RUN apt-get update -qq && apt-get install -y build-essential libpq-dev vim

# Sets the path where the app is going to be installed
ENV NODE_ROOT /var/www/app

# Creates the directory and all the parents (if they don't exist)
RUN mkdir -p $NODE_ROOT

WORKDIR $NODE_ROOT

# Copies the content of package.json
COPY ./Node/package.json .

# Installs all the packages
RUN yarn install

COPY ./Node .

EXPOSE 3000