#!/bin/bash

# FastAPI PostgreSQL Starter - Initialization Script
# This script helps you set up the project quickly

set -e

echo "🚀 FastAPI PostgreSQL Starter - Initialization Script"
echo "======================================================"
echo ""

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to print colored output
print_success() {
    echo -e "${GREEN}✓ $1${NC}"
}

print_info() {
    echo -e "${BLUE}ℹ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠ $1${NC}"
}

print_error() {
    echo -e "${RED}✗ $1${NC}"
}

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    print_warning "Docker is not installed. You'll need to set up the project manually."
    print_info "See SETUP.md for local development setup instructions."
    exit 1
fi

print_success "Docker is installed"

# Check if Docker Compose is installed
if ! command -v docker-compose &> /dev/null; then
    print_error "Docker Compose is not installed"
    print_info "Please install Docker Compose: https://docs.docker.com/compose/install/"
    exit 1
fi

print_success "Docker Compose is installed"

# Create .env file if it doesn't exist
if [ ! -f .env ]; then
    print_info "Creating .env file from .env.example..."
    if [ -f .env.example ]; then
        cp .env.example .env
        print_success ".env file created"
    else
        print_error ".env.example not found"
        exit 1
    fi
else
    print_success ".env file already exists"
fi

echo ""
print_info "Starting Docker containers..."
echo ""

# Start Docker containers
docker-compose up -d

echo ""
print_info "Waiting for PostgreSQL to be ready..."
sleep 5

# Check if containers are running
if ! docker-compose ps | grep -q "Up"; then
    print_error "Failed to start containers"
    print_info "Run 'docker-compose logs' to see what went wrong"
    exit 1
fi

print_success "Containers are running"

echo ""
print_info "Running database migrations..."
echo ""

# Run migrations
docker-compose exec -T api alembic upgrade head

if [ $? -eq 0 ]; then
    print_success "Database migrations completed"
else
    print_error "Migration failed"
    print_info "You can try running: docker-compose exec api alembic upgrade head"
fi

echo ""
echo "======================================================"
print_success "Setup complete!"
echo "======================================================"
echo ""
print_info "Your FastAPI application is now running!"
echo ""
echo "📍 Access points:"
echo "   • API Documentation: http://localhost:8000/api/v1/docs"
echo "   • Alternative Docs:  http://localhost:8000/api/v1/redoc"
echo "   • Health Check:      http://localhost:8000/health"
echo ""
print_info "Useful commands:"
echo "   • View logs:         docker-compose logs -f"
echo "   • Stop services:     docker-compose down"
echo "   • Restart services:  docker-compose restart"
echo ""
print_info "Next steps:"
echo "   1. Open http://localhost:8000/api/v1/docs in your browser"
echo "   2. Register a new user using the /auth/register endpoint"
echo "   3. Login to get an access token using the /auth/login endpoint"
echo "   4. Explore the API!"
echo ""
print_info "For more information, see SETUP.md and README.md"
echo ""

