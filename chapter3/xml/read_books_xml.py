
import xml.etree.ElementTree as ET

books = ET.parse("books.xml")
root = books.getroot()

print(root)

print(root.tag)

#Access to attributes
for child in root:
	print(child.tag, child.attrib)
	for element in child:
		print(element.tag, element.text)
	
#Access to attribute content
for child in root:
	print(child.tag, child.attrib['id'],child.attrib['name'])



    
