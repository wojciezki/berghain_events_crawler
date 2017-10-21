import re
import urllib.parse
import scrapy
from scrapy.spiders import CrawlSpider
from scrapy.linkextractors import LinkExtractor
from bh_artists.items import BhArtistsItem


class ArtistSpider(CrawlSpider):
    name = 'artists'
    allowed_domains = ['www.berghain.de']
    start_urls = ['http://berghain.de/events']

    def parse(self, response):
        import pdb
        pdb.set_trace()
        # create array of auctions links
        event_page = response.xpath('//*[@class="type_stage"]/span/a/@href').extract()
        events = []
        for page in event_page:
            events.append(response.urljoin(page))

        for event in events:
            import pdb
            pdb.set_trace()
            # define item
            item = BhArtistsItem()
            item['event_link'] = event
            item['lineup'] = {}

            # pass each page to the parse_event() method
            request = scrapy.Request(event, callback=self.parse_event)
            request.meta['item'] = item

            # add item to array of items
            yield request

        for div in response.xpath('//div[@class="expandlist"]//a/@href'):
            yield response.follow(div, callback=self.parse)

    def parse_event(self, response):

        item = response.meta['item']

        item['event_date'] = response.xpath('//div[@class="headline"]/h2/text()').extract_first()
        item['event_name'] = response.xpath('//div[@class="headline"]/h2/span[1]/text()').extract_first()

        items = response.xpath('//*[@class="col_context"]')

        for row in items:
            dd = [row.xpath('//*[@class="col_context"]/ul/li/span[2]/text()')]
            item['lineup'][row.xpath('h4/text()').extract_first] = [x for x in dd]

        yield item



