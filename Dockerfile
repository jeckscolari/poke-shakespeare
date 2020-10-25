FROM python:3.8-slim

EXPOSE 8000
WORKDIR /app

COPY poetry.lock pyproject.toml ./
RUN pip install poetry==1.0.* && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev

COPY . ./

CMD uvicorn --host=0.0.0.0 app.main:app