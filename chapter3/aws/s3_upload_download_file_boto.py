import sys
import boto3
import botocore

# Create an S3 client
s3 = boto3.client('s3')

# Create an S3 bucket
s3_bucket = boto3.resource('s3')

def download_file(bucket, s3_name):
	try:
		s3_bucket.Bucket(bucket).download_file('Python.png', 'Python_download.png')
	except botocore.exceptions.ClientError as e:
		if e.response['Error']['Code'] == "404":
			print("The object does not exist.")
		else:
			raise

def upload_file(bucket_name, filename):
	# Uploads the given file using a managed uploader, which will split up large
	# files automatically and upload parts in parallel.
	s3.upload_file(filename, bucket_name, filename)

if __name__ == '__main__':
	upload_file(sys.argv[1], sys.argv[2])
	download_file(sys.argv[1], sys.argv[2])
