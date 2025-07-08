# Automation Testing Boilerplate

A comprehensive boilerplate repository for various automation testing frameworks and tools. This repository provides ready-to-use templates and utilities for web, mobile, and API testing using popular automation frameworks.

## 🚀 Features

- **Multi-Framework Support**: Selenium, Appium, Playwright, and Robot Framework
- **Python & TypeScript**: Support for both Python and TypeScript/JavaScript
- **Utility Libraries**: Reusable components for common automation tasks
- **Test Reporting**: HTML reports with pytest-html integration
- **Cross-Platform**: Works on Windows, macOS, and Linux
- **Page Object Model**: Structured test architecture patterns

## 📁 Project Structure

```text
Automation-Boilerplate/
├── AppiumTest/              # Mobile app testing with Appium
├── PlaywrightTest/          # Web testing with Playwright (TypeScript)
├── SeleniumTest/            # Web testing with Selenium (Python)
├── RobotFrameworkTest/      # Keyword-driven testing with Robot Framework
├── PyUtils/                 # Python utility classes and helpers
│   ├── Appium/              # Appium-specific utilities
│   └── Selenium/            # Selenium-specific utilities
├── reports/                 # Test execution reports
├── requirements.txt         # Python dependencies
├── pytest.ini               # pytest configuration
└── README.md
```

## 🛠️ Supported Testing Frameworks

### 1. Selenium WebDriver (Python)

- **Location**: `SeleniumTest/`
- **Purpose**: Web browser automation
- **Features**: Cross-browser testing, page object model, pytest integration

### 2. Appium (Python)

- **Location**: `AppiumTest/`
- **Purpose**: Mobile application testing (iOS/Android)
- **Features**: Native, hybrid, and web mobile app testing

### 3. Playwright (TypeScript)

- **Location**: `PlaywrightTest/`
- **Purpose**: Modern web testing framework
- **Features**: Auto-wait, browser contexts, parallel execution

### 4. Robot Framework

- **Location**: `RobotFrameworkTest/`
- **Purpose**: Keyword-driven testing
- **Features**: Human-readable test cases, extensive library ecosystem

## 🔧 Prerequisites

### For Python-based frameworks

- Python 3.8+
- pip (Python package manager)

### For Playwright

- Node.js 14+
- npm or yarn

### For Mobile Testing (Appium)

- Android SDK (for Android testing)
- Xcode (for iOS testing on macOS)
- Appium Server

## 📦 Installation & Setup

### 1. Clone the Repository

```bash
git clone <repository-url>
cd Automation-Boilerplate
```

### 2. Python Dependencies

```bash
pip install -r requirements.txt
```

### 3. Playwright Setup

```bash
cd PlaywrightTest
npm install
npx playwright install
```

### 4. Robot Framework Setup

Robot Framework dependencies are included in `requirements.txt`.

## 🚀 Quick Start

### Running Selenium Tests

```bash
# Run all Selenium tests
pytest SeleniumTest/

# Run specific test file
pytest SeleniumTest/test_01.py

# Run with HTML report
pytest SeleniumTest/ --html=reports/selenium-report.html
```

### Running Appium Tests

```bash
# Ensure Appium server is running first
pytest AppiumTest/

# Run specific test
pytest AppiumTest/test_app_01.py
```

### Running Playwright Tests

```bash
cd PlaywrightTest

# Run all tests
npx playwright test

# Run tests with UI mode
npx playwright test --ui

# Generate test code
npx playwright codegen https://example.com
```

### Running Robot Framework Tests

```bash
# Run all Robot Framework tests
robot RobotFrameworkTest/Tests/

# Run specific test file
robot RobotFrameworkTest/Tests/test.robot

# Run with custom output directory
robot --outputdir reports RobotFrameworkTest/Tests/
```

## 🧰 Utility Libraries

### PyUtils Package

The `PyUtils` package contains reusable components:

- **`person.py`**: Person data model for test data
- **`address.py`**: Address data model for test data
- **`Selenium/`**: Selenium-specific utilities (login, logout)
- **`Appium/`**: Appium-specific utilities (login, logout)

## 📊 Test Reporting

### Python Tests (pytest-html)

- HTML reports are generated in the `reports/` directory
- Configure in `pytest.ini` file
- Includes test results, logs, and screenshots

### Playwright Tests

- Built-in HTML reporter
- Trace viewer for debugging
- Screenshot and video capture on failures

### Robot Framework Tests

- log.html, report.html, and output.xml files
- Detailed execution logs with screenshots

## 🔧 Configuration

### pytest Configuration (`pytest.ini`)

```ini
[pytest]
addopts = --html=reports/test-report.html --self-contained-html
testpaths = 
    AppiumTest
    SeleniumTest
python_files = test_*.py
```

### Playwright Configuration (`playwright.config.ts`)

Located in `PlaywrightTest/playwright.config.ts` - configure browsers, timeouts, and reporters.

## 🔍 Debugging Tips

### Playwright

```bash
# Run in headed mode
npx playwright test --headed

# Debug mode
npx playwright test --debug

# Trace viewer
npx playwright show-trace trace.zip
```

### Python Tests

```bash
# Verbose output
pytest -v

# Stop on first failure
pytest -x

# Run specific test method
pytest SeleniumTest/test_01.py::test_method_name
```
