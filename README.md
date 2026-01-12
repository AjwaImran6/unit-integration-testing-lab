# unit-integration-testing-lab

## Student Information
Name: Ajwa  
Roll Number: 231400105

## Project Description
This project demonstrates Unit Testing and Integration Testing using pytest
for a simple banking application. The application includes deposit, withdrawal,
interest calculation, loan eligibility, and money transfer functionalities.

## How to Run Tests
Install dependencies:
pip install -r requirements.txt

Run all tests:
pytest

Run with verbose output:
pytest -v

Generate HTML report:
pytest --html=report.html -v

## GitHub Actions
GitHub Actions is configured to automatically run unit and integration tests
on every push or pull request. If all tests pass, a green tick will appear
in the Actions tab.
