FROM node:17-alpine

WORKDIR /app

COPY package.json ./
COPY package-lock.json ./

COPY . ./

EXPOSE "3000"

RUN npm install

CMD ["npm", "start"]