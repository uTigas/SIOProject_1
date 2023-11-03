FROM python:3.9.18-bullseye

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY ./app .

RUN python3 -m flask --app . init-db

CMD [ "python3", "-m" , "flask", "--app","." ,"run", "--host=0.0.0.0"]