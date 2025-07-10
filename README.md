# Cardiac Risk Analyzer

A Flask-based healthcare analytics application that provides heart attack risk analysis using machine learning models. The application processes patient data and provides premium cardiac risk assessment services through a web interface.

## Features

- **Heart Attack Risk Analysis**: ML-powered risk assessment using Azure Machine Learning
- **Premium Service Model**: Tiered service offering with premium analytics
- **Patient Data Management**: Secure handling of patient demographics and medical data
- **Report Generation**: HTML and PDF report generation for analysis results
- **Web Interface**: User-friendly interface for healthcare professionals
- **Containerized Deployment**: Docker and Kubernetes support for scalable deployment

## Technology Stack

- **Backend**: Flask (Python)
- **Machine Learning**: Azure ML Services
- **Data Processing**: Pandas
- **Frontend**: HTML/CSS with Bootstrap
- **Report Generation**: HTML to PDF conversion
- **Containerization**: Docker
- **Orchestration**: Kubernetes
- **Data Storage**: CSV files

## Installation

### Prerequisites

- Python 3.7+
- Docker (optional)
- Azure ML Service account (for premium features)

### Local Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd cardiac-risk-analyzer
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your Azure ML API key
```

4. Run the application:
```bash
python app.py
```

The application will be available at `http://localhost:5000`

### Docker Deployment

1. Build the Docker image:
```bash
docker build -t cardiac-risk-analyzer .
```

2. Run the container:
```bash
docker run -p 5000:5000 cardiac-risk-analyzer
```

### Kubernetes Deployment

Deploy using the provided Kubernetes configuration:

```bash
cd K8/
kubectl apply -f .
```

## Usage

1. **Access the Application**: Navigate to the web interface
2. **Enter Transaction ID**: Input a 4-digit transaction ID for analysis
3. **View Results**: Get comprehensive cardiac risk analysis report
4. **Download Reports**: Export results as PDF for medical records

## Data Structure

### Patient Data (`data/Patient.csv`)
- Patient demographics and contact information
- Healthcare provider details
- Clinic information

### Transaction Data (`data/Transactions.csv`)
- Medical test results and measurements
- Premium service flags
- Cardiac risk factors including:
  - Age, sex, chest pain type
  - Blood pressure and cholesterol levels
  - ECG results and exercise parameters

## API Endpoints

- `GET /` - Main application interface
- `POST /analyze` - Process transaction and generate risk analysis
- `GET /download-pdf` - Download analysis report as PDF

## Premium Service Features

Premium subscribers receive:
- Advanced ML-powered risk analysis
- Detailed cardiac risk assessment
- Clinical recommendations
- Enhanced reporting capabilities

## Security

- SSL certificate verification bypass for development
- Environment variable management for API keys
- Secure data handling practices

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -am 'Add your feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support and questions:
- Create an issue in the repository
- Contact the development team
- Review the documentation

## Disclaimer

This application is for educational and research purposes. All medical decisions should be made in consultation with qualified healthcare professionals. The risk analysis provided is not a substitute for professional medical diagnosis.

## Roadmap

- [ ] Enhanced ML models for improved accuracy
- [ ] Multi-language support
- [ ] Advanced reporting features
- [ ] Integration with EMR systems
- [ ] Mobile application support
- [ ] Real-time monitoring capabilities

---

**Note**: Ensure you have proper Azure ML credentials configured before using premium features.
