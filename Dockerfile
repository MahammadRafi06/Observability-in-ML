# Use the official Python image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy dependencies file and install
COPY requirements.txt . 
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install opentelemetry-distro opentelemetry-exporter-otlp
RUN opentelemetry-bootstrap --action=install
RUN pip uninstall opentelemetry-instrumentation-aws-lambda -y

# Copy the application code
COPY . .

# Set environment variables for Flask
ENV FLASK_APP=app.py
ENV FLASK_ENV=development

ENV OTEL_LOGS_EXPORTER="console"
ENV OTEL_METRICS_EXPORTER="console"
ENV OTEL_TRACES_EXPORTER="console,otlp"
ENV OTEL_EXPORTER_OTLP_ENDPOINT="0.0.0.0:4317"
ENV OTEL_SERVICE_NAME=app
ENV OTEL_EXPORTER_OTLP_INSECURE=true

# Expose the application port (if needed, e.g., Flask)
EXPOSE 80

# Set the command to run the app
CMD ["opentelemetry-instrument","python", "app.py"]