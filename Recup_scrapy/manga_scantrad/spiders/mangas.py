import scrapy
import time
from scrapy import Request

class MangasSpider(scrapy.Spider):
    name = 'mangas'
    allowed_domains = ['manga-scantrad.io']
    start_urls = ['https://manga-scantrad.io']

    custom_settings = {
        'DOWNLOAD_DELAY': 10,
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',  # Imitation d'un navigateur réel
    }

    def parse(self, response):
        mangas = response.xpath('//div[@class="manga-title"]/a/text()').getall()
        
        for manga in mangas:
            yield {
                'title': manga.strip(),
            }
        
        # Pagination logic si nécessaire
        next_page = response.xpath('//a[@class="next page-numbers"]/@href').get()
        if next_page:
            time.sleep(10)
            yield Request(next_page, callback=self.parse)
