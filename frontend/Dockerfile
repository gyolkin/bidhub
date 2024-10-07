# PROJECT STAGE
FROM node:18-alpine as build-stage

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . ./
RUN npm run build

# NGINX STAGE
FROM nginx:1.27.1-alpine as nginx-stage

COPY --from=build-stage /app/dist /usr/share/nginx/html

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
