Workout Dashboard

This is a simple web application built with Python's Flask framework. It functions as a workout tracker, allowing users to log their exercise activities. The application is designed to demonstrate a complete development lifecycle, including a fully automated Continuous Integration/Continuous Delivery (CI/CD) pipeline using GitHub Actions.

Features

1. Web-Based Interface: A user-friendly dashboard for logging and viewing workouts.
2. API Endpoint: A RESTful API to add new workouts and retrieve a list of all logged activities.
3. Persistent Data: Workouts are saved to a workouts.json file to persist data between sessions.
4. Automated Testing: Unit tests are included to ensure application functionality and stability.
5. CI/CD Pipeline: An automated pipeline is configured to build, test, and validate the application on every code push.

Prerequisites
To run this application locally, you'll need the following installed on your system:
1. Docker: Used to containerize the application and its dependencies.
2. Git: To clone the repository.
3. Python 3.13>=: Required for running the application and tests outside of a Docker container.
    
Getting Started

Follow these steps to set up and run the application on your local machine.

1. Clone the repository:

       git clone <https://github.com/Sanjo66030/Fitness-Webapp.git>
       cd <Fitness-Webapp>
2. Build the Docker image:
The Dockerfile contains all the necessary instructions to create a portable environment for the application, including installing dependencies from requirements.txt.

       docker build -t workout-dashboard .
3. Run the Docker container:
This command will start the application and map port 5000 from the container to your local machine.

       docker run -p 5000:5000 workout-dashboard

The application will now be accessible at http://localhost:5000 in your web browser.

Running Tests:
The project includes a suite of unit tests using Pytest to ensure code quality.

Within the Docker Image:
To run the tests in the same environment used by the CI/CD pipeline, you can execute the following command after building the Docker image:

       docker run --rm workout-dashboard pytest

This command will create a temporary container, run the tests, and then remove the container.

With PowerShell:
For Windows users, an automated test runner script is provided.

    ./Automated Test Runner for Windows.ps1


CI/CD Pipeline:
This project uses GitHub Actions to automate the build and testing process. The workflow is defined in the .github/workflows/ci-cd.yml file.

The pipeline is triggered automatically on every push or pull_request to the main and develop branches.

Pipeline Steps:
Checkout Repository: The workflow checks out the latest code from the repository.
Build Docker Image: A Docker image is built from the Dockerfile and tagged as workout-dashboard.
Run Pytest Unit Tests: The built Docker image is used to run the pytest unit tests. If any tests fail, the workflow will stop and report a failure.
This automated process ensures that every change pushed to the main development branches is validated for functionality and stability, maintaining a high standard of code quality.

File Structure:

1. app.py: The main Flask application file.
2. index.html: The front-end user interface.
3. requirements.txt: Lists the Python dependencies.
4. test_app.py: The unit tests for the Flask application.
5. Dockerfile: Instructions for building the application's Docker image.
6. .github/workflows/ci-cd.yml: The GitHub Actions workflow definition.
7. Automated Test Runner for Windows.ps1: A script to simplify local test execution on Windows.
8. workouts.json: A JSON file for storing workout data.
