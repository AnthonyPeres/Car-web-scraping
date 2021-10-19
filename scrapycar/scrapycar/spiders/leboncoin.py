import scrapy
import os
from bs4 import BeautifulSoup
from time import sleep

from ..tools import clear_string, clear_price, clear_lieu
from ..items import AnnonceLeboncoinItem

# lancement : scrapy crawl leboncoin_spider -a recherche='Mercedes classe cla' -o annonces.csv

class LeboncoinSpider(scrapy.Spider):
    def __init__(self, url='https://www.leboncoin.fr', recherche='', **kwargs):
        self.url = url
        self.recherche = recherche.replace(' ', '%20')
        super().__init__(**kwargs)
    
    name = "leboncoin_spider"
    
    def start_requests(self):
        url = self.url + f'/recherche?category=2&text={self.recherche}&page=1'
        yield scrapy.Request(url=url, callback=self.parse)
            
    def parse(self, response):

        print(response.url)
        suiv = response.xpath('//a[@title="Page suivante"]/@href').extract_first()
        next_page = self.url + suiv
        
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse)
            
        # liste_annonces = response.css('div[class^="styles_adCard"]')
                
        # for annonce in liste_annonces:
        #     titre = annonce.css('p ::attr(title)').get()
        #     prix = annonce.css('div[aria-label^="Prix"] ::attr(aria-label)').get()
        #     lieu = annonce.css('span[aria-label^="Située"] ::text').get()
        #     annee = annonce.xpath(".//span[contains(text(), 'Année')]/../../p[2]/span/text()").get()
        #     km = annonce.xpath(".//span[contains(text(), 'Kilométrage')]/../../p[2]/span/text()").get()
        #     carburant = annonce.xpath(".//span[contains(text(), 'Carburant')]/../../p[2]/span/text()").get()
        #     boite = annonce.xpath(".//span[contains(text(), 'Boîte')]/../../p[2]/span/text()").get()

        #     # modifications si besoin
        #     titre = clear_string(titre)
        #     prix = clear_price(prix)
        #     ville, departement = clear_lieu(lieu)
        #     aneee = int(annee)
        #     km = int(km.split(' ')[0])
            
        #     annonce = AnnonceLeboncoinItem()
        #     annonce['titre'] = titre
        #     annonce['prix'] = prix
        #     annonce['ville'] = ville
        #     annonce['departement'] = departement
        #     annonce['annee'] = annee
        #     annonce['kilometrage'] = km
        #     annonce['carburant'] = carburant
        #     annonce['boite'] = boite
        #     yield annonce