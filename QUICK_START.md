# 🚀 Quick Start Guide

Get your FastAPI + PostgreSQL application running in under 2 minutes!

## Option 1: Automated Setup (Recommended)

```bash
# Run the initialization script
./init-project.sh
```

That's it! The script will:
- ✓ Check for Docker
- ✓ Create your .env file
- ✓ Start PostgreSQL and the API
- ✓ Run database migrations

**Access the app:** http://localhost:8000/api/v1/docs

---

## Option 2: Manual Setup

### With Docker (Easy)

```bash
# 1. Create environment file
cp .env.example .env

# 2. Start everything
docker-compose up -d

# 3. Run migrations
docker-compose exec api alembic upgrade head

# 4. Done! Open your browser
open http://localhost:8000/api/v1/docs
```

### Without Docker (Local Development)

```bash
# 1. Create virtual environment
python -m venv venv
source venv/bin/activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Create database
createdb fastapi_db

# 4. Setup environment
cp .env.example .env

# 5. Run migrations
alembic upgrade head

# 6. Start the server
uvicorn app.main:app --reload

# 7. Done! Open your browser
open http://localhost:8000/api/v1/docs
```

---

## 📝 First API Request

### Register a User

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

Copy the `access_token` from the response.

### Get Your Profile

```bash
curl -X GET "http://localhost:8000/api/v1/users/me" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN_HERE"
```

---

## 🎯 What's Next?

1. **Explore the API**: Open http://localhost:8000/api/v1/docs
2. **Read the docs**: Check out `README.md` and `SETUP.md`
3. **Add features**: Start building your API!

---

## 🛠️ Useful Commands

```bash
# View logs
docker-compose logs -f

# Stop the app
docker-compose down

# Restart the app
docker-compose restart

# Create a new migration
alembic revision --autogenerate -m "description"

# Run tests
pytest
```

---

## ❓ Having Issues?

Check `SETUP.md` for detailed troubleshooting or open an issue on GitHub.

**Happy coding! 🎉**

