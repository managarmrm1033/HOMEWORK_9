# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json

class QuotesScraperPipeline:

    def open_spider(self, spider):
        self.file_quotes = open('quotes.json', 'w')
        self.file_authors = open('authors.json', 'w')
        self.quotes = []
        self.authors = []

    def close_spider(self, spider):
        json.dump(self.quotes, self.file_quotes, ensure_ascii=False, indent=4)
        json.dump(self.authors, self.file_authors, ensure_ascii=False, indent=4)
        self.file_quotes.close()
        self.file_authors.close()

    def process_item(self, item, spider):
        if 'text' in item:
            self.quotes.append(dict(item))
        else:
            self.authors.append(dict(item))
        return item
