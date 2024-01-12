# Quizer

Quizer is a Django API built using Django REST framework. It allows users to create, host, and participate in online quizzes.

## Features

- Users can register and login using their email and password
- Users can create exams with multiple choice, fill in the blank, true/false questions and answers
- Users can create classrooms and add other users to them
- Users can host exams for a given classroom and set a time limit and a start date
- Users can join exams and submit their answers
- Users can view their scores and the correct answers after the exam is over
- The API supports JWT authentication and authorization

## Installation

To install Quizer, you need to have Python 3.8 or higher and pip installed on your system. Then, follow these steps:

- Clone this repository: `git clone https://github.com/Dawit-y/quizer.git`
- Create a virtual environment: `python -m venv venv`
- Activate the virtual environment: `source venv/bin/activate` (Linux/Mac) or `venv\Scripts\activate` (Windows)
- Install the requirements: `pip install -r requirements.txt`
- Run the migrations: `python manage.py migrate`
- Create a superuser: `python manage.py createsuperuser`
- Run the server: `python manage.py runserver`

## Testing

To run the tests, use the following command: `python manage.py test`
