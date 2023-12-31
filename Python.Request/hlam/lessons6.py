import requests
from bs4 import BeautifulSoup
import pandas
import postgres_client


links_to_pars = [
    'https://www.kufar.by/l/r~brest/mebel',
    'https://www.kufar.by/l/r~brest/mebel?cursor=eyJ0IjoiYWJzIiwiZiI6dHJ1ZSwicCI6Mn0%3D',
    'https://www.kufar.by/l/r~brest/mebel?cursor=eyJ0IjoiYWJzIiwiZiI6dHJ1ZSwicCI6M30%3D',
    'https://www.kufar.by/l/r~brest/mebel?cursor=eyJ0IjoiYWJzIiwiZiI6dHJ1ZSwicCI6NH0%3D',
    'https://www.kufar.by/l/r~brest/mebel?cursor=eyJ0IjoiYWJzIiwiZiI6dHJ1ZSwicCI6NX0%3D'
]


def get_mebel_by_link(link):
    response = requests.get(link)
    mebel_data = response.text

    mebel_items = []
    to_parse = BeautifulSoup(mebel_data, 'html.parser')
    for elem in to_parse.find_all('a', class_='styles_wrapper__yaLfq'):
        try:
            prise, decription = elem.text.split('р.')
            mebel_items.append((
                elem['href'],
                int(prise.replace(' ', '')),
                decription
                )
            )
        except:
            print(f'Цена не была указана. {elem.text}')
    return mebel_items


def save_to_csv(mebel_items):
    pandas.DataFrame(mebel_items).to_csv('../lessons 6 postgress/mebel.csv', index=False)


def save_to_sqlite3(mebel_items):
    connection = postgres_client.get_connection()
    for item in mebel_items:
        postgres_client.insert(connection, item[0], item[1], item[2])


def run():
    mebel_items = []
    for link in links_to_pars:
        mebel_items.extend(get_mebel_by_link(link))
    save_to_csv(mebel_items)


run()
