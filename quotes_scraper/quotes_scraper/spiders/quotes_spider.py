import scrapy
from quotes_scraper.items import QuoteItem

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        quotes = response.css('div.quote')
        for quote in quotes:
            item = QuoteItem()
            item['text'] = quote.css('span.text::text').get().strip('“”')
            item['author'] = quote.css('small.author::text').get()
            item['tags'] = quote.css('div.tags a.tag::text').getall()
            yield item

        next_page = response.css('li.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)
