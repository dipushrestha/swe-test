from config_manager import ConfigManager

class AdvancedCalculator:
    def __init__(self):
        self.config = ConfigManager()
        self.operations = []
    
    def add(self, a, b):
        result = a + b
        self.operations.append(f"add({a}, {b}) = {result}")
        
        if len(self.operations) % 3 == 0:  # Every 3 operations
            self.config.validate_config()
        
        return result
    
    def subtract(self, a, b):
        result = a - b
        self.operations.append(f"subtract({a}, {b}) = {result}")
        return result
    
    def get_operations(self):
        return self.operations
