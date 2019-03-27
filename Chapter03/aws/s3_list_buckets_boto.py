import boto3

# Create an S3 client
s3 = boto3.client('s3')

def list_buckets():

	# Call S3 to list current buckets
	response = s3.list_buckets()

	# Get a list of all bucket names from the response
	buckets = [bucket['Name'] for bucket in response['Buckets']]

	# Print out the bucket list
	print("Bucket List: %s" % buckets)
	
if __name__ == '__main__':
	list_buckets()