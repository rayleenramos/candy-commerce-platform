# Candy Store Website

Full-stack e-commerce web application developed as a software engineering capstone project. Built with Django and MySQL/SQLite using Agile Scrum practices, the platform supports end-to-end shopping workflows including authentication, product management, cart and checkout, order tracking, and administrative controls.

## Features

- User authentication (registration, login, logout)
- Browse products with pricing and stock availability
- Detailed product pages
- Shopping cart and checkout workflow
- Order creation, history, and tracking
- Admin dashboard for managing products and inventory
- Role-based access via Django Admin

## Tech Stack

- Backend: Django (Python)
- Frontend: HTML, CSS, Tailwind
- Database: SQLite (development)
- Tools: Git, GitHub, Agile Scrum
- Formatting: Black

## Contributions

This was a team-based software engineering project.
My primary responsibilities included:
- Scrum Master responsibilities and sprint coordination
- Backend development for orders and cart workflows
- Database modeling and migrations
- Frontend template integration
- Feature testing and debugging

## Database

The application uses SQLite (`db.sqlite3`) for data storage. Candies are managed through the Django admin panel at http://127.0.0.1:8000/admin/


## Setup

### Prerequisites

- Python 3.11 or higher
- pip

### Run Locally

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

## Usage

Once the server is running, access the application at http://127.0.0.1:8000/

## Project Structure

```
candystore/
├── accounts/      # User authentication
├── orders/        # Cart and order workflows
├── store/         # Product management
├── templates/     # Shared templates
├── candystore/   # Django configuration
└── manage.py
```

## Copyright

This project was created for Kean University CPS 5301 Advanced Software Engineering class project. 
