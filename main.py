import requests
import json


url_kfc = 'https://api.kfc.com/api/store/v2/store.get_restaurants' # адрес анализа
r = requests.get(url_kfc) # записываем ответ сервера в переменную r
address_kfc = r.json() # Получаем данные о ресторанах

count_restaurants = len(address_kfc['searchResults']) # Общее кол-во ресторанов КФС
data_json = {"count": count_restaurants,
             "restaurants": []}


def get_rest(address_kfc,number):
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


def main_rest():
    # Пробегаем по всем значениям, если не пустые и не вызывают ошибок добавляем в базу
    for id in range(count_restaurants):
        if get_rest(address_kfc, id)!=False:
            data_json['restaurants'].append(get_rest(address_kfc, id))
    # Сохраняем всю базу в файл
    with open('d:\data_rest_kfc.txt', 'w') as outfile:
        json.dump(data_json, outfile, ensure_ascii=False)


if __name__ == "__main__":
	main_rest()