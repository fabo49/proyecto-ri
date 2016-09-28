import scrapy

class QuotesSpider(scrapy.Spider):
	name = "quotes"
	start_urls = [
		'http://quotes.toscrape.com/page/1/',
		'http://ecci.ucr.ac.cr/',
	]

	def parse(self, response):
		page = response.url.split("/")[-2]
		filename = 'quotes-%s.html' % page 
		with open(filename, 'wb') as f:
			f.write(response.body)

		for quote in response.css('div.quote'):
			yield {
				'text': quote.css('span.text::text').extract_first(),
				'author': quote.css('span small::text').extract_first(),
				'tags': quote.css('div.tags a.tag::text').extract(),
			}

		next_page = response.css('li.next a::attr(href)').extract_first()
		if next_page is not None:
			next_page = response.urljoin(next_page)
			yield scrapy.Request(next_page, callback=self.parse)