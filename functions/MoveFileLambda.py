import boto3
import os

s3 = boto3.client('s3')

def lambda_handler(event, context):

    source_bucket = os.environ['SOURCE_BUCKET']
    dest_bucket = os.environ['DEST_BUCKET']

    # Event from S3
    for record in event['Records']:
        key = record['s3']['object']['key']

        copy_source = {'Bucket': source_bucket, 'Key': key}

        # Copy file
        s3.copy_object(
            Bucket=dest_bucket,
            Key=key,
            CopySource=copy_source
        )

        print(f"Moved file: {key}")

    return "Success"