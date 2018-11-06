FROM python:3.6-alpine

COPY . /deploy
WORKDIR /deploy

RUN pip install pipenv
RUN pipenv install --system --deploy

WORKDIR /deploy/app

CMD ["gunicorn", "-b 0.0.0.0:8000", "web.server:app"]
