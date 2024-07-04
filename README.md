# Django Admin Panel

## Requirements:
- Python 3
- PostgreSQL 16

## Instructions:
1. Clone the project: 
    ```bash
    git clone https://github.com/ornur/django.git
    ```

2. Install requirements for `venv`:
    ```bash
    pip install -r requirements.txt
    ```
3. Migrate models to Database:
    ```bash
    python manage.py makemigrations
    ```
    and 
    ```bash
    python manage.py migrate
    ```
4. Run server and open the link:
    ```bash
    python manage.py runserver
    ```
    and
    [localhost:8000/admin](http://127.0.0.1:8000/admin/)