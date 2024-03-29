# todo-app-w-django

This is a simple ToDo List web application built with Django. It allows users to manage their tasks with basic CRUD (Create, Read, Update, Delete) operations.

## Preview

### Image
![Alt text](image.png)

### Video 
https://www.awesomescreenshot.com/video/25962926?key=71ee743cb726b8e286e9bf2714eb7e0e

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.6 or higher
- Django 2.2 or higher

### Installing

First, clone the repository to your local machine:

```bash
git clone https://github.com/your-username/todo-list-django.git
cd todo-list-django
```

Next, create a virtual environment and activate it:

```
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

Then, install the requirements:

```
pip install -r requirements.txt
```


### Setting Up
To set up the database, run the following command:

first create the migration
```
 python manage.py makemigrations
 ```
the, upgrade it
```
python manage.py migrate
```

### Running the Application
To run the server, use the following command:
```
python manage.py runserver
```

Now, open your web browser and go to http://127.0.0.1:8000/ to view the application.

### Features
1. Add a new task
2. View the list of tasks
3. Mark a task as completed
4. Delete a task

### Author
Francisco Orozco - @frako23
