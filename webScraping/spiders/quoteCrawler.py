import scrapy

class QuoteCrawler(scrapy.Spider):
    name = 'quoteCrawler'
    allowed_domains = ['toscrape.com']
    start_urls = ['https://quotes.toscrape.com/page/1/']
    base_url = 'https://quotes.toscrape.com'
    
    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'quote_text': quote.css('span.text::text').get(),
                'quote_author': quote.css('small.author::text').get(),
                'quote_tags': quote.css('div.tags').css('a.tag::text').getall()
            }

        next_page_meta = response.css('li.next >  a').attrib['href']

        if next_page_meta is not None:
            next_page_url = self.base_url + next_page_meta
            yield response.follow(next_page_url, callback=self.parse)

        
