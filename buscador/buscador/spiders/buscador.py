from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.item import Item, Field
import os.path

class Buscador(CrawlSpider):
    name = 'buscador'
    allowed_domains = [
        'www.bbc.co.uk',
        "www.bbc.com/",
    ]
    start_urls = [
        'http://www.bbc.co.uk',
        "http://www.bbc.com/",
    ]

    rules = (
        Rule(SgmlLinkExtractor(), callback='parse_url', follow=False), 
    )

    # Guarda los docs con el nombre de la dir donde se obtuvo. Se utiliza un convenio de nombre '-' por '/'
    def parse_url(self, response):
	# Falta arreglar el nombre de los archivos ya guardado.
    	page = response.url.split('/')
        name_Page = "|".join(page)
        filename = 'docs/%s.html' % name_Page
    	with open(filename, 'wb') as f:
    		f.write(response.body)
    		self.log('Archivo %s guardado' % filename)