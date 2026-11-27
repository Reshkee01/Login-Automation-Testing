
# Login Automation Testing Project

## Project Overview
This project automates the login functionality of a demo website using Selenium WebDriver and Pytest.

## Tools & Technologies
- Python
- Selenium WebDriver
- Pytest
- Pytest HTML Report
- Google Colab

## Test Scenarios

| Test Case | Expected Result |
|---|---|
| Valid Login | Successful login |
| Invalid Password | Error message displayed |
| Invalid Username | Error message displayed |

## Project Structure

Login_Automation/
- pages/ - Page Object Model classes
- tests/ - Automated test cases
- screenshots/ - Failure screenshots
- reports/ - HTML test reports
- conftest.py - Pytest configuration
- requirements.txt - Required Python libraries

## How to Run

Install dependencies:

pip install -r requirements.txt

Run tests:

pytest tests/test_login.py -v

Generate HTML report:

pytest tests/test_login.py -v --html=reports/login_report.html --self-contained-html

## Test Results

Latest execution:
- Total Tests: 3
- Passed: 3
- Failed: 0

## Website Tested

https://the-internet.herokuapp.com/login

## Note
This is a practice project created for learning automation testing.
