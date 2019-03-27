# -*- coding: utf-8 -*-

# Scrapy settings for europython project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'europython'

SPIDER_MODULES = ['europython.spiders']
NEWSPIDER_MODULE = 'europython.spiders'


# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'europython.pipelines.EuropythonPipeline': 100,
    'europython.pipelines.EuropythonXmlExport': 200,
    'europython.pipelines.EuropythonSQLitePipeline': 300,
}

DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
    #'europython.middlewares.ProxyMiddleware': 100,
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'europython (+http://www.yourdomain.com)'
