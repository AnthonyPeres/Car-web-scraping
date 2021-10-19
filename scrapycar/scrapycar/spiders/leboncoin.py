import scrapy
from bs4 import BeautifulSoup
import os
from ..tools import clear_string, clear_price, clear_lieu
from ..items import AnnonceLeboncoinItem

# lancement : scrapy crawl leboncoin_spider -a recherche='Mercedes classe cla' -o annonces.csv

class LeboncoinSpider(scrapy.Spider):
    def __init__(self, recherche='', **kwargs):
        self.recherche = recherche 
        super().__init__(**kwargs)
    
    name = "leboncoin_spider"
    
    def start_requests(self):
        # url_base = 'https://www.leboncoin.fr/recherche?category=2&text='
        # url = self.url_base + self.recherche.replace(' ', '%20') + '&page=' + '1'
        BASE_DIR = str(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))).split('/')[:-1]
        
        parent = "/".join(BASE_DIR)
        print(parent)
        # BASE_DIR = BASE_DIR
        urls = [
            'https://www.leboncoin.fr/recherche?category=2&text=Mercedes%20classe%20cla&page=1',
            # f"file://{parent}/Mercedes_classe_cla.html"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
        
        # yield Request(url=url, callback=self.parse)
    

    def parse(self, response):
        # filename = self.recherche.replace(' ', '_') + '.html'
        # with open(filename, 'wb') as f:
            # f.write(response.body)
        
        
        
        
        # soup = BeautifulSoup(response.text, 'html.parser')
        # print(soup.prettify())
        # liste = soup.body.findAll('div', {'class':'sc-hZSUBg'})
        
        # i = 0
        # for annonce in liste:
        #     titre = annonce.find('p', {'class':'sc-jDwBTQ'}).text
        #     new_titre = clear_string(titre)
            
        #     div_prix = annonce.find('div', {'class':'sc-brqgnP'})
        #     prix = div_prix.find('span', {'class':'_3Wx6b'}).text
        #     new_prix = clear_string(prix)
            
        #     # div_info_1 = annonce.findAll('div', {'class':'sc-iRbamj'})[0]
        #     # annee = div_annee.findAll('p')
            
        #     print(f'{new_titre}, prix : {new_prix}')


        if response.status == 200:
            liste_annonces = response.css('div[class^="styles_adCard"]')
                    
            for annonce in liste_annonces:
                titre = annonce.css('p ::attr(title)').get()
                prix = annonce.css('div[aria-label^="Prix"] ::attr(aria-label)').get()
                lieu = annonce.css('span[aria-label^="Située"] ::text').get()
                annee = annonce.xpath(".//span[contains(text(), 'Année')]/../../p[2]/span/text()").get()
                km = annonce.xpath(".//span[contains(text(), 'Kilométrage')]/../../p[2]/span/text()").get()
                carburant = annonce.xpath(".//span[contains(text(), 'Carburant')]/../../p[2]/span/text()").get()
                boite = annonce.xpath(".//span[contains(text(), 'Boîte')]/../../p[2]/span/text()").get()

                # modifications si besoin
                titre = clear_string(titre)
                prix = clear_price(prix)
                ville, departement = clear_lieu(lieu)
                aneee = int(annee)
                km = int(km.split(' ')[0])
                
                annonce = AnnonceLeboncoinItem()
                annonce['titre'] = titre
                annonce['prix'] = prix
                annonce['ville'] = ville
                annonce['departement'] = departement
                annonce['annee'] = annee
                annonce['kilometrage'] = km
                annonce['carburant'] = carburant
                annonce['boite'] = boite
                yield annonce
                
                
                # print(f'{titre}: {prix}€, {annee}, {km}km, {carburant}, {boite}, a {ville} dans le {departement}')
                
