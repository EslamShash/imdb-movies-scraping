import scrapy
import re
from ..items import ImdbMoviesItem
class ImdbSpider(scrapy.Spider):
    name = 'imdb'
    start_urls = ['https://www.imdb.com/search/title/?title_type=tv_movie&user_rating=1.0,10.0']

    def parse(self, response):
        items = ImdbMoviesItem()
        movies = response.css(".mode-advanced")
        for movie in movies:
            items['name'] = movie.css(".lister-item-header a").css("::text").get()
            items['genre'] = movie.css(".genre::text").get()
            if items['genre'] is not None:
                items['genre'] = items['genre'].strip()
            items['year'] = re.search(r"(\d+)", movies.css(".text-muted.unbold").css("::text").get()).group()
            items['rating'] = movie.css(".ratings-imdb-rating strong").css("::text").get()
            if items['rating'] is not None:
                items['rating'] = float(items['rating'])
            items['director'] = movie.css(".text-muted+ p a:nth-child(1)").css("::text").get()
            items['votes'] = movie.css(".text-muted+ span").css("::text").get()
            if items['votes'] is not None:
                items['votes'] = int(re.sub(',', '', items['votes']))
            items['url'] = response.urljoin(movie.css(".lister-item-header a").css("::attr(href)").get())
            yield items
        next_page = response.css('a.next-page').css('::attr(href)').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)