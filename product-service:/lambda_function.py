import json
import time

def lambda_handler(event, context):
    print("product-service hit", {"event": event})

    products = [
        {"id": 1, "name": "Cloud Hoodie", "price": 49.99},
        {"id": 2, "name": "DevOps Mug", "price": 14.99},
        {"id": 3, "name": "SRE Sticker Pack", "price": 9.99}
    ]

    return {
        "statusCode": 200,
        "body": json.dumps({
            "service": "product-service",
            "status": "ok",
            "products": products,
            "timestamp": int(time.time())
        })
    }