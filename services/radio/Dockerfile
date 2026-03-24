FROM ubuntu:18.04 AS builder

RUN apt-get update
RUN apt-get install -y wget git gcc curl make

RUN wget -P /tmp https://dl.google.com/go/go1.13.linux-amd64.tar.gz

RUN tar -C /usr/local -xzf /tmp/go1.13.linux-amd64.tar.gz
RUN rm /tmp/go1.13.linux-amd64.tar.gz

ENV GOPATH /go
ENV PATH $GOPATH/bin:/usr/local/go/bin:$PATH
RUN mkdir -p "$GOPATH/src" "$GOPATH/bin" && chmod -R 777 "$GOPATH"

RUN curl -fsSL https://deb.nodesource.com/setup_16.x | bash -
RUN apt-get install -y nodejs
RUN npm install -g yarn@1

ENV APP_DIR /go/src/github.com/HackerDom/ructfe-2019/services/radio/
RUN mkdir -p $APP_DIR
WORKDIR $APP_DIR

COPY . .

RUN make build

FROM ubuntu:18.04

RUN set -eux; \
	groupadd -r radio --gid=999; \
	useradd -r -g radio --uid=999 --home-dir=/app --shell=/bin/bash radio;

ENV APP_DIR /app
ENV SECRET_PATH /secrets/

RUN mkdir -p $APP_DIR
RUN mkdir -p $SECRET_PATH
RUN chown radio:radio $APP_DIR
RUN chown radio:radio $SECRET_PATH

USER radio
WORKDIR $APP_DIR

COPY --from=builder /go/src/github.com/HackerDom/ructfe-2019/services/radio/.build/ $APP_DIR
COPY config.yaml.example config.yaml
COPY scripts $APP_DIR/scripts
COPY ./secrets/db_password.example $SECRET_PATH/db_password
COPY ./docker-entry.sh $APP_DIR

EXPOSE 4553
CMD [ "/app/docker-entry.sh" ]
