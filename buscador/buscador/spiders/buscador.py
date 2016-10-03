from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import HtmlXPathSelector
from scrapy.http.request import Request
from scrapy.item import Item, Field
import os.path
import re

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
        Rule(SgmlLinkExtractor(), callback='parse', follow=False), 
    )

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        links = hxs.select('//a')
        for link in links:
            href = link.select('@href').extract()[0]
            self.log('href=%s' % href)
            if re.match('#', href[0]) is not True:
                if re.match('/', href):
                    href = response.url.join(href)
                    self.log('link = %s' % href)
                else:
                    self.log('link = %s' % href)
            yield Request(href, callback=self.parse_url)

    # Guarda los docs con el nombre de la dir donde se obtuvo. Se utiliza un convenio de nombre '-' por '/'
    def parse_url(self, response):
    	page = response.url.split('/')
        name_Page = "|".join(page)
        filename = 'docs/%s.html' % name_Page
    	with open(filename, 'wb') as f:
    		f.write(response.body)
    		self.log('Archivo %s guardado' % filename)