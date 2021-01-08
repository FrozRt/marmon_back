FROM python:3.8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR .
COPY . .
RUN apt-get install poetry
RUN pip install --upgrade pip setuptools wheel \
    && poetry install \
    && rm -rf /root/.cache/pip
CMD uvicorn main:app --reload --host 0.0.0.0 --port 8000