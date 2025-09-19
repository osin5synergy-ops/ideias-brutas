#!/bin/bash

# Sandbox Environment Setup Script
# 2w3-0-sandbox-supply1-playbook5-machines

set -e

echo "🚀 Setting up ideias-brutas sandbox environment..."

# Check prerequisites
command -v docker >/dev/null 2>&1 || { echo "❌ Docker is required but not installed. Aborting." >&2; exit 1; }
command -v docker-compose >/dev/null 2>&1 || { echo "❌ Docker Compose is required but not installed. Aborting." >&2; exit 1; }

# Create necessary directories
echo "📁 Creating directories..."
mkdir -p ../docker/logs
mkdir -p /tmp/sandbox-data

# Initialize configuration
echo "⚙️  Initializing configuration..."
export SANDBOX_VERSION="2w3-0"
export ENVIRONMENT="sandbox"

# Build and start services
echo "🐳 Building and starting Docker services..."
cd ../docker
docker-compose build --no-cache
docker-compose up -d

# Wait for services to be ready
echo "⏳ Waiting for services to be ready..."
sleep 10

# Health check
echo "🔍 Performing health checks..."
docker-compose ps

echo "✅ Sandbox environment is ready!"
echo "📍 Access the application at: http://localhost:8080"
echo "📍 Database available at: localhost:5432"
echo "📍 Redis available at: localhost:6379"