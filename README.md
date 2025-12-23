# Project HIM - Church Management System

A modern church management system API built with FastAPI for managing members, classes, attendance, and organizational administration.

## 📋 Table of Contents

- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Prerequisites](#-prerequisites)
- [Quick Start](#-quick-start)
- [Project Structure](#-project-structure)
- [Configuration](#-configuration)
- [Database Setup](#-database-setup)
- [Running the Application](#-running-the-application)
- [API Documentation](#-api-documentation)
- [Development](#-development)
- [Testing](#-testing)
- [Deployment](#-deployment)
- [Contributing](#-contributing)

---

## ✨ Features

### User Management
- Organization and department administrators
- Member profiles with personal information
- Role-based access control (Admin, Teacher, Member)
- OAuth2 authentication support

### Class Management
- Create and manage classes with schedules
- Teacher assignments
- Room reservations
- Schedule conflict detection
- Class capacity management

### Member Management
- Detailed member profiles (birthday, contact info, baptism records)
- Family relationship tracking
- Photo uploads
- Custom field support per department

### Attendance & Check-in
- QR code-based check-in system
- Attendance tracking and history
- Automated name tag generation

### Data Management
- CSV/Excel import and export
- Bulk member operations
- Custom reporting

---

## 🛠 Tech Stack

- **Framework**: FastAPI 0.126.0
- **Database**: PostgreSQL or MySQL
- **ORM**: SQLAlchemy 2.0.45 (async)
- **Authentication**: JWT tokens (python-jose)
- **Validation**: Pydantic 2.10.4
- **Migrations**: Alembic 1.14.0
- **Testing**: Pytest 8.3.4
- **Server**: Uvicorn 0.34.0

---

## 📦 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.11+** ([Download](https://www.python.org/downloads/))
- **PostgreSQL 13+** or **MySQL 8+** ([PostgreSQL](https://www.postgresql.org/download/), [MySQL](https://dev.mysql.com/downloads/))
- **Git** ([Download](https://git-scm.com/downloads))
- **Conda** - Optional ([Download](https://docs.conda.io/projects/conda/en/stable/user-guide/install/index.html))

---

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/project-him.git
cd project-him/backend
```

### 2. Create Virtual Environment

with terminal enviroment
```bash
# Create virtual environment
python -m venv venv

# Activate it
# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```
with conda (install miniconda or anaconda)
```bash
# Create virtual environment
conda create -n venv # venv is the env name

# Activate it
conda activate venv

# Deactivate it
conda deactivate venv
```

### 3. Install Dependencies

```bash
# Upgrade pip
pip install --upgrade pip

# Install all dependencies
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

```bash
# Copy example env file
cp .env.example .env

# Edit .env with your settings
nano .env  # or use your favorite editor
```

**Required changes in `.env`:**
- `DB_PASSWORD` - Your database password
- `SECRET_KEY` - Generate with: `openssl rand -hex 32`
- `DB_TYPE` - Choose "postgresql" or "mysql"

### 5. Create Database

**PostgreSQL:**
```bash
psql -U postgres
CREATE DATABASE project_him_db;
\q
```

**MySQL:**
```bash
mysql -u root -p
CREATE DATABASE project_him_db;
exit;
```

### 6. Run Database Migrations

```bash
# Initialize Alembic (first time only)
alembic init alembic

# Create initial migration
alembic revision --autogenerate -m "Initial migration"

# Apply migrations
alembic upgrade head
```

### 7. Run the Application

```bash
# Development mode (with auto-reload)
uvicorn app.main:app --reload

# Or use Python directly
python -m app.main
```

The API will be available at: **http://localhost:8000**

### 8. Access API Documentation

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

---

## 📁 Project Structure

```
Project_HIM/
├── backend/
│   ├── api/                 # API endpoints
│   │   ├── auth.py
│   │   ├── user.py
│   │   ├── member.py
│   │   ├── department.py
│   │   ├── room.py
│   │   └── classes.py
│   │
│   ├── config/                 # Configuration files
│   │   ├── settings.py         # App settings (from .env)
│   │   └── database.py         # Database connection
│   │
│   ├── models/                 # Database models
│   │   ├── user.py
│   │   ├── member.py
│   │   ├── organization.py
│   │   ├── class_model.py
│   │   └── room.py
│   │
│   ├── repositories/           # Data Access Layer
│   │   ├── interfaces/         # Repository interfaces
│   │   └── implementations/    # SQLAlchemy implementations
│   │
│   ├── schemas/                # Data Transfer Objects
│   │   ├── requests/           # Request schemas
│   │   └── responses/          # Response schemas
│   │
│   ├── services/               # Business Logic Layer
│   │   ├── interfaces/         # Service interfaces
│   │   └── implementations/    # Service implementations
│   │
│   ├── utils/                  # Helper functions
│   ├── exceptions/             # Custom exceptions
│   ├── middleware/             # Middleware
│   ├── dependencies.py         # Dependency injection
│   └── main.py                 # Application entry point
│
├── tests/                      # Test files
├── uploads/                    # Uploaded files
├── .env                        # Environment variables (NOT in git)
├── .env.example                # Environment template
├── .gitignore                  # Git ignore rules
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

---

## ⚙️ Configuration

### Environment Variables

All configuration is managed through environment variables in the `.env` file:

```bash
# Application
APP_NAME=Project HIM API
DEBUG=True
ENVIRONMENT=development

# Database
DB_TYPE=postgresql              # or "mysql"
DB_HOST=localhost
DB_PORT=5432                    # 3306 for MySQL
DB_USER=postgres
DB_PASSWORD=your_password_here
DB_NAME=project_him_db

# Security
SECRET_KEY=your_generated_secret_key
ACCESS_TOKEN_EXPIRE_MINUTES=30

# CORS
ALLOWED_ORIGINS=http://localhost:3000,http://localhost:5173

# File Uploads
MAX_UPLOAD_SIZE=10485760        # 10MB
UPLOAD_DIR=uploads
```

### Generate Secret Key

```bash
openssl rand -hex 32
```

---

## 💾 Database Setup

### PostgreSQL Setup

```bash
# Install PostgreSQL (Ubuntu/Debian)
sudo apt-get install postgresql postgresql-contrib

# Start PostgreSQL service
sudo systemctl start postgresql

# Create database
sudo -u postgres createdb project_him_db

# Create user (optional)
sudo -u postgres createuser --interactive
```

### MySQL Setup

```bash
# Install MySQL (Ubuntu/Debian)
sudo apt-get install mysql-server

# Start MySQL service
sudo systemctl start mysql

# Secure installation
sudo mysql_secure_installation

# Create database
mysql -u root -p
CREATE DATABASE project_him_db;
GRANT ALL PRIVILEGES ON project_him_db.* TO 'your_user'@'localhost';
FLUSH PRIVILEGES;
```
<!-- 
### Database Migrations

```bash
# Create a new migration
alembic revision --autogenerate -m "Description of changes"

# Apply migrations
alembic upgrade head

# Rollback last migration
alembic downgrade -1

# View migration history
alembic history
``` -->

---

## 🏃 Running the Application

### Development Mode

```bash
# With auto-reload (recommended for development)
uvicorn app.main:app --reload

# Custom host and port
uvicorn app.main:app --host 0.0.0.0 --port 8080 --reload

# Using Python directly
python -m app.main
```

### Production Mode

```bash
# Using Uvicorn with multiple workers
uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4

# Using Gunicorn with Uvicorn workers
gunicorn app.main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

---

## 📚 API Documentation

Once the application is running, access the interactive API documentation:

### Swagger UI (Interactive)
**URL**: http://localhost:8000/docs

Features:
- Try out API endpoints directly
- View request/response schemas
- Test authentication

### ReDoc (Documentation)
**URL**: http://localhost:8000/redoc

Features:
- Clean, readable documentation
- Downloadable OpenAPI spec
- Search functionality

<!-- ### Example API Endpoints

```bash
# Health check
GET http://localhost:8000/health

# Get all users
GET http://localhost:8000/user/

# Create a user
POST http://localhost:8000/user/create
Content-Type: application/json
{
  "email": "user@example.com",
  "full_name": "John Doe",
  "role": "member"
}

# Login
POST http://localhost:8000/auth/login
Content-Type: application/x-www-form-urlencoded
username=user@example.com&password=password123
``` -->

---

## 🔧 Development

### Project Architecture

The project follows a **layered architecture** with dependency injection:

```
Routes (API Endpoints)
    ↓
Services (Business Logic)
    ↓
Repositories (Data Access)
    ↓
Database
```

### Adding a New Feature

1. **Create Model** (`app/models/your_model.py`)
```python
from app.config.database import Base
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID

class YourModel(Base):
    __tablename__ = "your_table"
    id = Column(UUID(as_uuid=True), primary_key=True)
    name = Column(String(100))
```

2. **Create Repository Interface** (`app/repositories/interfaces/iyour_repository.py`)
```python
from abc import ABC, abstractmethod

class IYourRepository(ABC):
    @abstractmethod
    async def get_all(self):
        pass
```

3. **Implement Repository** (`app/repositories/implementations/sqlalchemy/your_repository.py`)
```python
class YourRepository(IYourRepository):
    async def get_all(self):
        # Implementation
        pass
```

4. **Create Service** (`app/services/implementations/your_service.py`)
```python
class YourService:
    def __init__(self, repository: IYourRepository):
        self.repository = repository
```

5. **Create Routes** (`app/routes/your_routes.py`)
```python
@router.get("/your-endpoint")
async def get_items(service: YourService = Depends(get_your_service)):
    return await service.get_all()
```

6. **Register in main.py**
```python
app.include_router(your_routes.router)
```

### Code Style

```bash
# Format code with Ruff
ruff format .

# Lint code
ruff check .

# Type checking with mypy
mypy app/
```

---

## 🧪 Testing

### Run Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=app --cov-report=html

# Run specific test file
pytest tests/test_user_service.py

# Run with verbose output
pytest -v
```

<!-- ### Writing Tests

```python
# tests/test_user_service.py
import pytest
from app.services.implementations.user_service import UserService

@pytest.mark.asyncio
async def test_create_user(mock_user_repository):
    service = UserService(mock_user_repository)
    user = await service.create_user(...)
    assert user.email == "test@example.com"
```

--- -->

## 🚀 Deployment

### Using Docker (Recommended)

```dockerfile
# Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

```bash
# Build image
docker build -t project-him-api .

# Run container
docker run -p 8000:8000 --env-file .env project-him-api
```

### Using Docker Compose

```yaml
# docker-compose.yml
version: '3.8'

services:
  api:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DB_HOST=db
    depends_on:
      - db
  
  db:
    image: postgres:15
    environment:
      POSTGRES_DB: project_him_db
      POSTGRES_PASSWORD: ${DB_PASSWORD}
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```

```bash
# Start services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```
<!-- 
### Environment-Specific Deployment

```bash
# Staging
cp .env.staging .env
uvicorn app.main:app --host 0.0.0.0 --port 8000

# Production
cp .env.production .env
gunicorn app.main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker
``` -->

---

## 🤝 Contributing

### Getting Started

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

<!-- ### Coding Standards

- Follow PEP 8 style guide
- Write docstrings for all functions/classes
- Add type hints
- Write tests for new features
- Update documentation

### Commit Message Format

```
type(scope): subject

body (optional)

footer (optional)
```

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

Example:
```
feat(auth): add OAuth2 Google login

- Implement Google OAuth2 provider
- Add redirect URL handling
- Update user model with provider_id

Closes #123
```

--- -->

## 🐛 Troubleshooting

### Common Issues

**Database Connection Error**
```
Solution: Check DB_HOST, DB_PORT, DB_USER, DB_PASSWORD in .env
```

**Module Not Found**
```
Solution: Activate virtual environment and reinstall dependencies
pip install -r requirements.txt
```

<!-- **Alembic Migration Conflicts**
```
Solution: Check migration history and resolve conflicts
alembic history
alembic downgrade -1
``` -->

**Port Already in Use**
```
Solution: Kill process on port 8000 or use different port
lsof -ti:8000 | xargs kill -9  # macOS/Linux
uvicorn app.main:app --port 8080  # Use different port
```

---

<!-- ## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

--- -->

## 👥 Authors

- **Your Name** - Initial work - [gy180](https://github.com/gy180)

---

## 🙏 Acknowledgments

- FastAPI for the amazing framework
- SQLAlchemy for powerful ORM
- The open-source community

---
<!-- 
## 📞 Support

For support, email support@projecthim.org or open an issue on GitHub.

--- -->
