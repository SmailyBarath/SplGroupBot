FROM python:3.10-slim-buster

WORKDIR /ALPHA

COPY requirements.txt /ALPHA

RUN pip3 install -r requirements.txt

COPY . /ALPHA

CMD ["python3", "yashu.py"]
