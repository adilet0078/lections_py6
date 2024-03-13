
# from selenium.webdriver.firefox.service import Service
# from selenium.webdriver.common.by import By
# from webdriver_manager.firefox import GeckoDriverManager
# from selenium import webdriver
# import time
# import csv
# import requests
# import pprint
# from bs4 import BeautifulSoup

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

# # ... (existing code)

# # Define the base URL
# base_url = 'https://global.wildberries.ru/catalog?category=9492&page={}'

# # Set the initial page number
# page_number = 1

# # Loop through the pages
# while True:
#     url = base_url.format(page_number)
#     browser.get(url)
#     time.sleep(5)
    
#     # Your existing scraping logic here
    
#     # Check if there are more pages to scrape
#     next_button = browser.find_elements(By.CLASS_NAME, 'next')
#     if not next_button:
#         break  # Exit the loop if there are no more pages
    
#     # Increment the page number for the next iteration
#     page_number += 1

# # ... (rest of your code)

#     extract_data()