import sys
import requests
import requests_aws4auth as aws4auth
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom

access_id = 'AKIAISURAZJ3FQ3JUBEQ'
access_key = 'zGk2yZxPuozRBWh1IfqVoJNCLmL2iGXECifV/1XT'
region = 'eu-west-2'

endpoint = 's3.{}.amazonaws.com'.format(region)
auth = aws4auth.AWS4Auth(access_id, access_key, region, 's3')

ns = 'http://s3.amazonaws.com/doc/2006-03-01/'

def xml_pprint(xml_string):
	print(minidom.parseString(xml_string).toprettyxml())

def create_bucket(bucket):
	print(bucket)
	XML = ET.Element('CreateBucketConfiguration')
	XML.attrib['xmlns'] = ns
	location = ET.SubElement(XML, 'LocationConstraint')
	location.text = auth.region
	data = ET.tostring(XML, encoding='utf-8')
	url = 'http://{}.{}'.format(bucket,endpoint)
	xml_pprint(data)
	response = requests.put(url, data=data, auth=auth)
	print(response)
	if response.ok:
		print('Created bucket {} OK'.format(bucket))
	else:
		xml_pprint(response.text)

if __name__ == '__main__':
	create_bucket(sys.argv[1])