import json
from bs4 import BeautifulSoup
import requests
from threading import Thread
import os
import time
from core.models import FontionBooks

class SinglePageBS4(Thread):

    def __init__(self, url , page):
        Thread.__init__(self)
        self.url = url
        self.page = page
        self.fileName = str(f'html{page}.html')

    def loadPage(self):
        print(f'Start load page {self.page}  .....')
        self.web = requests.get(self.url)

    def saveHtmlResponse(self):
        try:
            with open(self.fileName,'wb') as f:
                f.write(self.web.content)
        except Exception as e:
            print(e)

    def extratData(self):
        # with open(self.fileName, "r") as html_file:
        #     html = html_file.read()
        soup = BeautifulSoup(self.web.content, 'html.parser')
        products = []
        for tag in soup.find_all('script'):

                if tag.string is not None:
                    if len(tag.string) > 10000 :
                        if tag.string.startswith('window'):
                            text = tag.string[16:len(tag.string)-1]
                            json_object = json.loads(str(text))
                            productList = json_object['state']['productList']['response']['results']
                            for prod in productList:
                                try:
                                    products.append(FontionBooks(
                                        productId=prod['productId'],
                                        productType=prod['productType'],
                                        imageUrl=prod['imageUrl'],
                                        name=prod['name'],
                                        currency=prod['currency'],
                                        sku=prod['sku'],
                                        urlSlug=prod['urlSlug'],
                                        title=prod['title'],
                                        author=prod['author'],
                                        description=prod['description'],
                                        price=prod['price'],
                                        formatType=prod['formatType'],
                                    ))
                                except:
                                    print('error insert data')
                                    print(prod['productId'] ,prod['name'])

                            try:
                                FontionBooks.objects.bulk_create(products)
                            except Exception as e:
                                print('error insert bulk' , e)
        if os.path.exists(self.fileName):
            os.remove(self.fileName)
        print(f'End load page {self.page}  .....')


    def run(self):
        try:
            self.loadPage()
            # self.saveHtmlResponse()
            self.extratData()
        except:
          print('error')
