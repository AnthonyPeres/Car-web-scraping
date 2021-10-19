# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AnnonceLeboncoinItem(scrapy.Item):
    nom = scrapy.Field()
    # date = scrapy.Field()
    prix = scrapy.Field()
    lieu = scrapy.Field()
    annee = scrapy.Field()
    kilometrage = scrapy.Field()
    carburant = scrapy.Field()
    boite = scrapy.Field()
    