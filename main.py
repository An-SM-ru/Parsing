import requests
from bs4 import BeautifulSoup # Для анализа html/css кода

url_kfc = 'https://api.kfc.com/api/store/v2/store.get_restaurants' # адрес анализа

r = requests.get(url_kfc) # записываем ответ сервера в переменную r

address_kfc = r.json() # Получаем данные о ресторанах

class Rest_KFC():

    def __init__(self, address_kfc, number):
        self._number = number
        self._address_kfc = address_kfc

        self.rest_title = self._address_kfc['searchResults'][self._number]['storePublic']['title']['ru']
        self.rest_address = self._address_kfc['searchResults'][self._number]['storePublic']['contacts']['streetAddress']['ru']

kfc = Rest_KFC(address_kfc, 10)
print(f'Название "{kfc.rest_title}" по адресу: {kfc.rest_address}')