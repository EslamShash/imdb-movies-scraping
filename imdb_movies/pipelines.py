# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3

class ImdbMoviesPipeline:
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect('imdb.db')
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS imdb""")
        self.curr.execute("""CREATE TABLE imdb(
            name text,
            genre text,
            year int,
            rating float,
            director text,
            votes int,
            url text
        )""")
    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        self.curr.execute("""INSERT INTO imdb VALUES(?,?,?,?,?,?,?)""",(
            item['name'],
            item['genre'],
            item['year'],
            item['rating'],
            item['director'],
            item['votes'],
            item['url']
                          ))
        self.conn.commit()