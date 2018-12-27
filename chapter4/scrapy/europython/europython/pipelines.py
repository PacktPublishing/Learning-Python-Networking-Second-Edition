# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
from scrapy import signals
from scrapy.exporters import CsvItemExporter
from scrapy.exporters import XmlItemExporter
from pony.orm import *
import codecs
import json
import csv

db = Database("sqlite", "europython.sqlite", create_db=True)

class EuropythonSession(db.Entity):
	"""Pony ORM model of the europython session table"""
	id = PrimaryKey(int, auto=True)
	author = Required(str)
	title = Required(str)
	description = Required(str)
	date = Required(str)
	tags = Required(str)
	
class EuropythonPipeline(object):	
	def __init__(self):
		self.file = codecs.open('europython_items.json', 'w+b', encoding='utf-8')

	def process_item(self, item, spider):
		line = json.dumps(dict(item), ensure_ascii=False) + "\n"
		self.file.write(line)
		return item

	def spider_closed(self, spider):
		self.file.close()

class EuropythonXmlExport(object):
	
	def __init__(self):
		self.files = {}

	@classmethod
	def from_crawler(cls, crawler):
		pipeline = cls()
		crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
		crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
		return pipeline

	def spider_opened(self, spider):
		file = open('europython_items.xml', 'w+b')
		self.files[spider] = file
		self.exporter = XmlItemExporter(file)
		self.exporter.start_exporting()

	def spider_closed(self, spider):
		self.exporter.finish_exporting()
		file = self.files.pop(spider)
		file.close()

	def process_item(self, item, spider):
		self.exporter.export_item(item)
		return item
		
		
class EuropythonSQLitePipeline(object):

	@classmethod
	def from_crawler(cls, crawler):
		pipeline = cls()
		crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
		crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
		return pipeline
		
	def spider_opened(self, spider):
		
		db.generate_mapping(check_tables=True, create_tables=True)

	def spider_closed(self, spider):
		db.commit()
		 
    # Insert data in database
	@db_session
	def process_item(self, item, spider):
                # use db_session as a context manager
                with db_session:
                        try:
                                strAuthor = str(item['author'])
                                strAuthor = strAuthor[3:len(strAuthor)-2]
			
                                strTitle = str(item['title'])
                                strTitle = strTitle[3:len(strTitle)-2]
			
                                strDescription = str(item['description'])
                                strDescription = strDescription[3:len(strDescription)-2]
			
                                strDate = str(item['date'])
                                strDate = strDate[3:len(strDate)-2]
                                strDate = strDate.replace("[u'", "").replace("']", "").replace("u'", "").replace("',", ",")
			
                                strTags = str(item['tags'])
                                strTags = strTags.replace("[u'", "").replace("']", "").replace("u'", "").replace("',", ",")

                                europython_session = EuropythonSession(author=strAuthor,title=strTitle,
                                                                       description=strDescription,date=strDate,tags=strTags)

			
                        except Exception as e:
                                print("Error processing the items in the DB %d: %s" % (e.args[0], e.args[1]))

                        return item
