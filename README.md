
# Library Management API

A RESTful Library Management API built with Django and Django REST Framework. This project is part of my backend development learning journey, where I am practicing Django REST Framework concepts through a practical library management system.

The project is being developed incrementally, starting with basic CRUD operations and gradually moving toward relational data handling and more advanced API development concepts.

## Project Overview

The Library Management API is designed to manage library resources such as authors, categories, and books.

The primary goal is to build a structured backend application while gaining practical experience with Django, Django REST Framework, PostgreSQL, and REST API development.

## Tech Stack

- **Language:** Python
- **Backend Framework:** Django
- **API Framework:** Django REST Framework (DRF)
- **Database:** PostgreSQL
- **Database Management:** pgAdmin
- **Environment Variables:** python-dotenv
- **API Testing:** Postman
- **Development Environment:** Visual Studio Code

## Project Goals

- Build a RESTful API using Django REST Framework.
- Understand APIView and HTTP methods through practical implementation.
- Practice ModelSerializer and data validation.
- Implement CRUD operations for different resources.
- Understand ForeignKey relationships between Django models.
- Work with dynamic URL parameters and custom URL slugs.
- Practice database operations using Django ORM.
- Learn to structure and organize a Django backend project.

## Implemented Features

### 1. Author Management

- Create new authors.
- Retrieve all authors.
- Retrieve a specific author using ID or slug.
- Update author information using PUT.
- Partially update author information using PATCH.
- Delete authors.
- Automatically generate unique slugs.
- Handle duplicate slugs using numeric suffixes.

### 2. Category Management

- Create new categories.
- Retrieve all categories.
- Retrieve a specific category using ID or slug.
- Update category information using PUT.
- Partially update category information using PATCH.
- Delete categories.
- Automatically generate unique slugs.
- Handle duplicate slugs using numeric suffixes.

### 3. Database Configuration

- PostgreSQL database integration.
- Environment variable configuration using `.env`.
- Sensitive environment variables excluded through `.gitignore`.
- Django migrations and database management.

### 4. Django Admin

- Registered Author, Category, and Book models.
- Configured list displays.
- Added search and filtering options.
- Configured automatic slug population in Django Admin.

## API Endpoints

Base URL:

```text
http://127.0.0.1:8000/api/
```

### Author Endpoints

| HTTP Method | Endpoint | Description |
|---|---|---|
| GET | `/authors/` | Retrieve all authors |
| POST | `/authors/` | Create a new author |
| GET | `/author/<identifier>/` | Retrieve an author by ID or slug |
| PUT | `/author/<identifier>/` | Fully update an author |
| PATCH | `/author/<identifier>/` | Partially update an author |
| DELETE | `/author/<identifier>/` | Delete an author |

### Category Endpoints

| HTTP Method | Endpoint | Description |
|---|---|---|
| GET | `/categories/` | Retrieve all categories |
| POST | `/categories/` | Create a new category |
| GET | `/category/<identifier>/` | Retrieve a category by ID or slug |
| PUT | `/category/<identifier>/` | Fully update a category |
| PATCH | `/category/<identifier>/` | Partially update a category |
| DELETE | `/category/<identifier>/` | Delete a category |

`<identifier>` accepts either a numeric ID or a slug.

Example:

```text
/api/v1/author/14/
/api/v1/author/stan-lee/
/api/v1/category/5/
/api/v1/category/fiction/
```

## Models

The project currently includes three main models:

### AuthorModel

- name
- slug
- biography
- created_at

### CategoryModel

- name
- slug
- description
- created_at

### BookModel

- title
- slug
- description
- author (ForeignKey)
- category (ForeignKey)
- isbn
- published year
- available copies
- created_at

The Book model establishes relationships with Author and Category using ForeignKey fields.

## Key Concepts Practiced

- Django Models
- Django ORM
- Django Admin
- Django REST Framework APIView
- ModelSerializer
- Serializer validation
- CRUD operations
- HTTP methods: GET, POST, PUT, PATCH, DELETE
- HTTP status codes
- QuerySet and `objects.all()`
- `get_object_or_404()`
- Dynamic URL parameters
- Slug generation using `slugify()`
- Custom model `save()` methods
- ForeignKey relationships
- `on_delete=PROTECT`
- `related_name`
- Environment variable management
- PostgreSQL integration

## Installation and Setup

### 1. Clone the repository

```bash
git clone <https://github.com/nrshakib/Library-Management-System-API>
```

### 2. Navigate to the project directory

```bash
cd Library Management System API
```

### 3. Create a virtual environment

```bash
py -m venv venv
```

### 4. Activate the virtual environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install django djangorestframework "psycopg[binary]" python-dotenv
```

### 6. Configure environment variables

Create a `.env` file in the project root directory.

```env
SECRET_KEY=your-secret-key
DEBUG=True

DB_NAME=library_management_db
DB_USER=postgres
DB_PASSWORD=your-database-password
DB_HOST=localhost
DB_PORT=5432
```

Update the database credentials according to your PostgreSQL configuration.

### 7. Create the PostgreSQL database

Create a database named:

```text
library_management_db
```

You can create and manage the database using pgAdmin.

### 8. Run migrations

```bash
py manage.py makemigrations
py manage.py migrate
```

### 9. Create a superuser

```bash
py manage.py createsuperuser
```

### 10. Start the development server

```bash
py manage.py runserver
```

The API will be available at:

```text
http://127.0.0.1:8000/api/
```

Django Admin:

```text
http://127.0.0.1:8000/admin/
```

## Upcoming Features

The following features are planned for future development:

- [ ] Complete Book CRUD API.
- [ ] Implement nested serializers.
- [ ] Handle ForeignKey relationships in API requests.
- [ ] Add Book filtering and searching.
- [ ] Add ordering functionality.
- [ ] Implement pagination.
- [ ] Improve serializer-level validation.
- [ ] Practice advanced Django ORM queries.
- [ ] Add API testing.
- [ ] Improve API response consistency and error handling.

## Learning Outcomes

Through this project, I aim to strengthen my understanding of Django REST Framework and gain practical experience in:

- Building RESTful APIs from scratch.
- Designing relational database models.
- Handling one-to-many relationships.
- Structuring reusable serializers and API views.
- Implementing clean and maintainable CRUD operations.
- Managing PostgreSQL databases.
- Following better backend development practices.

## Project Status

**Currently in Development**

Author and Category CRUD APIs have been implemented.
Book API development and additional features are planned for upcoming stages.

---

**Built as part of my advanced backend learning journey with Django REST Framework.**
