# wrapper script to run google crawler

import sys
import scrapy
import pymongo

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from pymongo import MongoClient

from googlecrawler.spiders.google_spider import GoogleSpider

# require input arguments
if len(sys.argv) < 2:
	raise ValueError('googlecrawler.py requires at least 1 input argument')

keywords = ''
# concatenate input args for google search
keywords = '+'.join(sys.argv[1:])

spider = GoogleSpider(scrapy.Spider)
process = CrawlerProcess(get_project_settings())

process.crawl(spider, query=keywords)
# runs spider; holds scripts until process finishes
process.start()

# connect to database, collection
client = pymongo.MongoClient('localhost', 27017)
db = client['crawlerdb']
collection = db['items']

# returns last 20 results entered into database to console
for data in collection.find().sort('_id', pymongo.DESCENDING).limit(20):
	print data
