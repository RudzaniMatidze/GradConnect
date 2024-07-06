# Gradconnect
![GradConnnect home page](images/home.png)
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
<li> -- gradconnect/ # Project configuration files</li>
<li> ------ init.py</li>
<li> ------ settings.py # Settings for the project</li>
<li> ------ urls.py # URL routing</li>
<li> ------ wsgi.py # WSGI entry point for deployment</li>
<li> -- app/ # Main application code</li>
<li> ------ migrations/ # Database migrations</li>
<li> ------ static/ # Static files (CSS, JavaScript, Images)</li>
<li> ------ templates/ # HTML templates</li>
<li> ------ init.py</li>
<li> ------ admin.py # Admin configuration</li>
<li> ------ apps.py # Application configuration</li>
<li> ------ models.py # Data models</li>
<li> ------ tests.py # Unit tests</li>
<li> ------ views.py # View functions</li>
<li> -- manage.py # Command-line utility for running and managing the project</li>
<li> -- requirements.txt # Python package dependencies</li>
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