import base64
from urllib import response
import requests
import json
from bs4 import BeautifulSoup as bs
import lxml
from fake_useragent import UserAgent

ua = UserAgent()
#print(ua.random)


def collect_data(types=2):
    # response = requests.get(url=url, headers={'user-agent': f'{ua.random}'})
    #
    # with open('result.json', 'w', encoding='utf-8') as file:
    #     json.dump(response.json(), file, indent=4, ensure_ascii=False)
    #     print('JSON записан успешно, брат')
    offset = 0
    zina_size = 60
    result = []
    count = 0
    while True:
        for item in range(offset, offset + zina_size, 60):
            url = f'https://inventories.cs.money/5.0/load_bots_inventory/730?buyBonus=40&isStore=true&limit=60&maxPrice=10000&minPrice=3000&offset={item}&sort=botFirst&type={types}&withStack=true'
            response = requests.get(
                url=url,
                headers = {'user-agent': f'{ua.random}'}
            )

            offset += zina_size

            data = response.json()
            items = data.get('items')

            for i in items: # Условие на скидку не мене 10 процентов
                if i.get('overprice') is not None and i.get('overprice') < -10:
                    item_full_name = i.get('fullName')
                    item_3d = i.get('3d')
                    item_price = i.get('price')
                    item_over_price = i.get('overprice')

                    result.append(
                        {
                            'full_name': item_full_name,
                            '3d': item_3d,
                            'item_price': item_price,
                            'overprice': item_over_price
                        }

                    )
        count += 1
        print(f'Page #{count}')
        print(url)

        if len(items) < 60: # Условие на окончание

            break
    with open('result.json', 'w', encoding='utf-8') as file:
        json.dump(result, file, indent=4, ensure_ascii=False)


    print(len(result))

def main():
    collect_data()

if __name__=='__main__':
    main()
