FROM alpine:3.17.1

RUN apk add python3 py3-pip
RUN pip install dexy

WORKDIR /data

COPY dexy.yaml .
RUN ["dexy", "setup"]

CMD ["dexy"]

