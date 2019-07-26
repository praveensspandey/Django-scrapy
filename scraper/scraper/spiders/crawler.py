# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from scraper.items import ScraperItem

class CrawlerSpider(scrapy.Spider):
    name = 'crawler'
    allowed_domains = ["imdb.com"]
    start_urls = ["https://www.imdb.com/chart/boxoffice"]

    def parse(self, response):
        links = response.xpath('//*[@class="titleColumn"]/a/@href').extract()
        for link in links:
            absolute_url = response.urljoin(link)
            yield Request(absolute_url, callback=self.parse_movie)

    def parse_movie(self, response):
        item = ScraperItem()

        item['title'] = response.xpath('//h1/text()').extract_first()
        item['year']=response.xpath('//*[@id="titleYear"]/a/text()').extract_first()
        # rating= response.xpath('//*[@itemprop="ratingValue"]/text()').extract_first()
        # director=response.xpath('//*[@id="title-overview-widget"]/div[2]/div[1]/div[2]/a/text()').extract_first()
        # writer=response.xpath('//*[@id="title-overview-widget"]/div[2]/div[1]/div[3]/a[1]/text()').extract_first()
        # release_date=response.xpath('//*[@id="titleDetails"]/div[4]/text()').extract()
        # release_date=release_date[1].strip()
        yield item

