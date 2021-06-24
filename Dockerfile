FROM python:3.9-slim
LABEL maintainer=cong

RUN apt-get -y update && rm -rf /var/lib/apt/lists/*
RUN mkdir /home/microblog

WORKDIR /home/microblog

COPY requirements.txt requirements.txt
COPY app app
COPY migrations migrations
COPY microblog.py config.py boot.sh ./
RUN pip install pymysql
RUN pip install -r requirements.txt && rm -rf /root/.cache
RUN chmod +x boot.sh

ENV FLASK_APP microblog.py

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]