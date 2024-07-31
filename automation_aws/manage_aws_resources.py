# Use boto3 to create resources on AWS

import boto3
client = boto3.client('s3')

response = client.create_bucket(
    Bucket='gouri-demo-s3-practice'
)