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

    def __init__(
            self,
            vacancy_tag="serp-item serp-item_simple serp-item_link serp-item-redesign",
            salary_tag="compensation-text--cCPBXayRjn5GuLFWhGTJ fake-magritte-primary-text--qmdoVdtVX3UWtBb3Q7Qj "
                       "separate-line-on-xs--pwAEUI79GJbGDu97czVC",
            employer_tag="vacancy-name--SYbxrgpHgHedVTkgI_cA serp-item__title-link serp-item__title-link_redesign",
            address_tag="vacancy-serp__vacancy-address"
    ):
        self.headers = Headers(browser='chrome', os='win').generate()
        self.vacancy_tag = vacancy_tag,
        self.salary_tag = salary_tag
        self.employer_tag = employer_tag
        self.address_tag = address_tag

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
            vacancy_list_pars_all = bs(vacancy_html, features='lxml').find_all(class_=self.vacancy_tag)
            if vacancy_list_pars_all:
                for vacancy in vacancy_list_pars_all:
                    is_salary = vacancy.find('span', class_=self.salary_tag)
                    salary = normalize('NFKD', is_salary.get_text()) if is_salary else ""
                    employer = normalize('NFKD', vacancy.find(class_=self.employer_tag).text)
                    address = normalize('NFKD', vacancy.find('span', {"data-qa": self.address_tag}).text)
                    vacancy_lst.append(
                        {'href': vacancy.find('a', target="_blank").attrs.get("href"),
                         'employer': employer,
                         'salary': salary,
                         'address': address
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
