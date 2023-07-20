
FROM python:3.11-slim-bullseye

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./csv/UN_WPP2022_GEN_F01_DEMOGRAPHIC_INDICATORS_COMPACT_REV1.csv csv/

COPY ./main.py .
COPY ./DataPage.py .
COPY ./initialize_pages.py .

EXPOSE 8050

CMD ["gunicorn", "main:server", "-b", "0.0.0.0:8050"]