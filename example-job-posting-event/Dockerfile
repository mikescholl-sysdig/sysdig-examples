FROM alpine:latest

RUN addgroup -S sdcjob && adduser -S sdcjob -G sdcjob

RUN apk add python3
RUN apk add py3-pip
RUN pip3 install sdcclient 

RUN mkdir /app
ADD random_number.py /app/random_number.py
RUN chmod -x /app/random_number.py

ADD entrypoint.sh /entrypoint.sh
RUN chmod +x ./entrypoint.sh
USER sdcjob 

ENTRYPOINT [ "/bin/sh", "./entrypoint.sh" ]