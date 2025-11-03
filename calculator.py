from webhook_logger import log_to_webhook

class Calculator:
    def __init__(self):
        self.operations = []
        log_to_webhook("calculator_initialized", {
            "location": "calculator.py",
            "operation": "init"
        })
    
    def add(self, a, b):
        result = a + b
        self.operations.append(f"add({a}, {b}) = {result}")
        
        # Log this operation to webhook
        log_to_webhook("addition_operation", {
            "numbers": [a, b],
            "result": result,
            "total_operations": len(self.operations)
        })
        
        return result
    
    def get_operations(self):
        return self.operations
