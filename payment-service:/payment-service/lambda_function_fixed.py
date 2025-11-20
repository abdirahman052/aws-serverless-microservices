import json
import time

def lambda_handler(event, context):
    # Log that the service was hit (shows up in CloudWatch)
    print("payment-service hit", {"event": event})

    # Normal healthy response
    response_body = {
        "service": "payment-service",
        "status": "ok",
        "message": "payment service reachable",
        "timestamp": int(time.time())
    }

    return {
        "statusCode": 200,
        "body": json.dumps(response_body)
    }
