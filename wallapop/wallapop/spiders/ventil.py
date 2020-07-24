import scrapy
from scrapy import Spider
from scrapy import Selector
from wallapop.items import WallapopItem

class VentilSpider(scrapy.Spider):
    name = 'ventil'
    allowed_domains = ['es.wallapop.com']
    start_urls = ['https://es.wallapop.com/electrodomesticos/aire-acondicionado#!']

    def parse(self, response):
        prods=Selector(response).xpath('//div[@class="card-product-product-info"]')

        for p in prods:
        	item=WallapopItem()
        	item['nombre']=p.xpath('span/text()').extract()[0]
        	item['precio']=p.xpath('div/span/text()').extract()[0]
        	item['descripcion']=p.xpath('p/text()').extract()[0]
        	yield item
