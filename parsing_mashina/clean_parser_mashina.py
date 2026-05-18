import requests 
from bs4 import BeautifulSoup 
import pandas as pd 
import re 
import time
from urllib.parse import urljoin

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}


# функция проверки html
def get_html(url):
    try:
        response = requests.get(url, headers=HEADERS)

        if response.status_code == 200:
            return response
        
    except Exception as e:
        print(e)

        return None
    
# функция для получения ссылок
def parse_catalog(response):
    data = response.json()
    # смотрим какие есть ключи в json объекте
    # print(data.keys())
    # вытаскиваем весь список машин
    car_list = data['items']
    page_data = []
    for car in car_list:
        car_info = {
            'title' : car.get('title'),
            'slug' : car.get('slug'),
            'url' : urljoin('https://www.mashina.kg/details/', car.get('slug', ''))
        }
    
        for p in car.get('prices', []):
            if p.get('currency') == "USD":
                car_info['price_usd'] = p.get('amount')
            elif p.get('currency') == 'KGS':
                car_info['price_kgs'] = p.get('amount')
        
        for attr in car.get('attributes', []):
            attr_name = attr.get('name')
            attr_slug = attr.get('slug')

            attr_value = attr.get('value_text') if attr.get('value_text') else attr.get('value_number')

            if attr_slug and attr_value:
                car_info[attr_name] = attr_value
        page_data.append(car_info)
        
    return page_data
# Главная функция
def main():
    all_cars = []
    for page in range(1, 21):
        api_url = f'https://mashina.kg/api/mbank-proxy/v1/ads/listings?category_id=1&sort_by=created_at&order=desc&page={page}&size=21'
        response = get_html(api_url)        
        
        # проверка странцы
        if response:
            links = parse_catalog(response)
            # print(len(links))
            # print(links[0])
            all_cars.extend(links)
        
        time.sleep(1)
    print(len(all_cars))
    # Превращаем наш огромный список словарей в красивую таблицу Dataframe
    df = pd.DataFrame(all_cars)
    
    # Сохраняем в CSV файл без лишних индексов, с кодировкой utf-8-sig (чтобы русский текст в Excel открывался ровно)
    df.to_csv('mashina_catalog.csv', index=False, encoding='utf-8-sig')
    print("Данные успешно сохранены в файл mashina_catalog.csv!")

main()