FROM python:3

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt

VOLUME [ "/app/data" ]

EXPOSE 5000

CMD [ "python3", "app.py" ]