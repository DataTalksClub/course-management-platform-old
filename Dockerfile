FROM python:3.10

WORKDIR /app

RUN pip install pipenv
COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --deploy --system

COPY cmp cmp

WORKDIR /app/cmp

ENTRYPOINT [ "python", "manage.py", "runserver" ]
