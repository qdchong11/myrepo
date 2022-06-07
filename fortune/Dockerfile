ARG VER=18.2.0

FROM node:${VER}

WORKDIR /app
#install curl
RUN apt update && apt install curl

ADD package.json .
ADD package-lock.json .
ADD public public
ADD views views
ADD main.js .


RUN npm ci

# run image
ENV APP_PORT=3000

EXPOSE ${APP_PORT}

HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
    CMD curl -s http://localhost:${APP_PORT}/healthz || exit 1

ENTRYPOINT [ "node", "main.js"]
