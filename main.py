import requests
import json


path_json_kfc = 'c:\data_rest_kfc.txt'
url_kfc = 'https://api.kfc.com/api/store/v2/store.get_restaurants' # адрес анализа

r = requests.get(url_kfc) # записываем ответ сервера в переменную r
address_kfc = r.json() # Получаем данные о ресторанах

count_restaurants = len(address_kfc['searchResults']) # Общее кол-во ресторанов КФС
data_json_kfc = {"count": 0,
                 "restaurants": []}


def get_rest_kfc(address_kfc,number):
    # Пробегаем по нужным нам полям, получаем значения
    try:
        rest_name = address_kfc['searchResults'][number]['storePublic']['title']['ru']
        rest_address = address_kfc['searchResults'][number]['storePublic']['contacts']['streetAddress']['ru']
        rest_city = address_kfc['searchResults'][number]['storePublic']['contacts']['city']['ru']
        rest_coordinates = address_kfc['searchResults'][number]['storePublic']['contacts']['coordinates']['geometry']['coordinates']
        # Возвращаем словарь с нужными нам полями
        return {"id": number+1,
               "name": rest_name,
               "address": rest_address,
               "city": rest_city,
               "coordinates": rest_coordinates}
    except:
        # Если значения ошибочные то ничего не возвращаем
        return False


def create_json_rest_kfc():
    # Пробегаем по всем значениям, если не пустые и не вызывают ошибок добавляем в базу
    for id in range(count_restaurants):
        if get_rest_kfc(address_kfc, id)!=False:
            data_json_kfc['count'] += 1
            data_json_kfc['restaurants'].append(get_rest_kfc(address_kfc, id))


def save_json_rest_kfc(path):
    # Сохраняем всю базу в файл по указанному пути
    with open(path, 'w') as outfile:
        json.dump(data_json_kfc, outfile, ensure_ascii=False)


if __name__ == "__main__":
    create_json_rest_kfc()
    save_json_rest_kfc(path_json_kfc)