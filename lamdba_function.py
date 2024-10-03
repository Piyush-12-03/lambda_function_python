import json
import boto3
import logging

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.info(f"Received event: {json.dumps(event)}")  # Log the entire event

    # Initialize S3 client
    s3_client = boto3.client('s3')

    try:
        # Check if 'Records' key is present
        if 'Records' not in event:
            logger.error("No 'Records' found in event.")
            return {
                'statusCode': 400,
                'body': json.dumps("No 'Records' found in event.")
            }

        # Extract bucket name and object key from the event
        bucket_name = event['Records'][0]['s3']['bucket']['name']
        object_key = event['Records'][0]['s3']['object']['key']

        # Get the object size using S3 client
        response = s3_client.head_object(Bucket=bucket_name, Key=object_key)
        file_size = response['ContentLength']

        # Log the file name and size
        logger.info(f"File uploaded: {object_key}, Size: {file_size} bytes")

        # Prepare the response
        return {
            'statusCode': 200,
            'body': json.dumps({
                'file_name': object_key,
                'file_size': file_size
            })
        }
    
    except Exception as e:
        logger.error(f"Error processing the event: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error processing the event: {str(e)}")
        }
