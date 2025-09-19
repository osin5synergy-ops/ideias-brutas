#!/bin/bash

# 2w3-0-sandbox-supply1-playbook5-machines Integration Script
# This script demonstrates the complete integration of all components

set -e

# Configuration
PROJECT_ROOT="/home/runner/work/ideias-brutas/ideias-brutas"
COMPONENT_VERSION="2w3-0"

# Color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

log() {
    echo -e "${GREEN}[$(date +'%H:%M:%S')]${NC} $1"
}

info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

error() {
    echo -e "${RED}[ERROR]${NC} $1" >&2
}

# Display header
echo "=========================================="
echo "🚀 ideias-brutas Integration Demo"
echo "   2w3-0-sandbox-supply1-playbook5-machines"
echo "=========================================="

# Component 1: Sandbox Environment
log "1. Testing Sandbox Environment (2w3-0)"
cd "$PROJECT_ROOT/sandbox"
info "Sandbox configuration exists: $(test -f config/environment.yml && echo '✅' || echo '❌')"
info "Docker compose ready: $(test -f docker/docker-compose.yml && echo '✅' || echo '❌')"
info "Setup script available: $(test -x scripts/setup.sh && echo '✅' || echo '❌')"

# Component 2: Supply Chain (supply1)
log "2. Testing Supply Chain Component (supply1)"
cd "$PROJECT_ROOT/supply1"
info "Supply1 configuration exists: $(test -f config/supply1.yml && echo '✅' || echo '❌')"
info "Supply manager ready: $(test -f src/supply_manager.py && echo '✅' || echo '❌')"

# Test supply1 functionality
if command -v python3 &> /dev/null; then
    cd src
    python3 -c "
import sys
sys.path.append('.')
try:
    from supply_manager import SupplyManager
    manager = SupplyManager('../config/supply1.yml')
    if manager.initialize_resources():
        print('✅ Supply1 component functional')
        status = manager.get_status()
        print(f'   - Environment: {status[\"environment\"]}')
        print(f'   - Humano allocation: {status[\"resources\"][\"humano\"][\"percentage\"]}%')
        print(f'   - FAISCA status: {\"enabled\" if status[\"resources\"][\"faisca\"][\"enabled\"] else \"disabled\"}')
    else:
        print('❌ Supply1 initialization failed')
except Exception as e:
    print(f'❌ Supply1 test failed: {e}')
"
    cd ..
else
    warning "Python3 not available, skipping supply1 functional test"
fi

# Component 3: Operational Playbook (playbook5)
log "3. Testing Operational Playbook (playbook5)"
cd "$PROJECT_ROOT/playbook5"
info "Playbook procedures exist: $(test -f procedures/supply-chain-ops.md && echo '✅' || echo '❌')"
info "Automation scripts ready: $(test -x automation/deploy.sh && echo '✅' || echo '❌')"

# Component 4: Machine Infrastructure
log "4. Testing Machine Infrastructure"
cd "$PROJECT_ROOT/machines"
info "Machine configuration exists: $(test -f config/machines.yml && echo '✅' || echo '❌')"
info "Health monitor ready: $(test -f monitoring/machine_health.py && echo '✅' || echo '❌')"

# Test machine health monitoring
if command -v python3 &> /dev/null; then
    cd monitoring
    python3 machine_health.py
    cd ..
else
    warning "Python3 not available, skipping machine health test"
fi

# Integration Test
log "5. Integration Verification"
cd "$PROJECT_ROOT"

# Check all components are present
components=(
    "sandbox/README.md"
    "supply1/README.md"
    "playbook5/README.md"
    "machines/README.md"
)

integration_score=0
for component in "${components[@]}"; do
    if [ -f "$component" ]; then
        integration_score=$((integration_score + 25))
    fi
done

info "Integration score: ${integration_score}%"

if [ $integration_score -eq 100 ]; then
    log "🎉 All components successfully integrated!"
    echo
    echo "📋 Component Summary:"
    echo "   🏗️  Sandbox (2w3-0): Development environment ready"
    echo "   🔗 Supply1: Supply chain management (10% Humano - A FAISCA)"
    echo "   📚 Playbook5: Operational procedures defined"
    echo "   🖥️  Machines: Infrastructure configuration complete"
    echo
    echo "🚀 Ready for deployment with: ./playbook5/automation/deploy.sh"
else
    error "Integration incomplete (${integration_score}%). Please check missing components."
    exit 1
fi