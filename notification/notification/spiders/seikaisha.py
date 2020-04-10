import scrapy
from bs4 import BeautifulSoup

from notification.items import Book


class SeikaishaSpider(scrapy.Spider):
    name = 'seikaisha'
    allowed_domains = ['www.seikaisha.co.jp']
    start_urls = ['https://www.seikaisha.co.jp/#publication']

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')
        books = []
        for section in soup.select('#publication > section'):
            book = Book()
            book['title'] = section.select_one('.entry-title a').text
            book['author'] = section \
                .select_one('.publication-meta > dd:nth-of-type(1)') \
                .text

            book['publishing_date'] = \
                section.select_one('.release-date .year').text \
                + section.select_one('.release-date .month').text \
                + section.select_one('.release-date .day').text

            books.append(book)
        print(books)