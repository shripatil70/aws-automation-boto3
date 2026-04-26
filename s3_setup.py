import boto3
from botocore.exceptions import ClientError
from config import BUCKET_NAME, REGION

s3 = boto3.client('s3')

def create_bucket():
    try:
        s3.create_bucket(
            Bucket=BUCKET_NAME,
            CreateBucketConfiguration={'LocationConstraint': REGION}
        )
        print("Bucket created:", BUCKET_NAME)

    except ClientError as e:
        error_code = e.response['Error']['Code']

        if error_code == 'BucketAlreadyOwnedByYou':
            print("Bucket already exists and is owned by you:", BUCKET_NAME)

        elif error_code == 'BucketAlreadyExists':
            print("Bucket name taken globally. Choose another.")

        else:
            raise e