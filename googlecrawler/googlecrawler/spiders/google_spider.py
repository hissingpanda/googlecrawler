# Google Spider to scrape information from google.com

import scrapy
import re

from urlparse import urlparse, parse_qs, urljoin
from googlecrawler.items import GoogleCrawlerItem

class GoogleSpider(scrapy.Spider):
    name = "google"
    def __init__(self, query):
        self.query = query
        self.start_urls = [
            # pass in query to google search, attach page per limit to be 20
            "https://www.google.com/search?q=%s&num=20" % query
        ]
    # get results and parse them into title, link properties
    def parse(self, response):
        for sel in response.xpath('//h3'):
            item = GoogleCrawlerItem()
            item['title'] = parse_html(sel.xpath('a/node()').extract())
            item['link'] = parse_url(sel.xpath('a/@href').extract()[0])
            urls = item['link'] 
            # follow each link to get the page's text
            for url in urls:
                request = scrapy.Request(url, callback=self.parse_dir_contents)
                # pass item into next request call
                request.meta['item'] = item
                yield request

    # scan text inside the link to see if it contains query
    def parse_dir_contents(self, response):
        item = response.meta['item']
        keywords = []
        item['desc'] = ''
        # split query into separate keywords and search text for each keyword
        keywords = re.split(r'\+', self.query)
        for keyword in keywords:
            text = parse_html(response.xpath("//p[contains(/following-sibling::text()[1], %s)]" % keyword).extract_first())
            if not item['desc']:
                item['desc'] = text
            else: 
                # avoid concatenating duplicate responses
                if item['desc'] != text:
                    item['desc'] = item['desc'] + text
        yield item

# strips html tags
def parse_html(html):
    parser = re.compile(r'<.*?>')
    text = ''
    if html:
        for line in html:
            text = text + line
        # remove extra white space
        text = ' '.join(text.split())
    return parser.sub('', text)

# strips url of extra characters from google results
def parse_url(url):
    query = parse_qs(urlparse(url).query)
    return query.get('q')