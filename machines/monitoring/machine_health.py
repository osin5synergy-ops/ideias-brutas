#!/usr/bin/env python3
"""
Machine Health Monitor
2w3-0-sandbox-supply1-playbook5-machines
"""

import time
import json
import logging
from datetime import datetime
from typing import Dict, List

class MachineHealthMonitor:
    """Monitor health and performance of machines in the infrastructure"""
    
    def __init__(self):
        self.logger = self._setup_logging()
        self.machines = self._load_machine_config()
        self.health_status = {}
        
    def _setup_logging(self) -> logging.Logger:
        """Setup logging configuration"""
        logger = logging.getLogger('machine_health')
        logger.setLevel(logging.INFO)
        
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        
        return logger
    
    def _load_machine_config(self) -> Dict:
        """Load machine configuration"""
        # Simplified configuration for demo
        return {
            'compute_nodes': [
                {
                    'name': 'sandbox-compute-01',
                    'type': 'compute',
                    'endpoint': 'http://sandbox-compute-01:8080',
                    'resources': {'humano_allocation': 10, 'faisca_enabled': True}
                }
            ],
            'monitoring_nodes': [
                {
                    'name': 'sandbox-monitor-01',
                    'type': 'monitoring',
                    'endpoint': 'http://sandbox-monitor-01:9090',
                    'services': ['prometheus', 'grafana']
                }
            ],
            'storage_nodes': [
                {
                    'name': 'sandbox-storage-01',
                    'type': 'storage',
                    'endpoint': 'postgresql://sandbox-storage-01:5432',
                    'capacity': '100GB'
                }
            ]
        }
    
    def check_machine_health(self, machine: Dict) -> Dict:
        """Check health of a specific machine"""
        machine_name = machine['name']
        machine_type = machine['type']
        
        health_data = {
            'name': machine_name,
            'type': machine_type,
            'timestamp': datetime.now().isoformat(),
            'status': 'unknown',
            'response_time': None,
            'details': {}
        }
        
        try:
            if machine_type == 'compute':
                health_data.update(self._check_compute_node(machine))
            elif machine_type == 'monitoring':
                health_data.update(self._check_monitoring_node(machine))
            elif machine_type == 'storage':
                health_data.update(self._check_storage_node(machine))
                
        except Exception as e:
            self.logger.error(f"Health check failed for {machine_name}: {e}")
            health_data['status'] = 'error'
            health_data['details']['error'] = str(e)
        
        return health_data
    
    def _check_compute_node(self, machine: Dict) -> Dict:
        """Check compute node specific health"""
        details = {}
        
        # Check if resources are properly allocated
        resources = machine.get('resources', {})
        humano_allocation = resources.get('humano_allocation', 0)
        faisca_enabled = resources.get('faisca_enabled', False)
        
        details['humano_allocation'] = f"{humano_allocation}%"
        details['faisca_status'] = 'enabled' if faisca_enabled else 'disabled'
        
        # Simulate health check
        status = 'healthy' if humano_allocation == 10 and faisca_enabled else 'warning'
        
        return {
            'status': status,
            'response_time': 50,  # ms
            'details': details
        }
    
    def _check_monitoring_node(self, machine: Dict) -> Dict:
        """Check monitoring node specific health"""
        details = {}
        
        services = machine.get('services', [])
        details['active_services'] = len(services)
        details['services'] = services
        
        return {
            'status': 'healthy',
            'response_time': 25,  # ms
            'details': details
        }
    
    def _check_storage_node(self, machine: Dict) -> Dict:
        """Check storage node specific health"""
        details = {}
        
        capacity = machine.get('capacity', 'unknown')
        details['total_capacity'] = capacity
        details['utilization'] = '15%'  # Simulated
        
        return {
            'status': 'healthy',
            'response_time': 30,  # ms
            'details': details
        }
    
    def monitor_all_machines(self) -> Dict:
        """Monitor health of all machines"""
        self.logger.info("Starting comprehensive machine health check...")
        
        all_status = {
            'timestamp': datetime.now().isoformat(),
            'environment': '2w3-0-sandbox',
            'supply_integration': 'supply1',
            'playbook_version': '5',
            'machines': []
        }
        
        # Check each machine type
        for machine_type, machines_list in self.machines.items():
            self.logger.info(f"Checking {machine_type}...")
            
            for machine in machines_list:
                health_data = self.check_machine_health(machine)
                all_status['machines'].append(health_data)
                
                status_emoji = "✅" if health_data['status'] == 'healthy' else "⚠️" if health_data['status'] == 'warning' else "❌"
                self.logger.info(f"{status_emoji} {machine['name']}: {health_data['status']}")
        
        # Calculate overall health
        healthy_count = sum(1 for m in all_status['machines'] if m['status'] == 'healthy')
        total_count = len(all_status['machines'])
        
        all_status['summary'] = {
            'total_machines': total_count,
            'healthy_machines': healthy_count,
            'overall_health': f"{(healthy_count/total_count)*100:.1f}%" if total_count > 0 else "0%"
        }
        
        self.logger.info(f"Health check completed: {healthy_count}/{total_count} machines healthy")
        return all_status

if __name__ == "__main__":
    monitor = MachineHealthMonitor()
    
    print("🔍 Starting Machine Health Monitor...")
    print("Environment: 2w3-0-sandbox-supply1-playbook5-machines")
    print()
    
    # Generate and display health data
    health_data = monitor.monitor_all_machines()
    
    print("📊 Machine Health Summary:")
    print(f"  Total Machines: {health_data['summary']['total_machines']}")
    print(f"  Healthy Machines: {health_data['summary']['healthy_machines']}")
    print(f"  Overall Health: {health_data['summary']['overall_health']}")
    
    print("\n🔍 Individual Machine Status:")
    for machine in health_data['machines']:
        status_icon = "✅" if machine['status'] == 'healthy' else "⚠️" if machine['status'] == 'warning' else "❌"
        print(f"  {status_icon} {machine['name']} ({machine['type']}): {machine['status']}")
    
    # Export health data
    with open('/tmp/machine_health_report.json', 'w') as f:
        json.dump(health_data, f, indent=2)
    
    print(f"\n📄 Health report exported to: /tmp/machine_health_report.json")