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
ENV OTEL_EXPORTER_OTLP_ENDPOINT="0.0.0.0:4317"
ENV OTEL_EXPORTER_OTLP_INSECURE=true
ENV OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED=true
# Expose the application port (if needed, e.g., Flask)
EXPOSE 80

# Set the command to run the app
CMD ["opentelemetry-instrument", "--traces_exporter", "console", "--metrics_exporter", "console", "--logs_exporter", "console", "--service_name", "dice-server", "flask", "run", "-p", "8080"]
