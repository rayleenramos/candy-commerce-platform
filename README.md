# Candy Store Website

A Django web application for browsing and managing a candy store inventory.

## Features

- Browse available candies with prices and stock information
- View detailed information for each candy
- User authentication (login/logout)
- User account page
- Django admin panel for managing candies

## Setup

### Prerequisites

- Python 3.11 or higher
- pip

### Installation

*Note: These instructions are for Linux-based systems (macOS/Linux).*

1. Create and activate virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run database migrations:
   ```bash
   python manage.py migrate
   ```

4. Load initial candy data:
   ```bash
   python manage.py load_candies
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

### Code Formatting

Format code with Black before committing:
```bash
black .
```

## Usage

Once the server is running, access the application at http://127.0.0.1:8000/

**Admin Credentials:**
- Username: `admin`
- Password: `cps5301`

The admin user will be automatically created on first login.

## Project Structure

```
CandyStoreWebsite/
├── accounts/          # User authentication app
├── store/            # Main store app (candies)
├── candystore/       # Django project configuration
├── templates/        # Shared templates
└── manage.py         # Django management script
```

## Database

The application uses SQLite (`db.sqlite3`) for data storage. Candies are managed through the Django admin panel at http://127.0.0.1:8000/admin/

## Django Learning Resources

### Official Documentation
- [Django Documentation](https://docs.djangoproject.com/) - Official Django documentation
- [Django Tutorial](https://docs.djangoproject.com/en/stable/intro/tutorial01/) - Official step-by-step tutorial
- [Django Models](https://docs.djangoproject.com/en/stable/topics/db/models/) - Model documentation
- [Django Views](https://docs.djangoproject.com/en/stable/topics/http/views/) - Views and URL routing

### Tutorials and Courses
- [Django for Beginners](https://djangoforbeginners.com/) - Comprehensive beginner's guide
- [Real Python Django Tutorials](https://realpython.com/tutorials/django/) - Practical Django tutorials
- [Mozilla Django Tutorial](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django) - MDN web docs tutorial

### Key Concepts
- **Models**: Define data structure (`models.py`)
- **Views**: Handle HTTP requests and business logic (`views.py`)
- **Templates**: HTML presentation layer (`templates/`)
- **URLs**: Map URLs to views (`urls.py`)
- **Apps**: Self-contained modules grouping related functionality

## Copyright

This project was created for Kean University CPS 5301 Advanced Software Engineering class project. All rights reserved.
