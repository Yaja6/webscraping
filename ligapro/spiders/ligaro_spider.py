import scrapy
from scrapy import Spider
from scrapy import Selector
from ligapro.items import LigaproItem
class LigaroSpiderSpider(scrapy.Spider):
    name = 'ligaro_spider'
    allowed_domains = ['ligapro.ec']
    start_urls = [
    'http://ligapro.ec/',
    'https://ligapro.ec/team/5?page=1',
    'https://ligapro.ec/team/5?page=2',
    'https://ligapro.ec/team/5?page=3',
    'https://ligapro.ec/team/5?page=4',
    'https://ligapro.ec/team/5?page=5'
    ]

    def parse(self, response):
        datos=Selector(response).xpath('//div[@class="inmersive-card w-100"]')
          
        for dato in datos:
        	item=LigaproItem()
        	item['fecha']=dato.xpath('div[1]/small[@class="created"]/text()').extract()[0]
        	item['titulo']=dato.xpath('div[2]/div/div[1]/div[1]/h5/a[@class="inmersive-title"]/text()').extract()[0]
        	item['url']=dato.xpath('div[2]/div/div[1]/div[1]/h5/a[@class="inmersive-title"]/@href').extract()[0]
        	yield item
