from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.item import Item, Field


class MyItem(Item):
    url= Field()


class Buscador(CrawlSpider):
    name = 'buscador'
    allowed_domains = ['ucr.ac.cr']
    start_urls = ['http://www.ecci.ucr.ac.cr/','http://www.ucr.ac.cr/']

    rules = (Rule(SgmlLinkExtractor(), callback='parse_url', follow=False), )

    def parse_url(self, response):
	# Falta arreglar el nombre de los archivos ya guardado.
	page = response.url.split("/")[-1]
	filename = 'docs/ecci_%s.html' % page	
	with open(filename, 'wb') as f:
		f.write(response.body)
		self.log('Archivo %s guardado' % filename)

        item = MyItem()
        item['url'] = response.url
        return item
