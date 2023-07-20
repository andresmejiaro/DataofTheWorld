# Pull the official Python 3.11 image
FROM python:3.11-slim-bullseye

# Set work directory
WORKDIR /usr/src/app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the CSV files
COPY ./csv/UN_WPP2022_GEN_F01_DEMOGRAPHIC_INDICATORS_COMPACT_REV1.csv csv/

# Copy the Python files
COPY ./main.py .
COPY ./DataPage.py .

# Expose port
EXPOSE 8050

# Run the application
CMD ["gunicorn", "main:server", "-b", "0.0.0.0:8050"]