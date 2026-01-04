# FastAPI PostgreSQL Starter

A production-ready FastAPI project template with PostgreSQL database integration, featuring async support, authentication, and database migrations.

## Features

- ⚡ **FastAPI** - Modern, fast web framework for building APIs
- 🐘 **PostgreSQL** - Powerful, open-source relational database
- 🔄 **Async/Await** - Full async support with SQLAlchemy 2.0
- 🔐 **Authentication** - JWT-based authentication system
- 📊 **Database Migrations** - Alembic for database schema management
- 🐳 **Docker** - Containerized application and database
- 📝 **API Documentation** - Auto-generated with Swagger UI and ReDoc
- ✅ **Type Safety** - Pydantic models for request/response validation

## Project Structure

```
fastapi-postgres-starter/
├── app/
│   ├── api/
│   │   ├── deps.py              # Dependencies (auth, db session)
│   │   └── v1/
│   │       ├── api.py           # API router
│   │       └── endpoints/
│   │           ├── auth.py      # Authentication endpoints
│   │           └── users.py     # User endpoints
│   ├── core/
│   │   ├── config.py            # Settings and configuration
│   │   ├── database.py          # Database connection
│   │   └── security.py          # JWT and password hashing
│   ├── crud/
│   │   └── user.py              # CRUD operations for users
│   ├── models/
│   │   └── user.py              # SQLAlchemy models
│   ├── schemas/
│   │   └── user.py              # Pydantic schemas
│   └── main.py                  # FastAPI application
├── alembic/
│   ├── versions/                # Migration files
│   └── env.py                   # Alembic configuration
├── .env.example                 # Environment variables example
├── .gitignore                   # Git ignore file
├── alembic.ini                  # Alembic configuration
├── docker-compose.yml           # Docker Compose configuration
├── Dockerfile                   # Docker image configuration
├── requirements.txt             # Python dependencies
└── README.md                    # This file
```

## Prerequisites

- Python 3.11+
- PostgreSQL 15+ (or use Docker)
- Docker and Docker Compose (optional)

## Quick Start

### Option 1: Using Docker (Recommended)

1. **Clone the repository**
   ```bash
   cd fastapi-postgres-starter
   ```

2. **Create environment file**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

3. **Start the application**
   ```bash
   docker-compose up -d
   ```

4. **Run database migrations**
   ```bash
   docker-compose exec api alembic upgrade head
   ```

5. **Access the API**
   - API Documentation: http://localhost:8000/api/v1/docs
   - Alternative Docs: http://localhost:8000/api/v1/redoc
   - Health Check: http://localhost:8000/health

### Option 2: Local Development

1. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up PostgreSQL**
   - Install PostgreSQL locally
   - Create a database: `createdb fastapi_db`
   - Update `.env` with your database credentials

4. **Create environment file**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

5. **Run database migrations**
   ```bash
   alembic upgrade head
   ```

6. **Start the development server**
   ```bash
   uvicorn app.main:app --reload
   ```

7. **Access the API**
   - API Documentation: http://localhost:8000/api/v1/docs

## Database Migrations

Create a new migration:
```bash
alembic revision --autogenerate -m "Description of changes"
```

Apply migrations:
```bash
alembic upgrade head
```

Rollback migration:
```bash
alembic downgrade -1
```

## API Endpoints

### Authentication

- **POST** `/api/v1/auth/register` - Register a new user
- **POST** `/api/v1/auth/login` - Login and get access token

### Users

- **GET** `/api/v1/users/me` - Get current user information
- **PUT** `/api/v1/users/me` - Update current user information
- **GET** `/api/v1/users/` - Get all users (superuser only)
- **GET** `/api/v1/users/{user_id}` - Get user by ID (superuser only)
- **DELETE** `/api/v1/users/{user_id}` - Delete user (superuser only)

## Example Usage

### Register a new user

```bash
curl -X POST "http://localhost:8000/api/v1/auth/register" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "username": "testuser",
    "password": "password123",
    "full_name": "Test User"
  }'
```

### Login

```bash
curl -X POST "http://localhost:8000/api/v1/auth/login" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=testuser&password=password123"
```

### Get current user information

```bash
curl -X GET "http://localhost:8000/api/v1/users/me" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

## Environment Variables

Key environment variables (see `.env.example` for all options):

```bash
# Application
APP_NAME="FastAPI PostgreSQL Starter"
DEBUG=True

# Database
DATABASE_URL=postgresql+asyncpg://postgres:postgres@localhost:5432/fastapi_db
DATABASE_URL_SYNC=postgresql://postgres:postgres@localhost:5432/fastapi_db

# Security
SECRET_KEY=your-secret-key-here-change-in-production
ACCESS_TOKEN_EXPIRE_MINUTES=30

# CORS
BACKEND_CORS_ORIGINS=["http://localhost:3000"]
```

## Development

### Running Tests

```bash
pytest
```

### Code Quality

Install development dependencies:
```bash
pip install black flake8 mypy
```

Format code:
```bash
black app/
```

Lint code:
```bash
flake8 app/
```

Type check:
```bash
mypy app/
```

## Production Deployment

1. Set `DEBUG=False` in `.env`
2. Use a strong `SECRET_KEY`
3. Configure proper CORS origins
4. Use environment-specific database credentials
5. Set up SSL/TLS certificates
6. Use a reverse proxy (e.g., Nginx)
7. Enable logging and monitoring
8. Use production-grade WSGI server (already using uvicorn)

## Technologies Used

- **FastAPI** - Web framework
- **SQLAlchemy** - ORM
- **Alembic** - Database migrations
- **PostgreSQL** - Database
- **Pydantic** - Data validation
- **python-jose** - JWT handling
- **passlib** - Password hashing
- **uvicorn** - ASGI server
- **Docker** - Containerization

## License

This project is licensed under the MIT License.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Support

If you have any questions or issues, please open an issue on the repository.

