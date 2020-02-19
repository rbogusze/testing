import scrapy
import datetime
import urlparse


class QuotesSpider(scrapy.Spider):
    name = "lodz"
    start_urls = [
        'https://bip.uml.lodz.pl/urzad-miasta/przetargi/zamowienia-publiczne-powyzej-30000-euro/',
    ]

    def parse(self, response):

        # here I can do everything that I can do in interactive mode
        title = response.css('title::text').get()
        date = datetime.date.today()

        #print('Hello--------------')
        #print(dir(response.request))
        #print(response.request.headers)
        #print(date)
        #print('/Hello--------------')

        # he is looping here through div.quote class, as visible in html source code, that is why title is not here
        for quote in response.css('div.article-item.article-item--gold.article-item--type-0'):
            #base_url = '{uri.scheme}://{uri.netloc}/'.format(uri=urlparse(response.request.url))
            base_url = urlparse.urljoin(response.request.url, '/')

            print('Hello--------------')
            print('url:')
            print(response.request.url)
            print(base_url)
            print(quote.css('h3.article-item__title a::attr(href)').get())
            print(base_url.rstrip("/") + quote.css('h3.article-item__title a::attr(href)').get())
            print('title:')
            print(quote.css('span::text').get().lstrip())
            print('text:')
            print(quote.css('h3.article-item__title a::text').get().lstrip())
            print('/Hello--------------')
            yield {
                'date': date,
                'url': base_url.rstrip("/") + quote.css('h3.article-item__title a::attr(href)').get(),
                'title': quote.css('span::text').get().lstrip(),
                'text': quote.css('h3.article-item__title a::text').get().lstrip(),
                'author': 'UML',
            }
