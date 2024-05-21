# https://github.com/netology-code/py-homeworks-advanced/tree/new_hw_scrapping/6.Web-scrapping

from pprint import pprint

import requests
from unicodedata import normalize
from bs4 import BeautifulSoup as bs
from fake_headers import Headers
import json

areas = ['1']
search_txt = 'python django flask'


class HH:
    HOST = "https://spb.hh.ru/search/vacancy"

    def __init__(self):
        self.headers = Headers(browser='chrome', os='win').generate()

    def get_vacancy(self, search_tags, areas=('1',)):
        page = 0
        vacancy_lst = []
        while True:

            params = {
                'text': search_tags,
                'area': areas,
                'page': page,
                'items_on_page': '20',
            }
            vacancy_html = requests.get(self.HOST, headers=self.headers, params=params).text
            vacancy_list_pars_all = bs(vacancy_html, features='lxml').find_all(class_="vacancy-serp-item__layout")
            if vacancy_list_pars_all:
                for vacancy in vacancy_list_pars_all:
                    h2 = vacancy.find('h2', {'data-qa': 'bloko-header-2'})
                    salary = ''
                    if vacancy.find('span', class_='bloko-header-section-3'):
                        salary = vacancy.find('span', class_='bloko-header-section-3').get_text()
                    employer = vacancy.find(class_="vacancy-serp-item__meta-info-company").text
                    address = list(vacancy.find(class_="vacancy-serp-item__info").children)[1].text
                    vacancy_lst.append(
                        {'href': vacancy.find('a', target="_blank").attrs.get("href"),
                         'employer': normalize('NFKD', employer),
                         'salary': normalize('NFKD', salary),
                         'address': normalize('NFKD', address)

                         }
                    )
                page += 1
            else:
                return vacancy_lst


hh = HH()
vac_lst = hh.get_vacancy(search_txt, areas)
with open("data_file.json", "w", encoding="utf-8") as f:
    f.write(json.dumps(vac_lst))
pprint(vac_lst)
