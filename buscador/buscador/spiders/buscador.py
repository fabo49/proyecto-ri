from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
#from scrapy.selector import HtmlXPathSelector
#from scrapy.http.request import Request
from scrapy.item import Item, Field
import os.path
import re

class Buscador(CrawlSpider):    
    if not os.path.exists("../docs"): os.makedirs("../docs")
    name = 'buscador'
    request_timeout = 120
    depth_limit = 4
    allowed_domains = ['londonmet.ac.uk']
    start_urls = [
        'http://www.londonmet.ac.uk/',
        'http://www.londonmet.ac.uk/faculties',
        'http://www.londonmet.ac.uk/contact-us/',
    ]

    rules = (
        Rule(SgmlLinkExtractor(allow=()), callback='parse_url', follow=True), 
    )

    # Guarda los docs con el nombre de la dir donde se obtuvo. Se utiliza un convenio de nombre '-' por '/'
    def parse_url(self, response):
    	page = response.url.split('/')
        name_Page = "|".join(page)
        filename = '../docs/%s.html' % name_Page
    	with open(filename, 'wb') as f:
    		f.write(response.body)
    		self.log('Archivo %s guardado satisfactoriamente' % filename)