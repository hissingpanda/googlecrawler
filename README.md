# googlecrawler
Python 2.7 script that crawls Google using Scrapy and stores the results in MongoDB.

Tested on Ubuntu 15.04

## Function
- Crawls google.com for user-inputted search terms
- Saves the first 20 results returned to MongoDB database
- Visits each of the result pages and stores info related to search terms
- Displays results to console

## Installation
googlecrawler requires Scrapy and pymongo in order to run:
```
pip install Scrapy
pip install pymongo
```
You also need to have MongoDB installed. It can be installed on Ubuntu by running:
```
apt-get install mongodb-server
```

## Getting started
googlecrawler is run by passing keywords into the script via command-line. To perform a search with a single keyword such as "csv", you can do the following:
```
python googlecrawler.py csv
```
Multiple keywords are also accepted; to do this pass each keyword in as an individual argument. For instance, this is how to perform the search "python vs lua":
```
python googlecrawler.py python vs lua
```
