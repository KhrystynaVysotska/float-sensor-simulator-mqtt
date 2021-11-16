FROM python:3.8-slim-buster

WORKDIR /app
COPY . .

RUN pip3 install -r requirements.txt
RUN touch /app/keys/rsa_private.pem

CMD ["python", "./simulator.py"]