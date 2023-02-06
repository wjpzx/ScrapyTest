import scrapy


class DangdangSpider(scrapy.Spider):
    name = "dangdang"
    allowed_domains = ["e.dangdang,com"]
    start_urls = ["http://e.dangdang,com/"]

    def parse(self, response):
        pass
