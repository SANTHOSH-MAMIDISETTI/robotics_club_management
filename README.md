# Robotics Club Management System

## Overview
The Robotics Club Management System (CMS) is a web application designed to manage the activities and members of a robotics club. This system helps organize user roles, groups, and member information efficiently.

## Features
- **User Authentication**: Secure login for members with roles such as Alumni, Staff, Mentor, and Admin.
- **Profile Pages**: Each user has a dedicated profile displaying their name, role, group, and account creation date.
- **Group Management**: Groups cannot exist without assigned mentors, allowing flexibility in organization.
- **User Data Management**: Ability to save usernames, roles, and groups to a file for easy management.
- **Intuitive Interface**: A simple and user-friendly web interface built with Django and advanced CSS.

## Technologies Used
- **Django**: A high-level Python web framework that promotes rapid development and clean design.
- **SQLite**: The default database for storing user and group data.
- **Python**: The programming language used for backend development.
- **HTML/CSS/Bootstrap**: For frontend development.

## Installation

### Prerequisites
- Python 3.x
- Django 4.x

### Steps
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/SANTHOSH-MAMIDISETTI/robotics_club_management.git
   ```

2. **Navigate to the Project Directory**:
   ```bash
   cd robotics_club_management
   ```

3. **Set Up a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   ```

4. **Activate the Virtual Environment**:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

5. **Install the Required Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

6. **Run Database Migrations**:
   ```bash
   python manage.py migrate
   ```

7. **Create a Superuser** (optional):
   ```bash
   python manage.py createsuperuser
   ```

8. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```

9. **Access the Application**:
   Open your web browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to view the application.

## Contributing
We welcome contributions to improve the Club Management System! Whether you're a developer, designer, or documentation enthusiast, your input is invaluable. Feel free to open issues for new features, submit pull requests, and share your ideas. Your contributions mean a lot to us, and we appreciate your support in making this project better !
