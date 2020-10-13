FROM python:3-slim

WORKDIR /app

RUN apt-get update --fix-missing \
    && apt-get install -y build-essential

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY main.py rushing.json gunicorn.conf.py ./
RUN mkdir logs

EXPOSE 8001

CMD ["gunicorn", "-b", "0.0.0.0:8001", "main:app"]
