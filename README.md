# Web Application 

## Overview
This project automates several test cases for a web application using **Pytest** and **Playwright**. 
The tests verify that search results match the provided keyword and ensure that 
downloaded wallpapers are not corrupted.

## Technologies Used
- **Python** (Automation scripting)
- **Pytest** (Test framework)
- **Playwright** (Web automation)
- **Pillow (PIL)** (Image verification)
- **Logging & OS** (File handling and logging)

## Installation

1. Clone this repository:
   ```sh
   git clone https://github.com/your-repo-url.git
   cd your-repo

2. Install all libraries from requirements

## How to run tests

1. Run this command in the terminal using :
   ```
   pytest tests/test_suite.py --test-url=<your_URL> --html=report.html