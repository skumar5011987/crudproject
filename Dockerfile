# getting base image
FROM python:3.9-slim
LABEL maintainer="Sailesh Kumar"
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY . .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
# Define the command to run when the container starts
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]