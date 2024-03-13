# from configparser import ParsingError
# from bs4 import BeautifulSoup
# import requests
# import csv
# import pprint



# def parsing_data(url):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     container = soup.find('div', class_='table-view-list')
#     cars = container.find_all('div', class_='list-item')
    
#     result = []
#     for car in cars:
#         name = car.find('h2', class_='name').text.strip()
#         try:
#             img = car.find('img', class_='lazy-image-attr').get('src')
#         except Exception as e:
#             img = f'No image', {e}
#         price = car.find('div', class_='block price').find('strong').text
#         # print(name, img, price)
#         desc = ''.join(car.find('div', class_='item-info-wrapper').text.split())
#         data = {'title': name, 'desc': desc, 'img': img, 'price': price}
#         result.append(data)

#     return result


# def get_last_page(url):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     pages = soup.find_all('a', class_='page-link') [-1]
#     return int(pages.get('data-page')) 




# def  prepare_csv():
#     with open('cars.csv', 'w') as file:
#         fieldnames = ['№' ,'name', 'desc', 'img', 'price']
#         writer = csv.DictWriter(file, fieldnames)
#         writer.writerow({ '№': 'No', 'name': 'name', 'desc': 'desc', 'img': 'img', 'price': 'price'})

# def write_csv(data):
#     with open('cars.csv', 'a') as file:
#         global count 
#         fieldnames = ['№' ,'name', 'desc', 'img', 'price']
#         writer = csv.DictWriter(file, fieldnames)
#         for car in data:
#             writer.writerow({ '№': count, 'name': car['title'], 'desc': car['desc'], 'img': car['img'], 'price': car['price']})
#             count += 1


# url = f'https://www.mashina.kg/search/all/?page=1'
# last_page = get_last_page(url)
# count = 1
# print(last_page)
# prepare_csv()
# data = parsing_data(url)
# write_csv(data)

# i = 1
# while i <= last_page:
#     page_url = f'https://www.mashina.kg/search/all/?page={i}'
#     data = parsing_data(page_url)
#     i += 1
#     write_csv(data)
#     print(f'спарсили {i}/{last_page} страницу')

# # # selenium-ParsingE   

# import requests
# from bs4 import BeautifulSoup
# from selenium import webdriver
# import csv
# import time

# from selenium.webdriver.chrome.service import Service

# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager

# service = Service(expected_conditions='/snap/bin/chromium')
# chrome_options = webdriver.ChromeOptions()
# # chrome_options.add_argument("--disable-javascript")

# def get_html_selenium(url):
#     driver = webdriver.Chrome(options=chrome_options, service=service)
#     driver.get(url)
#     time.sleep(5)
    
#     html = driver.page_source
#     driver.quit() 
#     return html



# def get_data(html):
#     soup = BeautifulSoup(html, 'lxml')
#     print(soup)
#     items = soup.find_all('div', class_='dtList i-dtList j-card-item')

#     data = []
#     for item in items:
#         name = item.find('div', class_='b-card__info-row').text
#         price = item.find('ins', class_='price__lower').text
#         image_link = item.find('img', class_="main-img").get_attribute('src')

#         data.append({'Name': name, 'Price': price, 'Image_Link': image_link})
    
#     return data

# def main():
#     url = 'https://global.wildberries.ru/catalog?category=9492'
#     html = get_html_selenium(url)
#     print(html)

#     if html:
#         data = get_data(html)

#         with open('wildberries_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
#             fieldnames = ['Name', 'Price', 'Image_Link']
#             writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#             writer.writeheader()
#             for item in data:
#                 writer.writerow(item)
#     else:
#         print("Failed to fetch HTML.")

# if __name__ == '__main__':
#     main()from selenium import webdriver

# from selenium.webdriver.firefox.service import Service
# from selenium.webdriver.common.by import By
# from webdriver_manager.firefox import GeckoDriverManager
# from selenium import webdriver
# import time
# import csv

# options = webdriver.FirefoxOptions()
# options.headless = True

# # Указываем путь к исполняемому файлу geckodriver версии 0.33.0
# geckodriver_path = '/snap/bin/geckodriver'

# # Создаем объект сервиса для Firefox WebDriver
# service = Service(executable_path=geckodriver_path)

# # Создаем экземпляр WebDriver для Firefox с использованием сервиса и опций
# browser = webdriver.Firefox(service=service, options=options)

# url = 'https://global.wildberries.ru/catalog?category=9492'
# browser.get(url)

# time.sleep(5)

# product_names = browser.find_elements(By.CLASS_NAME, 'card__link')

# result = []

# for product in product_names:
#     title = product.find_element(By.CLASS_NAME, 'b-card__info-row').text
#     print(title)
#     price = product.find_element(By.CLASS_NAME, 'price__lower').text
#     sales = product.find_element(By.CLASS_NAME, 'price__discount').text
#     img = product.find_element(By.CLASS_NAME, 'main-img').get_attribute('src')
#     data = {'title': title, 'price': price, 'sales': sales, 'img': img}
#     result.append(data)

# browser.quit()

# with open('wildberis.csv', 'w') as file:
#     fieldnames = ['№', 'title', 'sales', 'price', 'image']
#     writer = csv.DictWriter(file, fieldnames)
#     writer.writerow({'№': '№', 'title': 'title', 'sales': 'sales', 'price': 'price', 'image': 'img'})
# count = 1
# with open('wildberis.csv', 'a') as file:
#     fieldnames = ['№', 'title', 'sales', 'price', 'image']
#     writer = csv.DictWriter(file, fieldnames)
#     for nout in result:
#         writer.writerow({
#             '№': count,
#             'title': nout['title'],
#             'sales': nout['sales'],
#             'price': nout['price'],
#             'image': nout['img']
#         })
#         count += 1


