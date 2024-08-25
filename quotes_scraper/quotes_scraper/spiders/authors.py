import scrapy
from quotes_scraper.items import AuthorItem

class AuthorsSpider(scrapy.Spider):
    name = 'authors'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        author_links = response.css('div.quote span a::attr(href)').getall()
        for link in author_links:
            yield response.follow(link, self.parse_author)

        next_page = response.css('li.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)

    def parse_author(self, response):
        author_item = AuthorItem()
        author_item['name'] = response.css('h3.author-title::text').get().strip()
        author_item['birthdate'] = response.css('span.author-born-date::text').get()
        author_item['bio'] = response.css('div.author-description::text').get().strip()
        yield author_item
