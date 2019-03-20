import sys
import requests
import requests_aws4auth as aws4auth
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom

access_id = 'AKIAILMYBJXAWAGCEDAQ'
access_key = 'jyC7ZtaZFq++ZjRPJzxxjPA7ohvDOwKFJOJkK+3v'
region = 'eu-west-2'

endpoint = 's3.{}.amazonaws.com'.format(region)
auth = aws4auth.AWS4Auth(access_id, access_key, region, 's3')

def xml_pprint(xml_string):
	print(minidom.parseString(xml_string).toprettyxml())

def download_file(bucket, s3_name):
	url = 'http://{}/{}/{}'.format(endpoint, bucket, s3_name)
	print('download file '+url)
	response = requests.get(url, auth=auth)
	print(response)
	if response.ok:
		open(s3_name, 'wb').write(response.content)
		print('Downloaded {} OK'.format(s3_name))
	else:
		xml_pprint(response.text)

def upload_file(bucket, local_path):
	data = open(local_path, 'rb').read()
	url = 'http://{}/{}/{}'.format(endpoint, bucket, local_path)
	print('upload file '+url)
	response = requests.put(url, data=data, auth=auth)
	if response.ok:
		print('Uploaded {} OK'.format(local_path))
	else:
		xml_pprint(response.text)

if __name__ == '__main__':
	upload_file(sys.argv[1], sys.argv[2])
	download_file(sys.argv[1], sys.argv[2])
