import boto3   # AWS services access karayla boto3 library use karto
import os      # environment variables access karayla

# S3 client create karto (AWS S3 operations sathi)
s3 = boto3.client('s3')


def lambda_handler(event, context):

    # -------------------------------
    # 1️⃣ Event madhun data gheto
    # -------------------------------
    # EventBridge / S3 event madhun source bucket & file name miltat

    source_bucket = event['detail']['bucket']['name']  # source bucket name
    object_key = event['detail']['object']['key']      # file name (key)

    # -------------------------------
    # 2️⃣ Destination bucket gheto
    # -------------------------------
    # CloudFormation / env variable madhun destination bucket

    destination_bucket = os.environ['DEST_BUCKET']

    # -------------------------------
    # 3️⃣ Copy source info prepare karto
    # -------------------------------
    copy_source = {
        'Bucket': source_bucket,
        'Key': object_key
    }

    try:

        # -------------------------------
        # 4️⃣ FILE COPY (Source → Destination)
        # -------------------------------
        s3.copy_object(
            CopySource=copy_source,     # kuthiun copy karaycha
            Bucket=destination_bucket,  # kuthe paste karaycha
            Key=object_key             # same file name thevto
        )

        # -------------------------------
        # 5️⃣ SOURCE FILE DELETE (MOVE behavior)
        # -------------------------------
        s3.delete_object(
            Bucket=source_bucket,
            Key=object_key
        )

        # -------------------------------
        # 6️⃣ SUCCESS MESSAGE
        # -------------------------------
        print(f"File moved successfully: {object_key}")

        return {
            'statusCode': 200,
            'body': f"Moved {object_key} from {source_bucket} to {destination_bucket}"
        }

    except Exception as e:

        # -------------------------------
        # 7️⃣ ERROR HANDLING
        # -------------------------------
        print("Error occurred:", str(e))

        return {
            'statusCode': 500,
            'body': str(e)
        }