import json

def handler(event, context):
    body = { "message": "go serverless v1.0! your function executed successfully!", "input": event }
    response = { "statusCode": 200, "body": json.dumps(body) }
    return response
