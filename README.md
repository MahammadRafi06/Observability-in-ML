# Observability in Distributed Systems with OpenTelemetry
 
This project demonstrates comprehensive observability implementation for distributed systems using OpenTelemetry (OTel), showcasing different instrumentation approaches and deployment strategies in containerized and Kubernetes environments.

## 🎯 Project Overview

The project implements a **Cardiac Analysis Service** - a medical data analysis application that serves as a realistic example for demonstrating observability patterns. The application analyzes patient cardiac data and provides risk assessments, making it perfect for showcasing how to monitor critical business applications.

### Key Features

- **Multiple Instrumentation Approaches**: Manual, Zero-code, and Kubernetes Operator-based
- **Complete Observability Stack**: Traces, Metrics, and Logs
- **Production-Ready Configurations**: Docker Compose and Kubernetes deployments
- **Real-world Application**: Medical data analysis with premium service tiers

## 🏗️ Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Application   │───▶│ OpenTelemetry   │───▶│   Observability │
│   (Flask App)   │    │   Collector     │    │      Stack      │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                                                       │
                                           ┌───────────┼───────────┐
                                           │           │           │
                                    ┌─────────┐ ┌─────────┐ ┌─────────┐
                                    │ Jaeger  │ │Prometheus│ │  Logs   │
                                    │(Traces) │ │(Metrics)│ │ (Debug) │
                                    └─────────┘ └─────────┘ └─────────┘
```

## 📁 Project Structure

```
Observability-in-ML/
├── manual-instrumetation/          # Manual OpenTelemetry instrumentation
│   ├── app.py                      # Flask app with manual tracing
│   ├── Dockerfile                  # Container configuration
│   ├── requirements.txt            # Python dependencies
│   └── data/                       # Sample medical datasets
├── zero-instrumetation/            # Zero-code instrumentation approach
│   ├── app.py                      # Flask app (no manual tracing)
│   ├── docker-compose.yaml         # Full observability stack
│   ├── collector/                  # OpenTelemetry Collector config
│   └── prometheus/                 # Prometheus configuration
├── K8-Operator/                    # Kubernetes operator approach
│   ├── autom-instrument.yaml       # Auto-instrumentation configuration
│   ├── demo-collector.yaml         # Collector deployment
│   └── OpenTelemetryCollector.yaml # Collector CRD
└── k8/                             # Kubernetes Helm values
    ├── values_deployment.yaml      # Deployment mode values
    └── values_daemonset.yaml       # DaemonSet mode values
```

## 🚀 Getting Started

### Prerequisites

- Docker and Docker Compose
- Kubernetes cluster (for K8s deployments)
- OpenTelemetry Operator (for auto-instrumentation)
- Python 3.11+ (for local development)

### Environment Variables

Create a `.env` file in the `zero-instrumetation` directory:

```bash
# Docker Images
JAEGERTRACING_IMAGE=jaegertracing/all-in-one:latest
COLLECTOR_CONTRIB_IMAGE=otel/opentelemetry-collector-contrib:latest
PROMETHEUS_IMAGE=prom/prometheus:latest

# Ports
PROMETHEUS_SERVICE_PORT=9090
```

## 🔧 Implementation Approaches

### 1. Manual Instrumentation

Located in `manual-instrumetation/` directory.

**Features:**
- Explicit tracing with custom spans
- Manual span attributes and events
- Direct OpenTelemetry API usage

**Key Code Example:**
```python
from opentelemetry import trace
tracer = trace.get_tracer("app.tracer")

@app.route('/analyze', methods=['POST'])
def analyze():
    with tracer.start_as_current_span("add") as span:
        # Your business logic here
        span.set_attribute("app.value", transaction_data)
```

**Running:**
```bash
cd manual-instrumetation
docker build -t cardiac-manual .
docker run -p 8080:8080 cardiac-manual
```

### 2. Zero-Code Instrumentation

Located in `zero-instrumetation/` directory.

**Features:**
- Automatic instrumentation without code changes
- Complete observability stack with Docker Compose
- Jaeger for distributed tracing
- Prometheus for metrics collection

**Services Included:**
- **Cardiac Server**: The main application
- **Jaeger**: Distributed tracing UI
- **OpenTelemetry Collector**: Telemetry data processing
- **Prometheus**: Metrics storage and querying

**Running:**
```bash
cd zero-instrumetation
docker-compose up -d
```

**Access Points:**
- Application: http://localhost:8099
- Jaeger UI: http://localhost:16686
- Prometheus: http://localhost:9090

### 3. Kubernetes Operator Approach

Located in `K8-Operator/` directory.

**Features:**
- Automatic instrumentation using OpenTelemetry Operator
- Kubernetes-native deployment
- Scalable collector configuration

**Prerequisites:**
```bash
# Install OpenTelemetry Operator
kubectl apply -f https://github.com/open-telemetry/opentelemetry-operator/releases/latest/download/opentelemetry-operator.yaml
```

**Deployment:**
```bash
# Create namespace
kubectl create namespace application

# Deploy collector
kubectl apply -f K8-Operator/demo-collector.yaml

# Deploy auto-instrumentation
kubectl apply -f K8-Operator/autom-instrument.yaml

# Deploy your application with annotation:
# sidecar.opentelemetry.io/inject: "true"
```

## 🎛️ Configuration Deep Dive

### OpenTelemetry Collector Configuration

The collector is configured to:
- Receive OTLP data on ports 4317 (gRPC) and 4318 (HTTP)
- Process data with memory limiting and batching
- Export to multiple backends (Jaeger, Prometheus, Debug)

### Kubernetes Configurations

#### DaemonSet Mode (`k8/values_daemonset.yaml`)
- Collects node-level metrics
- Enables Kubernetes attributes processor
- Collects kubelet metrics and logs

#### Deployment Mode (`k8/values_deployment.yaml`)
- Cluster-level metrics collection
- Kubernetes events collection
- Single replica for cluster-wide data

## 🏥 Demo Application Details

### Cardiac Analysis Service

The demo application simulates a medical service that:
- Analyzes patient cardiac data
- Provides risk assessments
- Offers premium vs. basic service tiers
- Processes transaction-based requests

### Sample Usage

1. **Access the application** at the configured port
2. **Enter a Transaction ID** (4-digit number)
3. **View analysis results** with detailed patient information
4. **Observe telemetry data** in Jaeger and Prometheus

### Sample Transaction IDs
Check the `data/Transactions.csv` file for valid transaction IDs to test with.

## 📊 Observability Features

### Distributed Tracing
- **Jaeger Integration**: Complete request tracing across services
- **Custom Spans**: Business logic instrumentation
- **Trace Correlation**: Request flow visualization

### Metrics Collection
- **Application Metrics**: Custom business metrics
- **System Metrics**: Resource utilization
- **Kubernetes Metrics**: Pod and node metrics

### Logging
- **Structured Logging**: JSON formatted logs
- **Log Correlation**: Trace ID injection
- **Centralized Collection**: Aggregated log viewing

## 🔍 Monitoring and Alerting

### Key Metrics to Monitor
- Request latency and throughput
- Error rates and success ratios
- Resource utilization (CPU, memory)
- Database query performance

### Alerting Rules
Configure alerts for:
- High error rates (>5%)
- Slow response times (>2s)
- Service unavailability
- Resource exhaustion

## 🛠️ Development and Testing

### Local Development
```bash
# Install dependencies
pip install -r requirements.txt

# Install OpenTelemetry packages
pip install opentelemetry-distro opentelemetry-exporter-otlp
opentelemetry-bootstrap --action=install

# Run with instrumentation
opentelemetry-instrument --traces_exporter console --service_name cardiac-server flask run
```

### Testing Instrumentation
1. Generate sample requests
2. Verify trace generation in Jaeger
3. Check metrics in Prometheus
4. Validate log correlation

## 📚 Best Practices

### Instrumentation Guidelines
- Use semantic naming for spans and attributes
- Implement proper error handling and reporting
- Add business context to traces
- Monitor critical user journeys

### Performance Considerations
- Configure appropriate sampling rates
- Use batch processing for high-volume data
- Implement memory limits on collectors
- Monitor collector performance

### Security
- Secure collector endpoints
- Implement proper authentication
- Use TLS for data transmission
- Sanitize sensitive data in traces

## 🔄 Production Deployment

### Scaling Considerations
- Deploy collectors as DaemonSets for node-level data
- Use deployment mode for cluster-level metrics
- Configure resource limits and requests
- Implement horizontal scaling for high load

### Backup and Recovery
- Backup collector configurations
- Implement data retention policies
- Plan for disaster recovery scenarios
- Monitor data pipeline health

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Implement your changes
4. Add tests and documentation
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

For issues and questions:
- Check the documentation
- Search existing issues
- Create a new issue with detailed information
- Include logs and configuration details

## 🔗 Additional Resources

- [OpenTelemetry Documentation](https://opentelemetry.io/docs/)
- [Jaeger Documentation](https://www.jaegertracing.io/docs/)
- [Prometheus Documentation](https://prometheus.io/docs/)
- [OpenTelemetry Operator](https://github.com/open-telemetry/opentelemetry-operator)

---

**Happy Monitoring! 🚀** 