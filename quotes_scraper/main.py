from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

def run_spiders():
    process = CrawlerProcess(get_project_settings())
    process.crawl('quotes')  # Для спайдера цитат
    process.crawl('authors')  # Для спайдера авторів
    process.start()

if __name__ == "__main__":
    run_spiders()
