import json
from lamdba_function import lambda_handler

# Sample event for testing (replace with your own S3 event data)
event = {
    "Records": [
        {
            "s3": {
                "bucket": {
                    "name": "your-bucket-name"
                },
                "object": {
                    "key": "your-file-key"
                }
            }
        }
    ]
}

# Simulate the Lambda context (if needed, this can be extended)
class Context:
    def __init__(self):
        self.function_name = "test_lambda"
        self.memory_limit_in_mb = 128
        self.invoked_function_arn = "arn:aws:lambda:us-west-2:123456789012:function:test_lambda"
        self.aws_request_id = "test1234"

context = Context()

# Call the Lambda function
result = lambda_handler(event, context)
print(json.dumps(result, indent=2))
