# Googlecrawler:
Python 2.7 script that crawls google using Scrapy and stores the results in MongoDB.

Tested on Ubuntu 15.04

## Function
- Crawls google for user-inputted search terms
- Saves the first 20 results returned to mongodb database
- Visits each of the result pages and stores info related to search terms
- Displays results to console

## Installation
- pip install Scrapy
- pip install pymongo
- need to have mongodb installed
	- apt-get install mongodb-server

## Getting started
```
python googlecrawler.py csv

```
```
python googlecrawler.py python vs lua
```