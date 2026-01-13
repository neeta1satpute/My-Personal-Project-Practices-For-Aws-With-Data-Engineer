def lambda_handler(event, context):
    print("CI/CD first deployment working 🚀")
    return {
        "statusCode": 200,
        "body": "Hello from Lambda CI/CD"
    }
