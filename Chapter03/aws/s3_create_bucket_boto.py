import boto3
import sys

# Create an S3 client
s3 = boto3.client('s3')

def create_bucket(bucket):
	s3.create_bucket(Bucket=bucket,
	CreateBucketConfiguration={'LocationConstraint': 'eu-west-2'})
	
if __name__ == '__main__':
	create_bucket(sys.argv[1])