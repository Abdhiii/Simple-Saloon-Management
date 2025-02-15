Salon Ticketing System

Overview

The Salon Ticketing System is a web-based application that allows customers to book salon services and generate tickets for their appointments. The system provides a user-friendly interface with an interactive UI and a backend built using Django.

Features

Select multiple salon services (Hair Cut, Spa, Facial, etc.).

Generate a ticket with a unique ticket ID.

Store customer information and services in a database.

Display ticket details on the UI.

Technologies Used

Frontend: HTML, CSS, JavaScript (Bootstrap for styling)

Backend: Django (Python)

Database: SQLite (Default Django Database)

Installation

Prerequisites

Python (>=3.7)

Django (>=3.2)

Git (Optional, for cloning the repository)

Setup Steps

Clone the repository (or download the source code):

git clone https://github.com/yourusername/salon-ticketing.git
cd salon-ticketing

Create a virtual environment and activate it:

python -m venv venv
source venv/bin/activate   # On Windows, use: venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Apply migrations and run the server:

python manage.py makemigrations
python manage.py migrate
python manage.py runserver

Open the application in your browser:

http://127.0.0.1:8000/

Usage

Enter the customer name in the input field.

Select one or more salon services.

Click the Generate Ticket button.

The ticket details will be displayed on the screen.

Project Structure

├── salon_ticketing/
│   ├── ticketing/         # Django app
│   ├── static/            # CSS, JavaScript, Images
│   ├── templates/         # HTML templates
│   ├── manage.py          # Django project manager
│   ├── db.sqlite3         # SQLite database
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation

Issues & Contributions

If you encounter any issues, feel free to open an issue on GitHub. Contributions are welcome!
