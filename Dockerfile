FROM node:12-alpine as react-build
WORKDIR /usr/src/app
COPY front-end/package.json front-end/package-lock.json ./
COPY front-end/src ./src/
COPY front-end/public ./public/
RUN ls -R
RUN npm install
RUN npm run build

FROM python:3-slim-buster
WORKDIR /usr/src/app
COPY requirements.txt ./
COPY --from=react-build /usr/src/app/build/index.html ./template/index.html
COPY --from=react-build /usr/src/app/build/static ./static/
COPY plot-server ./plot-server/
RUN ls -R
RUN pip install --no-cache-dir -r requirements.txt
ENV PORT=8080
EXPOSE $PORT
CMD gunicorn --bind 0.0.0.0:$PORT plot-server:app
