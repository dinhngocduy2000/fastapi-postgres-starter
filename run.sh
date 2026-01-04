#!/bin/bash

# Startup script for FastAPI application

echo "🚀 Starting FastAPI PostgreSQL Application..."

# Wait for PostgreSQL to be ready
echo "⏳ Waiting for PostgreSQL to be ready..."
while ! pg_isready -h localhost -p 5432 -U postgres 2>/dev/null; do
    sleep 1
done

echo "✅ PostgreSQL is ready!"

# Run database migrations
echo "📊 Running database migrations..."
alembic upgrade head

echo "✅ Migrations completed!"

# Start the application
echo "🎉 Starting the application..."
uvicorn app.cmd.main:app --host 0.0.0.0 --port 8000 --reload

