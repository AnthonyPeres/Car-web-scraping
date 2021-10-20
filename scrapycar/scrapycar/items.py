# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AnnonceItem(scrapy.Item):
    titre = scrapy.Field()
    # date = scrapy.Field()
    prix = scrapy.Field()
    ville = scrapy.Field()
    departement = scrapy.Field()
    annee = scrapy.Field()
    kilometrage = scrapy.Field()
    carburant = scrapy.Field()
    boite = scrapy.Field()
    site = scrapy.Field()
    