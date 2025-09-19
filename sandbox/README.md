# Sandbox Environment Configuration

This directory contains the sandbox environment setup for development and testing.

## Components

- `config/`: Environment configuration files
- `docker/`: Docker compose and container definitions
- `scripts/`: Setup and utility scripts

## Usage

1. Run `./scripts/setup.sh` to initialize the sandbox environment
2. Use `docker-compose up` to start all services
3. Access the environment at `http://localhost:8080`

## Requirements

- Docker and Docker Compose
- Node.js 18+ (for local development)
- Python 3.9+ (for automation scripts)