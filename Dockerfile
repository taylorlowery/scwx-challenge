FROM python:3.8

WORKDIR /opt/scwx_challenge

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . /opt/scwx_challenge

CMD ["ptyest", "./tests"]
