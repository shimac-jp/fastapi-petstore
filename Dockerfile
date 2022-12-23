FROM docker.io/library/python:3.8-buster

RUN mkdir -p /app

COPY ./app /app

RUN pip install -r /app/requirements.txt

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

