import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

from mongoengine import connect
import json
import configparser
from models import Author, Quote

# Конфігурація MongoDB
config = configparser.ConfigParser()
config.read('config.ini')

mongo_user = config.get('DB', 'user')
mongodb_pass = config.get('DB', 'pass')
db_name = config.get('DB', 'db_name')
domain = config.get('DB', 'domain')

connection_string = f"mongodb+srv://{mongo_user}:{mongodb_pass}@{domain}/{db_name}?retryWrites=true&w=majority"
connect(host=connection_string, ssl=True)

def load_authors():
    with open('authors.json', encoding='utf-8') as f:
        authors_data = json.load(f)
        for author in authors_data:
            Author(
                fullname=author['name'],
                born_date=author.get('birthdate', ''),
                born_location='',
                description=author.get('bio', '')
            ).save()

def load_quotes():
    with open('quotes.json', encoding='utf-8') as f:
        quotes_data = json.load(f)
        for quote in quotes_data:
            author = Author.objects(fullname=quote['author']).first()
            if author:
                Quote(
                    tags=quote.get('tags', []),
                    author=author,
                    quote=quote['text']
                ).save()

if __name__ == "__main__":
    load_authors()
    load_quotes()
