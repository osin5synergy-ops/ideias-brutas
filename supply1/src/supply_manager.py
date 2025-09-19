#!/usr/bin/env python3
"""
Supply1 - Supply Chain Manager
2w3-0-sandbox-supply1-playbook5-machines
"""

import yaml
import logging
from datetime import datetime
from typing import Dict, List, Optional

class SupplyManager:
    """Supply Chain Component #1 - Resource Management"""
    
    def __init__(self, config_path: str = "config/supply1.yml"):
        """Initialize the supply manager with configuration"""
        self.config = self._load_config(config_path)
        self.logger = self._setup_logging()
        self.resources = {}
        self.tracking_active = False
        
    def _load_config(self, config_path: str) -> Dict:
        """Load configuration from YAML file"""
        try:
            with open(config_path, 'r') as file:
                return yaml.safe_load(file)
        except Exception as e:
            print(f"Error loading config: {e}")
            return {}
    
    def _setup_logging(self) -> logging.Logger:
        """Setup logging configuration"""
        logger = logging.getLogger('supply1')
        logger.setLevel(logging.INFO)
        
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        
        return logger
    
    def initialize_resources(self) -> bool:
        """Initialize resource tracking - 10% Humano A FAISCA"""
        try:
            humano_percentage = self.config.get('configuration', {}).get('resources', {}).get('humano_percentage', 10)
            faisca_enabled = self.config.get('configuration', {}).get('resources', {}).get('faisca_enabled', True)
            
            self.resources = {
                'humano': {
                    'percentage': humano_percentage,
                    'allocated': 0,
                    'available': 100,
                    'last_update': datetime.now()
                },
                'faisca': {
                    'enabled': faisca_enabled,
                    'intensity': 100 if faisca_enabled else 0,
                    'last_spark': datetime.now() if faisca_enabled else None
                }
            }
            
            self.logger.info(f"Resources initialized: {humano_percentage}% Humano, FAISCA {'enabled' if faisca_enabled else 'disabled'}")
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to initialize resources: {e}")
            return False
    
    def allocate_supply(self, amount: int, resource_type: str = 'humano') -> bool:
        """Allocate supply resources"""
        if resource_type not in self.resources:
            self.logger.error(f"Unknown resource type: {resource_type}")
            return False
            
        resource = self.resources[resource_type]
        if resource['available'] >= amount:
            resource['allocated'] += amount
            resource['available'] -= amount
            resource['last_update'] = datetime.now()
            
            self.logger.info(f"Allocated {amount} units of {resource_type}")
            return True
        else:
            self.logger.warning(f"Insufficient {resource_type} resources: requested {amount}, available {resource['available']}")
            return False
    
    def get_status(self) -> Dict:
        """Get current supply status"""
        return {
            'timestamp': datetime.now().isoformat(),
            'environment': self.config.get('configuration', {}).get('environment', 'unknown'),
            'resources': self.resources,
            'tracking_active': self.tracking_active
        }
    
    def start_tracking(self) -> bool:
        """Start real-time supply tracking"""
        try:
            self.tracking_active = True
            self.logger.info("Supply tracking started")
            return True
        except Exception as e:
            self.logger.error(f"Failed to start tracking: {e}")
            return False
    
    def stop_tracking(self) -> bool:
        """Stop supply tracking"""
        try:
            self.tracking_active = False
            self.logger.info("Supply tracking stopped")
            return True
        except Exception as e:
            self.logger.error(f"Failed to stop tracking: {e}")
            return False

if __name__ == "__main__":
    # Initialize and test the supply manager
    manager = SupplyManager()
    
    if manager.initialize_resources():
        print("✅ Supply1 initialized successfully")
        print(f"📊 Current status: {manager.get_status()}")
        
        # Test allocation
        if manager.allocate_supply(5, 'humano'):
            print("✅ Resource allocation successful")
        
        print(f"📊 Updated status: {manager.get_status()}")
    else:
        print("❌ Failed to initialize Supply1")