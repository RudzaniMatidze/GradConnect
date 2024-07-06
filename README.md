# Gradconnect

Gradconnect is a Django-based web application designed to connect graduates with mentors, job opportunities, and networking events. This project aims to provide a platform for graduates to build professional relationships and advance their careers.

## Table of Contents
- [Colaborators](#Collaborators)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Collaborators
- Rudzani Matidze - [Github](https://github.com/RudzaniMatidze)
- Thomas Manhica - [Github](https://github.com/ManhicaThomas)

## Features
- User authentication and profile management
- Mentor-mentee matching system
- Job postings and application tracking
- Event listings and registrations
- User dashboards for managing connections and activities

## Requirements
- Python 3.x
- Django 3.x or later
- SQLite (default) or other preferred database
- Virtualenv (recommended)

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/RudzaniMatidze/GradConnect.git
    cd gradconnect
    ```
2. Create and activate a virtual environment:
    ```sh
    python3 -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```
3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```
4. Apply migrations:
    ```sh
    python manage.py migrate
    ```
5. Create a superuser:
    ```sh
    python manage.py createsuperuser
    ```
6. Run the development server:
    ```sh
    python manage.py runserver
    ```

## Project Structure
<ul>
<li>gradconnect/</li>
<li> - gradconnect/ # Project configuration files</li>
<li> ---- init.py</li>
<li> ---- settings.py # Settings for the project</li>
      urls.py # URL routing
      wsgi.py # WSGI entry point for deployment
   app/ # Main application code
      migrations/ # Database migrations
      static/ # Static files (CSS, JavaScript, Images)
      templates/ # HTML templates
      init.py
      admin.py # Admin configuration
      apps.py # Application configuration
      models.py # Data models
      tests.py # Unit tests
      views.py # View functions
   manage.py # Command-line utility for running and managing the project
   requirements.txt # Python package dependencies
</ul>

## Usage
- User Registration
Users can sign up by clicking the "Register" link on the homepage. After registration, they can log in to access their dashboard.

- Profile Management
Users can edit their profiles by navigating to the "Edit Profile" section. Here, they can update their personal information, upload a profile picture, and manage their visibility settings.

- Mentor-Mentee Matching
Graduates can search for mentors based on their interests and professional background. Mentors can approve or decline connection requests from graduates.

- Job Postings
Users can browse and apply for job postings. Employers can post job openings and review applications.

- Event Listings
Users can view and register for upcoming events related to their field of interest. Event organizers can create and manage event listings.