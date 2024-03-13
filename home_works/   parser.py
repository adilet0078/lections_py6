                    
# # import requests
# # from bs4 import BeautifulSoup
# # import csv
# # def refinde(s):
# #     str = s.split()[0]
# #     return str.replace(',','')

# # def write_csv(data):
# #     with open('pagination1.csv', 'a') as f:
# #         recorder = csv.writer(f)

# #         recorder.writerow((data['h3'],
# #                            data['a'],
# #                            data['rating']
# #                            ))

# # def get_data(html):
# #     soup = BeautifulSoup(html, 'lxml')
# #     articles = soup.find('main', class_='site-main').find_all('article')
# #     for article in articles:
# #         h3 = article.find('h3').get_text()
# #         a = article.find('h3').find('a').get('href')
# #         rating = article.find('span', class_='rating-count').find('a').get_text()

# #         data = {'h3':h3,
# #               'a':a,
# #               'rating':rating}
# #         write_csv(data)
# #         print (h3,a,refinde(rating))

# # def get_html(url):
# #     r = requests.get(url)
# #     return r.text

# # def main():
# #     for i in range(1,26):
# #         url = f'https://wordpress.org/plugins/browse/blocks/page/{i}'
# #         print (get_data(get_html(url)))

# # if __name__=='__main__':
# #     main()



# import re
# import os.path
# import time
# import random
# from bs4 import BeautifulSoup

# from seleniumwire import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# import lib.config
# import headers
# from lib.csv_handler import CsvHandler

# # Напишем код для случайной выборки прокси и юзер-агента:

# def get_headers_proxy() -> dict:
#     '''
#     The config file must have dict:
#         {
#             'http_proxy':'http://user:password@ip:port',
#             'user-agent': 'user_agent name'
#         }
#     '''

#     try:
#         users = lib.config.USER_AGENTS_PROXY_LIST
#         persona = random.choice(users)
#     except ImportError:
#         persona = None
#     return persona

# # Загрузим html-код страницы, используя библиотеку Selenium

# def get_html(persona, url):
#     options = webdriver.ChromeOptions()
#     options.add_argument(f"user-agent={persona['user-agent']}")
#     options.add_argument("--disable-blink-features=AutomationControlled")

#     options_proxy = {
#         'proxy': {
#             'https': persona['http_proxy'],
#             'no_proxy': 'localhost,127.0.0.1:8080'
#         }
#     }

#     s = Service(executable_path="/lib/chromedriver")

#     driver = webdriver.Chrome(options=options, service=s, seleniumwire_options=options_proxy)

#     try:
#         driver.request_interceptor = headers.interceptor
#         driver.get(url)
#         wait = WebDriverWait(driver, 10)
#         wait.until(EC.presence_of_element_located((By.CLASS_NAME, "collapsible__toggle-wrap")))

#         driver.find_element(By.XPATH, "//*[contains(text(), 'Развернуть характеристики')]").click()
#         wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Свернуть характеристики')]")))
#         html = driver.page_source
#     except Exception as ex:
#         print(ex)
#         html = None
#     finally:
#         driver.close()
#         driver.quit()
#     return html

# # Из полученного html извлечем требуемые данные, а результат запишем в csv-файл:

# def parse_data(html):
#     soup = BeautifulSoup(html, 'html.parser')
#     h1 = get_h1(soup)
#     sku = get_sku(soup)
#     stars = get_stars(soup)
#     price = get_price(soup)
#     original_price = get_original_price(soup)
#     description = get_description(soup)
#     brand = get_brand(soup)

#     tables = get_tables_specifications(soup)
#     specifications = prepare_specifications(tables) if tables else None

#     payload = {
#         'h1': h1,
#         'sku': sku,
#         'price': re.findall(r'[0-9]+', re.sub(r'\xa0', '', price))[0] if price else None,
#         'original_price': re.findall(r'[0-9]+', re.sub(u'\xa0', '', original_price))[0] if original_price else None,
#         'description': description,
#         'stars': stars,
#         'brand': brand,
#         'specifications': specifications,
#     }

#     write_to_csv(payload)

# def write_to_csv(data):
#     filename = 'wildberries_data.csv'
#     if os.path.isfile(filename):
#         CsvHandler(filename).write_to_csv_semicolon(data)
#     else:
#         CsvHandler(filename).create_headers_csv_semicolon(data)
#         CsvHandler(filename).write_to_csv_semicolon(data)

# # Реализуем функции извлечения данных из кода:

# # Декоратор для перехвата ошибок 
# def try_except(func):
#     def wrapper(*args, **kwargs):
#         try:
#             data = func(*args, **kwargs)
#         except:
#             data = None
#         return data
#     return wrapper

# @try_except
# def get_h1(soup):
#     return soup.h1.string

# @try_except
# def get_sku(soup):
#     return soup.find('span', attrs={'id': 'productNmId'}).get_text()

# @try_except
# def get_stars(soup):
#     return soup.find('div', attrs={'class': 'product-page__common-info'}).find('span', attrs={'data-link': 'text{: product^star}'}).get_text()

# @try_except
# def get_price(soup):
#     return soup.find('ins', attrs={'class': 'price-block__final-price'}).get_text()

# @try_except
# def get_original_price(soup):
#     return soup.find('del', attrs={'class': 'price-block__old-price j-final-saving j-wba-card-item-show'}).get_text()

# @try_except
# def get_description(soup):
#     return soup.find('p', attrs={'class': 'collapsable__text'}).get_text()

# @try_except
# def get_brand(soup):
#     return soup.find('div', attrs={'class': 'product-page__brand-logo hide-mobile'}).find('a').get('title')

# @try_except
# def get_tables_specifications(soup):
#     return soup.find('div', attrs={'class': 'collapsable__content j-add-info-section'}).find_all('table')

# def prepare_specifications(tables):
#     data_spec_all = {}
#     data_spec = []
#     for table in tables:
#         caption = table.find('caption').get_text()
#         for tr in table.find_all('tr'):
#             char = tr.find('th').get_text()
#             value = tr.find('td').get_text()
#             data_spec.append([char.strip(), value.strip()])
#         data_spec_all[caption] = data_spec

#     return data_spec_all

# # Напишем основную функцию запуска:

# def main():
#     url = 'https://www.wildberries.ru/catalog/13615125/detail.aspx'

#     persona = get_headers_proxy()
#     html = get_html(persona, url)
#     if html: parse_data(html)



# if __name__ == '__main__':
#     main()




                