import requests
from bs4 import BeautifulSoup
import sys

def find_preview(url, page_num, keywords, headers):
    soup = get_request(url + str(page_num), headers)
    articls = soup.find_all(class_='tm-article-snippet')
    for article in articls:
        txt_set = set(_.lstrip('*').lower() for _ in article.text.split())
        search_ref = article.find(class_='tm-article-snippet__readmore')
        article_url = 'https://habr.com' + search_ref.attrs['href']
        if keywords & txt_set: 
            print_article_title (article, article_url)
            print('В превью статьи найдены слова: ' + str(keywords & txt_set))
        else:
            find_text_result = find_article(article_url, keywords, headers)
            if find_text_result:
                print_article_title (article, article_url)
                print(find_text_result)

def get_request(url, headers):
    try:        
        ret = requests.get(url, headers=headers)
    except Exception as exc:
        print('При запросе возникла ошибка: ' + str(exc))
        print('Проверьте подключение к интернету.')
        sys.exit()
    soup = BeautifulSoup(ret.text, features='html.parser')
    return soup

def find_article(url, keywords, headers):
    soup = get_request(url, headers)
    article = soup.find(id='post-content-body')
    txt_set = set(_.lstrip('*').lower() for _ in article.text.split())
    if keywords & txt_set:
        return 'В тексте статьи найдены слова: ' + str(keywords & txt_set)  

def print_article_title (article, article_url):
    datetime_published = article.find(class_='tm-article-snippet__datetime-published')
    title_article = article.find(class_='tm-article-snippet__title tm-article-snippet__title_h2')
    print(f"\n{datetime_published.contents[0].attrs['title'].partition(',')[0]}"
        f" - {title_article.text} - {article_url}")

if __name__ == '__main__':
    KEYWORDS = {'дизайн', 'фото', 'web', 'python'}
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0'
    }
    URL = 'https://habr.com/ru/all/page'
    page_start = ''
    page_end = ''
    while not page_start.isdigit():
        page_start = input('Введите начальную старницу поиска (по умолчанию 1, "q - выход"): ')
        if page_start == 'q':
            sys.exit()
        elif not page_start:
            page_start = '1'
    while not page_end.isdigit():
        page_end = input('Введите конечную старницу поиска (по умолчанию равно начальной, "q - выход"): ')
        if page_end == 'q':
            sys.exit()
        elif not page_end or int(page_end) < int(page_start):
            page_end = page_start
        elif page_end == 'q':
            sys.exit()
    for page_num in range(int(page_start), int(page_end) + 1):
        find_preview(URL, page_num, KEYWORDS, HEADERS)