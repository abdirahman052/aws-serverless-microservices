import json
import time

def lambda_handler(event, context):
    # Log that this service was hit (shows up in CloudWatch)
    print("auth-service hit", {"event": event})

    # Later we can add real auth logic or break this on purpose
    response_body = {
        "service": "auth-service",
        "status": "ok",
        "message": "auth service reachable",
        "timestamp": int(time.time())
    }

    return {
        "statusCode": 200,
        "body": json.dumps(response_body)
    }
