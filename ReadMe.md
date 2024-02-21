## Django Task CRUD Application
This Django project is designed to perform CRUD (Create, Read, Update, Delete) operations on tasks. It includes a table with fields for title, description, and completion status.

## Installation
Follow these steps to set up and run the project locally:

1. Clone the Repository
``` shell
git clone <repository-url>
```

2. Install Dependencies
``` shell
pip install .
or
pip3 install .
```

3. Set up the Database
``` shell
python manage.py migrate
or
python3 manage.py migrate 
```

4. Create a Superuser (Optional)
``` shell
python manage.py createsuperuser
or
python3 manage.py createsuperuser
```

8. Run the Development Server
``` shell
python manage.py runserver
or
python3 manage.py runserver
```

The project will be accessible at http://127.0.0.1:8000/.

## Usage
Once the development server is running, you can access the application in your web browser. Use the provided CRUD functionalities to manage tasks.

