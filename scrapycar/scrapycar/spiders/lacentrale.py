import scrapy
import os
from bs4 import BeautifulSoup
from time import sleep
import unicodedata

from ..tools import clear_string, clear_price, clear_lieu
from ..items import AnnonceItem

# lancement : scrapy crawl lacentrale_spider -a recherche='Mercedes CLA' -o annonces_lacentrale.csv


class LacentraleSpider(scrapy.Spider):
    def __init__(self, recherche='', **kwargs):
        self.recherche = recherche.replace(' ', '%3A')
        super().__init__(**kwargs)

    name = "lacentrale_spider"
    url = "https://www.lacentrale.fr"

    def start_requests(self):
        url = self.url + f'/listing?makesModelsCommercialNames={self.recherche}&options=&page=1'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        liste_annonces = response.css('div.adLineContainer')
        
        for annonce in liste_annonces:
            model = scrapy.Selector(text=annonce.css('span[class^="searchCard__makeModel"]').get().replace('<!-- -->', ' ')).css('::text').get()
            version = scrapy.Selector(text=annonce.css('span[class^="searchCard__version"]').get().replace('<!-- -->', ' ')).css('::text').get()
            prix = annonce.css('div[class="searchCard__fieldPrice"] ::text').get()
            departement = annonce.css('div[class="searchCard__dptCont"] ::text').get()
            annee = annonce.css('div[class="searchCard__year"] ::text').get()
            km = annonce.css('div[class="searchCard__mileage"] ::text').get()
            
            titre = clear_string(model) + ' ' + clear_string(version)
            prix = clear_price(prix)
            annee = int(annee)
            departement = int(departement)
            km = unicodedata.normalize("NFKD", km)
            km = int(km.split('km')[0].replace(' ', ''))
            
            print(f'{titre} :: {prix}€ :: annee {annee} :: {km}km :: {departement}')
            
            
        # On parcourt la page suivante si il y en a une
        suiv = response.xpath('//a[@title="Page suivante"]/@href').extract_first()
        if suiv:
            next_page = self.url + suiv
            sleep(10) # sleep 10 seconds
            yield scrapy.Request(url=next_page, callback=self.parse)