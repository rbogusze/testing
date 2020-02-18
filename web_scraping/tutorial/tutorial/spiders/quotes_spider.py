import scrapy
import datetime


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):

        # here I can do everything that I can do in interactive mode
        title = response.css('title::text').get()
        date = datetime.date.today()

        print('Hello--------------')
        #print(dir(response.request))
        #print(response.request.headers)
        print(date)
        print('/Hello--------------')

        # he is looping here through div.quote class, as visible in html source code, that is why title is not here
        for quote in response.css('div.quote'):
            #print (dir(quote))
            yield {
                'date': date,
                'url': response.request.url,
                'title': title,
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }
