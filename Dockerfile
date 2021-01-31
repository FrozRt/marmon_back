FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR .

COPY . .

RUN pip install poetry && poetry config virtualenvs.create false

RUN pip install --upgrade pip setuptools wheel \
    && poetry install --no-root --no-dev\
    && rm -rf /root/.cache/pip

CMD uvicorn main:app --reload --host 0.0.0.0 --port 8000