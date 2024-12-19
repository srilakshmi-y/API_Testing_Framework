# API Automation Framework

## Overview
This is a Python-based API automation framework that supports CRUD (Create, Read, Update, Delete) operations. The framework is designed to be modular, scalable, and reusable for testing REST APIs.

## Features
- Supports **GET**, **POST**, **PUT**, and **DELETE** requests.
- Modular design for easy maintenance and scalability.
- Uses `pytest` for test execution and reporting.
- Configurable using data files (JSON).
- Readable and maintainable test cases with fixtures.


## Folder Structure
```plaintext

API_Automation_Framework_Verizon/
│
├── data/                                    # Data files
│   ├── request_payloads/                    # JSON payloads
│       ├── post_author_invalid.json
│       ├── post_author_valid.json
│       ├── put_author_invalid.json
│       ├── put_author_valid.json
│       └── __init__.py
│ 
├── reports/                                 # Reports 
│   ├── test_report.html                     # Summarry Report for Test cases status
│
│
├── tests/                                   # Test cases for API endpoints
│   ├── test_post_author.py
│   ├── test_get_author.py
│   ├── test_put_author.py
│   ├── test_delete_author.py
│   └── __init__.py
│
├── utils/                                   # Utilities
│   ├── API.py                               # API interaction logic
│   ├── config.py                            # Global configurations (base URL, ID parameters)
│   ├── endpoints.py                         # API endpoints
│   └── data_loader.py                       # Helper for loading test data
│
├── conftest.py                              # Shared fixtures
├── requirements.txt                         # Dependencies
└── README.md                                # Documentation

```

## Setup Instructions
### Install Dependencies
All dependencies are listed in the requirements.txt file. Key dependencies include:

- Python 3.8 or higher. 
- pytest - For test execution.
- requests - For API interaction.
- pytest-html - For generating HTML test reports.


## How to Run
### 1. Run All Tests
To execute all tests, run:

    pytest -v -s

### 2. Run Specific Test
To execute tests for a specific API operation (e.g., GET):

    pytest tests/test_get_author.py

### 3. Generate HTML Report
Use the following command to generate an HTML report:

    pytest --html=reports/test_report.html

## Example Test Output
    ========================================================================================== test session starts ===========================================================================================
    platform darwin -- Python 3.11.10, pytest-8.1.1, pluggy-1.4.0
    rootdir: /Users/sb/PycharmProjects/API_Automation_Framework_Verizon
    plugins: html-4.1.1, metadata-3.1.1
    collected 13 items                                                                                                                                                                                       

    tests/test_delete_author.py ....                                                                                                                                                                   [ 30%]
    tests/test_get_author.py ...                                                                                                                                                                       [ 53%]
    tests/test_post_author.py ...                                                                                                                                                                      [ 76%]
    tests/test_put_author.py ...                                                                                                                                                                       [100%]

    =========================================================================================== 13 passed in 9.01s ===========================================================================================

## Scalability
To test additional APIs:

 - Add new endpoints in API.py.
 - Write test cases for new endpoints in the tests/ folder.
 - Add sample payloads in the data/ folder.
 - Add configurations in the utils/ folder.

