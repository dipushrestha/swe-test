#!/usr/bin/env python3
from calculator import AdvancedCalculator

def test_operations():
    print("Testing calculator operations...")
    
    calc = AdvancedCalculator()
    
    results = []
    results.append(calc.add(10, 5))
    results.append(calc.add(20, 3)) 
    results.append(calc.add(7, 2))   # 3rd operation triggers webhook
    results.append(calc.add(15, 4))
    
    assert results[0] == 15
    print("✓ Addition tests passed")
    
    # Test subtraction
    sub_result = calc.subtract(10, 3)
    assert sub_result == 7
    print("✓ Subtraction test passed")
    
    # Test operations log
    operations = calc.get_operations()
    assert len(operations) >= 4
    print("✓ Operations logging test passed")
    
    return True

def test_configuration():
    from config_manager import ConfigManager
    
    config = ConfigManager()
    is_valid = config.validate_config()
    
    assert is_valid == True
    print("✓ Configuration validation test passed")
    return True

if __name__ == "__main__":
    print("Running advanced calculator tests...")
    
    test_operations()
    test_configuration()
    
    print("All tests passed! 🎉")
