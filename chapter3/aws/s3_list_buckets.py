import sys
import requests
import requests_aws4auth as aws4auth
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom

access_id = ''
access_key = ''
region = 'eu-west-2'

endpoint = 's3.{}.amazonaws.com'.format(region)
auth = aws4auth.AWS4Auth(access_id, access_key, region, 's3')

ns = 'http://s3.amazonaws.com/doc/2006-03-01/'

def xml_pprint(xml_string):
	print(minidom.parseString(xml_string).toprettyxml())

def handle_error(response):
	output = 'Status code: {}\n'.format(response.status_code)
	root = ET.fromstring(response.text)
	code = root.find('Code').text
	output += 'Error code: {}\n'.format(code)
	message = root.find('Message').text
	output += 'Message: {}\n'.format(message)
	print(output)

def list_buckets():
	print(endpoint)
	response = requests.get("http://"+endpoint, auth=auth)
	print(response.text)
	xml_pprint(response.text)
	if response.ok:
		root = ET.fromstring(response.text)
		for element in root:
			print('Tag: ' + element.tag)
	else:
		handle_error(response)
	
if __name__ == '__main__':
	list_buckets()