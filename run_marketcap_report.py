"""
Copyright 2017 Iofacture Digital Solutions (IDS)

This file is subject to the terms and conditions defined in
file 'LICENSE.txt', which is part of this source code package.

Author: Matthew Ishii
Created: 01-02-2018

Notes:

"""

from scrapy.crawler import CrawlerProcess
from datascraper.spiders.spiders import MarketCapSpider

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
    'LOG_ENABLED': False
})

process.crawl(MarketCapSpider)

# the script will block here until the crawling is finished
process.start()
