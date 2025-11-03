#!/usr/bin/env python3
"""
Test file with webhook logging
"""
from webhook_logger import log_to_webhook
from calculator import Calculator

def test_addition():
    """Test addition with webhook logging"""
    log_to_webhook("test_started", {"test_name": "test_addition"})
    
    calc = Calculator()
    result = calc.add(5, 3)
    
    assert result == 8
    print("✓ Addition test passed")
    
    log_to_webhook("test_passed", {
        "test_name": "test_addition", 
        "result": result
    })
    return True

def test_operations_log():
    """Test operations logging"""
    log_to_webhook("test_started", {"test_name": "test_operations_log"})
    
    calc = Calculator()
    calc.add(2, 2)
    calc.add(3, 4)
    
    operations = calc.get_operations()
    assert len(operations) == 2
    print("✓ Operations log test passed")
    
    log_to_webhook("test_passed", {
        "test_name": "test_operations_log",
        "operations_count": len(operations)
    })
    return True

if __name__ == "__main__":
    print("Running calculator tests...")
    
    # Log test suite start
    log_to_webhook("test_suite_started", {
        "total_tests": 2,
        "python_file": __file__
    })
    
    # Run tests
    test_addition()
    test_operations_log()
    
    print("All tests passed! ✅")
    
    # Log completion
    log_to_webhook("test_suite_completed", {
        "status": "success",
        "tests_run": 2
    })
