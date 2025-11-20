import json
import time

def lambda_handler(event, context):
    # Simulate a service outage by raising an error
    raise Exception("Simulated payment service failure")

    # This part will never run while the exception is here
    response_body = {
        "service": "payment-service",
        "status": "ok",
        "message": "payment service reachable",
        "timestamp": int(time.time())
    }

    return {
        "statusCode": 200,
        "body": json.dumps(response_body)