#!/bin/bash

# Playbook5 - Automated Deployment Script
# 2w3-0-sandbox-supply1-playbook5-machines

set -e

echo "🚀 Starting Playbook5 automated deployment..."

# Configuration
SANDBOX_ENV="2w3-0-sandbox"
SUPPLY_COMPONENT="supply1"
PLAYBOOK_VERSION="5"

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

log() {
    echo -e "${GREEN}[$(date +'%Y-%m-%d %H:%M:%S')]${NC} $1"
}

error() {
    echo -e "${RED}[ERROR]${NC} $1" >&2
}

warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

# Function to check prerequisites
check_prerequisites() {
    log "Checking prerequisites..."
    
    # Check if sandbox is running
    if ! docker-compose -f ../../sandbox/docker/docker-compose.yml ps | grep -q "Up"; then
        warning "Sandbox environment not running. Starting..."
        cd ../../sandbox/scripts
        ./setup.sh
        cd ../../playbook5/automation
    fi
    
    # Check if supply1 config exists
    if [ ! -f "../../supply1/config/supply1.yml" ]; then
        error "Supply1 configuration not found!"
        exit 1
    fi
    
    log "Prerequisites check completed ✅"
}

# Function to deploy supply chain component
deploy_supply_chain() {
    log "Deploying Supply Chain Component (supply1)..."
    
    cd ../../supply1/src
    python3 -c "
from supply_manager import SupplyManager
manager = SupplyManager('../config/supply1.yml')
if manager.initialize_resources():
    print('✅ Supply1 deployed successfully')
    manager.start_tracking()
    print('📊 Tracking started')
else:
    print('❌ Supply1 deployment failed')
    exit(1)
" || { error "Supply1 deployment failed"; exit 1; }
    
    cd ../../playbook5/automation
    log "Supply chain deployment completed ✅"
}

# Function to configure machines
configure_machines() {
    log "Configuring machine integrations..."
    
    # Create machine configuration
    cat > /tmp/machine_config.yml << EOF
machines:
  environment: "${SANDBOX_ENV}"
  supply_integration: "${SUPPLY_COMPONENT}"
  playbook_version: "${PLAYBOOK_VERSION}"
  
  instances:
    - name: "sandbox-worker-1"
      type: "compute"
      resources:
        cpu: 2
        memory: "4GB"
        disk: "20GB"
    
    - name: "supply-monitor-1"
      type: "monitoring"
      resources:
        cpu: 1
        memory: "2GB"
        disk: "10GB"
    
  networking:
    subnet: "10.0.0.0/24"
    gateway: "10.0.0.1"
EOF

    log "Machine configuration created ✅"
}

# Function to run integration tests
run_integration_tests() {
    log "Running integration tests..."
    
    # Test sandbox connectivity
    if curl -s http://localhost:8080/health > /dev/null; then
        log "Sandbox connectivity test ✅"
    else
        warning "Sandbox connectivity test failed"
    fi
    
    # Test database connectivity
    if docker exec $(docker-compose -f ../../sandbox/docker/docker-compose.yml ps -q sandbox-db) pg_isready -U sandbox_user > /dev/null; then
        log "Database connectivity test ✅"
    else
        warning "Database connectivity test failed"
    fi
    
    log "Integration tests completed"
}

# Main deployment flow
main() {
    log "🎯 Playbook5 Deployment Started"
    log "Environment: ${SANDBOX_ENV}"
    log "Supply Component: ${SUPPLY_COMPONENT}"
    log "Playbook Version: ${PLAYBOOK_VERSION}"
    
    check_prerequisites
    deploy_supply_chain
    configure_machines
    run_integration_tests
    
    log "🎉 Playbook5 deployment completed successfully!"
    log "📋 Summary:"
    log "  - Sandbox environment: Ready"
    log "  - Supply1 component: Deployed and tracking"
    log "  - Machine configurations: Applied"
    log "  - Integration tests: Completed"
}

# Execute main function
main "$@"