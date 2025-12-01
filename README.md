# Subsidie Matcher

A Python FastAPI application for analyzing Dutch subsidy eligibility from investment quotes. The service extracts information from PDF quotes and matches them with relevant subsidies based on various criteria.

## Project Description

This API analyzes investment quotes (PDF documents) to determine which Dutch subsidies a company may be eligible for. It uses Claude AI for document processing and intelligent matching of subsidy rules.

## Project Structure

```
subsidie-matcher/
├── main.py                    # FastAPI app
├── services/
│   ├── __init__.py
│   ├── document_processor.py  # PDF extraction
│   └── subsidy_matcher.py     # Matching logic
├── models/
│   ├── __init__.py
│   └── schemas.py             # Pydantic models
├── data/
│   └── subsidies/             # JSON rules
├── tests/
│   ├── __init__.py
│   └── fixtures/              # Sample PDFs
├── .env.example
├── .gitignore
├── requirements.txt
├── README.md
└── docker-compose.yml         # Optional, for PostgreSQL later
```

## Setup Instructions

1. Clone the repository:
```bash
git clone <repository-url>
cd subsidie-matcher
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
# Edit .env and add your ANTHROPIC_API_KEY
```

## How to Run

Start the development server:

```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## API Endpoints

### Health Check

```bash
GET /health
```

Returns the service health status.

**Response:**
```json
{
  "status": "healthy"
}
```

### Root Endpoint

```bash
GET /
```

Returns a welcome message.

## Features

- PDF extraction from investment quotes
- Claude AI-powered document analysis
- Structured data extraction with Instructor
- Subsidy matching based on JSON rules
- RESTful API with FastAPI
- Interactive API documentation

## API Documentation

Once the application is running, visit:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Development

### Running Tests

```bash
pytest
```

### Project Status

Version: 0.1.0 - Initial setup with health check endpoint
