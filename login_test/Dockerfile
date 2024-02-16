FROM python:3.12.1

COPY ./requirements.txt /root/
WORKDIR /root
RUN pip install --proxy="http://gwproxy.daikin.co.jp:3128" -r requirements.txt
