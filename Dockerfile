FROM python:3.12.4-alpine

RUN pip3 install cutie

WORKDIR /app

COPY menu-test.py .


CMD [ "python3", "menu-test.py" ]