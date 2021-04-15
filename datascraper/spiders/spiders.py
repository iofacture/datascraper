"""
Copyright 2017 Iofacture Digital Solutions (IDS)

This file is subject to the terms and conditions defined in
file 'LICENSE.txt', which is part of this source code package.

Author: Matthew Ishii
Created: 01-01-2018

Notes:
    For this specific case we want to obtain the market capitalization for
    BTC/USD across the various crypto-currency exchanges. This script will
    allow us to see, at a glance, the current market conditions and where
    to focus our effort.

    Target web page: https://coinmarketcap.com/currencies/bitcoin/#marketso

"""

import scrapy
import datetime


class MarketCapSpider(scrapy.Spider):
    name = 'MCSpider'
    start_urls = ['https://coinmarketcap.com/currencies/bitcoin/#markets']

    def parse(self, response):
        trows = response.xpath('//table[@id="markets-table"]/tbody/tr')

        filename = 'reports\\btc_marketcap_report_%s.txt' % datetime.datetime.now().strftime("%d%m%Y")
        handle = open(filename, 'w')

        cmclist = []
        for row in trows:
            pair = row.xpath('td[3]/a[1]/text()').extract()[0].strip()

            if pair == 'BTC/USD':
                cmcrow = {'pair': pair,
                          'ranking': row.xpath('td[1]/text()').extract()[0].strip(),
                          'source': row.xpath('td[2]/a[1]/text()').extract()[0].strip(),
                          'volume': row.xpath('td[4]/span[1]/text()').extract()[0].strip(),
                          'price': row.xpath('td[5]/span[1]/text()').extract()[0].strip(),
                          'percent': row.xpath('td[6]/text()').extract()[0].strip()}
                cmclist.append(cmcrow)

        sorted(cmclist, key=lambda k: k['percent'], reverse=True)

        header = "%-17s %-17s %-17s %-17s %-17s %-17s\n" % ('Ranking', 'Source', 'Pair', 'Volume', 'Price', 'Percent')
        handle.write(header)
        separator = ((("-" * 17) + " ") * 6) + '\n'
        handle.write(separator)
        for r in cmclist:
            record = "%-17s %-17s %-17s %-17s %-17s %-17s\n" % (r['ranking'], r['source'],
                                                                r['pair'], r['volume'], r['price'], r['percent'])
            handle.write(record)

        handle.close()
