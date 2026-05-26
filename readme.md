# Playwright Automation Framework

A scalable test automation framework built using **Python + Pytest + Playwright** following the **Page Object Model (POM)** design pattern.

This framework supports:

- UI automation
- API automation
- End-to-End (E2E) tests
- Cross-browser execution
- Test tagging (smoke / regression / browser-specific)
- Trace generation for failed tests
- HTML reporting
- GitHub Actions CI integration

---

# Tech Stack

- **Python 3.11+**
- **Pytest**
- **Playwright**
- **Pytest HTML Reporter**
- **Requests** (API testing)
- **GitHub Actions**

---

# Project Structure

```text
playwright-framework/
│
├── api/                     # API clients
│
├── config/                  # Config reader
│
├── fixtures/                # Pytest fixtures
│   ├── browser_fixture.py
│   └── api_fixture.py
│
├── pages/                   # Page Object Model classes
│
├── test_data/               # Test data (JSON)
│
├── tests/
│   ├── api/
│   ├── ui/
│   └── e2e/
│
├── utils/                   # Utility helpers
│
├── traces/                  # Playwright trace files
├── reports/                 # HTML reports
│
├── pytest.ini               # Pytest config
├── requirements.txt
├── .env
└── .github/workflows/c1.yml
```

---

# Features

## UI Automation
- Page Object Model (POM)
- Cross-browser support
- Trace generation
- HTML reports

## API Automation
- REST API testing using Requests
- API fixtures
- JSON payload management

## E2E Testing
- Combined UI + API scenarios

## Reporting
- HTML report generation
- Playwright trace artifacts
- GitHub Actions artifact upload

## CI/CD
- GitHub Actions integration
- Manual workflow trigger
- Cross-browser execution in CI

---

# Setup

## 1. Clone repository

```bash
git clone <repo-url>
cd playwright-framework
```

---

## 2. Create virtual environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Mac/Linux

```bash
python -m venv venv
source venv/bin/activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
playwright install
```

---

# Environment Configuration

Create a `.env` file:

```env
BASE_URL=https://demoqa.com/
BROWSERS=all
HEADLESS=false
API_BASE_URL=https://demoqa.com
TIMEOUT=30000
ENVIRONMENT=qa
```

### Explanation

| Variable | Description |
|----------|-------------|
| BASE_URL | UI base URL |
| BROWSERS | chromium / firefox / webkit / all |
| HEADLESS | true / false |
| API_BASE_URL | API endpoint |
| TIMEOUT | Global timeout |
| ENVIRONMENT | Execution environment |

---

# Running Tests

## Run all tests

```bash
pytest
```

---

## Run specific suite

### UI tests

```bash
pytest tests/ui
```

### API tests

```bash
pytest tests/api
```

### E2E tests

```bash
pytest tests/e2e
```

---

# Test Tagging

Markers are defined in `pytest.ini`.

## Run smoke tests

```bash
pytest -m smoke
```

## Run regression tests

```bash
pytest -m regression
```



Example:

```bash
pytest -m "smoke and chromium"
```

Example:

```bash
pytest -m "regression and firefox"
```

---

# Cross-Browser Execution

Framework supports:

- Chromium
- Firefox
- WebKit

### Run all browsers

In `.env`

```env
BROWSERS=all
```

### Run single browser

```env
BROWSERS=chromium
```

or

```env
BROWSERS=firefox
```

or

```env
BROWSERS=webkit
```

---

# Reports

After execution:

HTML report:

```text
reports/report.html
```

Open in browser.

---

# Trace Files

Playwright traces are stored in:

```text
traces/
```

Open trace:

```bash
playwright show-trace traces/<trace-file>.zip
```

---

# GitHub Actions CI

Workflow file:

```text
.github/workflows/c1.yml
```

Triggers:

- Push
- Manual workflow dispatch

## CI execution includes

- Dependency installation
- Browser installation
- Test execution
- HTML report generation
- Trace artifact upload

---

# Run CI manually

Go to:

```text
GitHub → Actions → Run Tests → Run workflow
```

---

# Writing Tests

Example UI test:

```python```

---

# Best Practices Followed

- Page Object Model
- Externalized test data
- Config-driven execution
- Reusable fixtures
- CI/CD ready
- Browser abstraction
- Trace + reporting support
- Marker-based execution

--

# Common Commands

| Command | Purpose |
|---------|---------|
| pytest | Run all tests |
| pytest -m smoke | Run smoke suite |
| pytest -m regression | Run regression suite |
| pytest tests/ui | Run UI tests |
| pytest tests/api | Run API tests |
| pytest --html=report.html | Generate report |

---

# Future Enhancements

- Allure reporting
- Retry failed tests
- Parallel execution with pytest-xdist
- Docker support
- Environment-based pipelines

---

# Author

Built using:

**Python + Playwright + Pytest**