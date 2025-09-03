Workout Dashboard

This is a simple web application built with Python's Flask framework. It functions as a workout tracker, allowing users to log their exercise activities. The application is designed to demonstrate a complete development lifecycle, including a fully automated Continuous Integration/Continuous Delivery (CI/CD) pipeline using GitHub Actions.

Features

    Web-Based Interface: A user-friendly dashboard for logging and viewing workouts.

    API Endpoint: A RESTful API to add new workouts and retrieve a list of all logged activities.

    Persistent Data: Workouts are saved to a workouts.json file to persist data between sessions.

    Automated Testing: Unit tests are included to ensure application functionality and stability.

    CI/CD Pipeline: An automated pipeline is configured to build, test, and validate the application on every code push.

Prerequisites

To run this application locally, you'll need the following installed on your system:

    Docker: Used to containerize the application and its dependencies.

    Git: To clone the repository.

    Python 3.9+: Required for running the application and tests outside of a Docker container.
    
Getting Started

Follow these steps to set up and run the application on your local machine.

1. Clone the repository:
    git clone <your-repository-url>
    cd <your-repository-name>
