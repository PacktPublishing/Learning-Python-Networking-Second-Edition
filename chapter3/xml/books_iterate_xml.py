from xml.etree.cElementTree import iterparse

def books(file):
	for event, elem in iterparse(file):
		if event == 'start' and elem.tag == 'root':
			books = elem
		if event == 'end' and elem.tag == 'book':
			print ("%s,%s,%s,%s,%s" % (
			elem.findtext('title'),
			elem.findtext('publisher'),
			elem.findtext('numberOfChapters'),
			elem.findtext('pageCount'),
			elem.findtext('author')))
		if event == 'end' and elem.tag == 'chapter':
			print ("%s,%s,%s" % (
			elem.findtext('chapterNumber'),
			elem.findtext('chapterTitle'),
			elem.findtext('pageCount')))

if __name__ == '__main__':
    books(open("books.xml"))