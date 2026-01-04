# Setup Guide

## Quick Start with Docker (Recommended)

This is the easiest way to get started. Docker will handle all dependencies and setup for you.

### Step 1: Create Environment File

```bash
# Copy the example environment file
cp .env.example .env

# Optional: Edit .env if you want to change any settings
nano .env
```

### Step 2: Start the Application

```bash
# Build and start all services (PostgreSQL + API)
docker-compose up -d

# Wait a few seconds for PostgreSQL to be ready, then run migrations
docker-compose exec api alembic upgrade head
```

### Step 3: Verify Everything Works

1. Open your browser and go to: http://localhost:8000/api/v1/docs
2. You should see the Swagger UI with all API endpoints

### Step 4: Create Your First User

Using the Swagger UI:
1. Find the **POST /api/v1/auth/register** endpoint
2. Click "Try it out"
3. Fill in the request body:
```json
{
  "email": "admin@example.com",
  "username": "admin",
  "password": "admin123",
  "full_name": "Admin User"
}
```
4. Click "Execute"

### Step 5: Login and Get Access Token

1. Find the **POST /api/v1/auth/login** endpoint
2. Click "Try it out"
3. Fill in:
   - username: `admin`
   - password: `admin123`
4. Click "Execute"
5. Copy the `access_token` from the response

### Step 6: Test Authenticated Endpoints

1. Click the "Authorize" button at the top of the Swagger UI
2. Paste your access token (just the token, no "Bearer" prefix)
3. Click "Authorize"
4. Now try the **GET /api/v1/users/me** endpoint to see your user information

---

## Local Development Setup (Without Docker)

If you prefer to run everything locally without Docker:

### Prerequisites

- Python 3.11 or higher
- PostgreSQL 15 or higher installed and running

### Step 1: Create a Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate it
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Set Up PostgreSQL Database

```bash
# Create the database
createdb fastapi_db

# Or using psql:
psql -U postgres
CREATE DATABASE fastapi_db;
\q
```

### Step 4: Configure Environment

```bash
# Copy example environment file
cp .env.example .env

# Edit .env with your database credentials
# Make sure DATABASE_URL matches your PostgreSQL setup
```

### Step 5: Run Migrations

```bash
alembic upgrade head
```

### Step 6: Start the Application

```bash
# Development mode with auto-reload
uvicorn app.main:app --reload

# Or using the Makefile
make dev
```

### Step 7: Access the Application

Open http://localhost:8000/api/v1/docs in your browser

---

## Using the Makefile

The project includes a Makefile with helpful commands:

```bash
# Install dependencies
make install

# Run development server
make dev

# Start Docker containers
make docker-up

# Stop Docker containers
make docker-down

# Run database migrations
make migrate

# Create a new migration
make migration

# Run tests
make test

# Format code
make format

# Clean cache files
make clean
```

---

## Database Migrations

### Create a New Migration

After modifying your models in `app/models/`:

```bash
# Using Alembic directly
alembic revision --autogenerate -m "Add new table"

# Or using Makefile
make migration
```

### Apply Migrations

```bash
# Apply all pending migrations
alembic upgrade head

# Or using Makefile
make migrate
```

### Rollback a Migration

```bash
# Rollback one migration
alembic downgrade -1

# Rollback to specific revision
alembic downgrade <revision_id>

# Rollback all migrations
alembic downgrade base
```

---

## Common Issues and Solutions

### Issue: Port 5432 is already in use

**Solution:** Another PostgreSQL instance is running. Either:
- Stop the other instance
- Change the port in `docker-compose.yml` (e.g., `"5433:5432"`)

### Issue: Port 8000 is already in use

**Solution:** Another application is using port 8000. Either:
- Stop the other application
- Change the port in `docker-compose.yml` or when running uvicorn

### Issue: Database connection errors

**Solution:** 
- Verify PostgreSQL is running: `docker-compose ps` (for Docker) or `pg_isready` (for local)
- Check your database credentials in `.env`
- Ensure the database exists

### Issue: Import errors

**Solution:**
- Make sure you're in the virtual environment: `source venv/bin/activate`
- Reinstall dependencies: `pip install -r requirements.txt`

### Issue: Migration errors

**Solution:**
- Check if database exists and is accessible
- Try resetting migrations: `alembic downgrade base` then `alembic upgrade head`
- Check Alembic configuration in `alembic.ini` and `alembic/env.py`

---

## Next Steps

After setting up, you might want to:

1. **Add More Models**: Create new models in `app/models/`
2. **Add New Endpoints**: Create new route files in `app/api/v1/endpoints/`
3. **Add Tests**: Add test files in `tests/`
4. **Configure CORS**: Update `BACKEND_CORS_ORIGINS` in `.env`
5. **Set Up Production**: See README.md for production deployment tips

---

## Useful Commands

### Docker Commands

```bash
# View logs
docker-compose logs -f api

# Execute commands in the API container
docker-compose exec api bash

# Rebuild containers
docker-compose up -d --build

# Remove everything including volumes
docker-compose down -v
```

### Database Commands

```bash
# Connect to PostgreSQL (Docker)
docker-compose exec db psql -U postgres -d fastapi_db

# Connect to PostgreSQL (local)
psql -U postgres -d fastapi_db

# Backup database
pg_dump -U postgres fastapi_db > backup.sql

# Restore database
psql -U postgres fastapi_db < backup.sql
```

---

## Support

If you encounter any issues:
1. Check the logs: `docker-compose logs -f` (Docker) or terminal output (local)
2. Verify all services are running: `docker-compose ps`
3. Check the README.md for more detailed information
4. Open an issue on the repository

