FROM python:3.10-slim

RUN apt-get -y update && apt-get -y install curl

ENV POETRY_VERSION=1.7.1
ENV POETRY_HOME=/opt/poetry
ENV POETRY_VIRTUALENVS_CREATE=False

RUN curl -sSL https://install.python-poetry.org | python3 -

ENV PATH="$POETRY_HOME/bin:$PATH:"

WORKDIR /app

COPY . /app

RUN poetry install --no-interaction --no-cache --without dev

EXPOSE 8080

CMD [ "poetry", "run", "gunicorn", "-w", "4", "-b", "0.0.0.0:8080", "wsgi:app" ]