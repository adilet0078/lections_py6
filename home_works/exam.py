# Hackathon: Parsing
# 100 баллов
# Проекты на выбор по уровням сложности.
# Сложность: Легкая - 80 б.
# Сложность: Средняя - 90 б.
# Сложность: Сложная -100 б.
# ТЕХНИЧЕСКОЕ ЗАДАНИЕ(сложность: легкая)
# Вы должны спарсить сайт
# https://www.kivano.kg/mobilnye-telefony. Как результат вы должны
# получить:
# 1. Наименование всех телефонов
# 2. Цену каждого продукта(в KGS)
# 3. И ссылка к фотографии
# 4. Все это записать в CSV файл
# Дополнительно(по желанию):
# 1. Ваш парсинг скрипт должен выполняться каждые 60 минут
# import requests
# import requests
# from bs4 import BeautifulSoup
# import csv
# import time

# def scrape_kivano():
#     kivano_url = 'https://www.kivano.kg/mobilnye-telefony'
#     html = requests.get(kivano_url)
#     soup = BeautifulSoup(html.text, 'lxml')
#     container = soup.find('div', class_='product-index product-index oh')
#     mobiles = container.find_all('div', class_="item product_listbox oh")

#     result = []
#     for mobile in mobiles:
#         name = mobile.find('div', class_="listbox_title").text.strip()
#         price = mobile.find('div', class_="listbox_price text-center").text.strip()
#         image = "https://www.kivano.kg" + mobile.find('img').get("src")
#         data = {'name': name, 'price': price, 'image': image}
#         result.append(data)

#     return result

# def write_to_csv(data):
#     with open('mobiles.csv', 'w', newline='', encoding='utf-8') as file:
#         fieldnames = ['name', 'price', 'image']
#         writer = csv.DictWriter(file, fieldnames=fieldnames)
#         writer.writeheader()
#         for idx, mobile in enumerate(data, start=1):
#             writer.writerow({
#                 'name': mobile['name'],
#                 'price': mobile['price'],
#                 'image': mobile['image']
#             })

# # Scrape the website and write the data to CSV
# mobile_data = scrape_kivano()
# write_to_csv(mobile_data)

# Optional: Schedule the script to run every 60 minutes
# while True:
#     mobile_data = scrape_kivano()
#     write_to_csv(mobile_data)
#     time.sleep(3600)  # 3600 seconds = 60 minutes




# ТЕХНИЧЕСКОЕ ЗАДАНИЕ(сложность: средняя)
# ● Спарсить kolesa.kz, категорию:
# 1.Название всех моделей.
# 2.Цену всех моделей
# 3.Изображение всех моделей
# 4.Краткое описание всех моделей
# 5.Записать все в csv файл

# from bs4 import BeautifulSoup
# import requests
# import csv
# import lxml


# url = 'https://auto312.kg'

# html_content = requests.get(url)
# soup = BeautifulSoup(html_content.text, 'lxml')
# container = soup.find('div', class_='dj-items-rows')
# cars = container.find_all('div', class_='item_row_in')
# result = []

# for car in cars:
#     name = car.find('div', class_='item_title').text.strip()
#     price = car.find('div', class_='item_price').text.strip()
#     image = car.find('img', class_='').get('src')
#     desc = car.find('div', class_='item_content_in').text.strip()
#     data = {'title': name, 'desc': desc, 'img': image, 'price': price}
#     result.append(data)
#     # print(result)

# def prepare_csv():
#     with open('cars.csv', 'w') as file:
#         fieldnames = [ '№', 'title', 'desc', 'img', 'price']
#         writer = csv.DictWriter(file, fieldnames)
#         writer.writerow( {
#             '№': '№',
#             'title': 'title',
#             'desc': 'desc',
#             'img': 'img',
#             'price': 'price'
#         })

# def write_csv(data, count):
#     with open('cars.csv', 'a') as file:
#         fieldnames = [ '№', 'title', 'desc', 'img', 'price']
#         writer = csv.DictWriter(file, fieldnames)
#         for car in data:
#             writer.writerow({
#                 '№': count,
#                 'title': car['title'],
#                 'desc': car['desc'],
#                 'img': car['img'],
#                 'price': car['price']
#             })        
#             count += 1

#         return count

# count = 1
# prepare_csv()
# data = result
# count = write_csv(data, count)
# print('Спарсили', count, 'машин')



# ТЕХНИЧЕСКОЕ ЗАДАНИЕ(сложность: тяжелая)
# 1. При нажатии на кнопку start, телеграмм бот должен
# зайти на сайт KaktusMedia (https://kaktus.media/) и
# спарсить категорию “Все новости”
# 2. При вводе текста должны выйти первые 20
# заголовков статей с нумерацией. Должна быть
# возможность выбрать новости по нумерации или id
# (по желанию)
# 3. После выбора новости по нумерации, телеграмм
# бот должен отправить сообщение в виде “some
# title news you can see Description of this news
# and Photo” и пользователь отправит текст (либо
# нажмет кнопку) Description, то бот должен
# отправить описание именно текущего поста, также
# аналогично с Photo.
# 4. При нажатии на кнопку «Quit» бот должен
# отправить сообщение “До свидания“
# Рекомендации:
# 1. BeautifulSoup
# 2. CSV
# 3. lxml
# 3. Requests



# import telebot
# import requests
# from bs4 import BeautifulSoup
# from selenium import webdriver
# from telegram.ext import Updater, CommandHandler, MessageHandler, filters
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time


# TELEGRAM_BOT_TOKEN = 't.me/parser_kaktus_kg_bot.'

# def start(update, context):
#     html = requests.get("https://kaktus.media/")
#     soup = BeautifulSoup(html.content, "html.parser")
#     container = soup.find('div', class_='Tag--articles')
#     news = container.find_all('div', class_='Tag--article')
#     result = []
#     count = 0
#     for i in news:
#         count += 1
#         name = i.find('a', class_='ArticleItem--name').text.strip()
#         img = i.find('img').get('src')
#         link = i.find('a').get('href')
#         desc = parsing_desc(link)
#         data = {'count': count, 'name': name, 'img': img, 'link': link, 'desc': desc}
#         result.append(data)
#         if count == 20:
#             break

#     messages = [f"{item['count']}. {item['name']} - {item['link']}" for item in result]
#     message = "\n".join(messages)

#     context.bot.send_message(chat_id=update.effective_chat.id, text=message)


# def news(update, context):
#     news_id = int(context.args[0])  # Getting the news id from the user's message
#     html = requests.get("https://kaktus.media/")
#     soup = BeautifulSoup(html.content, "html.parser")
#     container = soup.find('div', class_='Tag--articles')
#     news = container.find_all('div', class_='Tag--article')
#     selected_news = news[news_id - 1]  # Adjusting index to match user input

#     name = selected_news.find('a', class_='ArticleItem--name').text.strip()
#     link = selected_news.find('a').get('href')
#     desc = parsing_desc(link)

#     message = f"{name}\n\n{desc}"

#     context.bot.send_message(chat_id=update.effective_chat.id, text=message)


# def parsing_desc(url):
#     html = requests.get(url)
#     soup = BeautifulSoup(html.content, 'html.parser')
#     desc = soup.find('div', class_='BbCode').find_all('p')
#     desc_text = []
#     for i in desc:
#         desc_text.append(i.text)
#     return '\n'.join(desc_text)


# def quit(update, context):
#     context.bot.send_message(chat_id=update.effective_chat.id, text="До свидания!")


# def main():
#     updater = Updater(TELEGRAM_BOT_TOKEN, use_context=True)
#     dp = updater.dispatcher

#     dp.add_handler(CommandHandler("start", start))
#     dp.add_handler(CommandHandler("news", news))
#     dp.add_handler(CommandHandler("quit", quit))

#     updater.start_polling()
#     updater.idle()


# if __name__ == '__main__':
#     main()


# # @parser_kaktus_kg_bot (https://t.me/parser_kaktus_kg_bot)
# import time
# import httpx
# from lxml import html
# from telegram import Update
# from telegram.ext import Updater, CommandHandler, CallbackContext

# updater = Updater("t.me/parser_kaktus_kg_bot.", use_context=True)
# def start(update: Update, context: CallbackContext) -> None:
#     with httpx.Client() as client:
#         response = client.get("https://kaktus.media/")
#         soup = html.fromstring(response.content)
#         container = soup.xpath('//div[@class="Tag--articles"]')[0]
#         news = container.xpath('//div[@class="Tag--article"]')[:20]
#         result = []
#         for count, item in enumerate(news, start=1):
#             name = item.xpath('.//a[@class="ArticleItem--name"]/text()')[0].strip()
#             img = item.xpath('.//img/@src')[0]
#             link = item.xpath('.//a/@href')[0]
#             desc = parsing_desc(link)
#             data = {'count': count, 'name': name, 'img': img, 'link': link, 'desc': desc}
#             result.append(data)

#         messages = [f"{item['count']}. {item['name']} - {item['link']}" for item in result]
#         message = "\n".join(messages)
#         context.bot.send_message(chat_id=update.effective_chat.id, text=message)

# def news(update: Update, context: CallbackContext) -> None:
#     news_id = int(context.args[0])
#     with httpx.Client() as client:
#         response = client.get("https://kaktus.media/")
#         soup = html.fromstring(response.content)
#         container = soup.xpath('//div[@class="Tag--articles"]')[0]
#         news = container.xpath('//div[@class="Tag--article"]')
#         selected_news = news[news_id - 1]

#         name = selected_news.xpath('.//a[@class="ArticleItem--name"]/text()')[0].strip()
#         link = selected_news.xpath('.//a/@href')[0]
#         desc = parsing_desc(link)

#         message = f"{name}\n\n{desc}"
#         context.bot.send_message(chat_id=update.effective_chat.id, text=message)

# def parsing_desc(url):
#     with httpx.Client() as client:
#         response = client.get(url)
#         soup = html.fromstring(response.content)
#         desc = soup.xpath('//div[@class="BbCode"]/p/text()')
#         return '\n'.join(desc)

# def quit(update: Update, context: CallbackContext) -> None:
#     context.bot.send_message(chat_id=update.effective_chat.id, text="До свидания!")

# def main() -> None:
#     updater = Updater(token=TELEGRAM_BOT_TOKEN, use_context=True)
#     dp = updater.dispatcher
#     dp.add_handler(CommandHandler("start", start))
#     dp.add_handler(CommandHandler("news", news))
#     dp.add_handler(CommandHandler("quit", quit))
#     updater.start_polling()
#     updater.idle()

# if __name__ == '__main__':
#     main()
# #-----------------------------------------------------------------------------
# import httpx
# from lxml import html
# from telegram import Update
# from telegram.ext import Updater, CommandHandler, CallbackContext

# TELEGRAM_BOT_TOKEN = 't.me/parser_kaktus_kg_bot.'

# def start(update: Update, context: CallbackContext) -> None:
#     with httpx.Client() as client:
#         response = client.get("https://kaktus.media/")
#         soup = html.fromstring(response.content)
#         container = soup.xpath('//div[@class="Tag--articles"]')[0]
#         news = container.xpath('//div[@class="Tag--article"]')[:20]
#         result = []
#         for count, item in enumerate(news, start=1):
#             name = item.xpath('.//a[@class="ArticleItem--name"]/text()')[0].strip()
#             img = item.xpath('.//img/@src')[0]
#             link = item.xpath('.//a/@href')[0]
#             desc = parsing_desc(link)
#             data = {'count': count, 'name': name, 'img': img, 'link': link, 'desc': desc}
#             result.append(data)

#         messages = [f"{item['count']}. {item['name']} - {item['link']}" for item in result]
#         message = "\n".join(messages)
#         context.bot.send_message(chat_id=update.effective_chat.id, text=message)

# def news(update: Update, context: CallbackContext) -> None:
#     news_id = int(context.args[0])
#     with httpx.Client() as client:
#         response = client.get("https://kaktus.media/")
#         soup = html.fromstring(response.content)
#         container = soup.xpath('//div[@class="Tag--articles"]')[0]
#         news = container.xpath('//div[@class="Tag--article"]')
#         selected_news = news[news_id - 1]

#         name = selected_news.xpath('.//a[@class="ArticleItem--name"]/text()')[0].strip()
#         link = selected_news.xpath('.//a/@href')[0]
#         desc = parsing_desc(link)

#         message = f"{name}\n\n{desc}"
#         context.bot.send_message(chat_id=update.effective_chat.id, text=message)

# def parsing_desc(url):
#     with httpx.Client() as client:
#         response = client.get(url)
#         soup = html.fromstring(response.content)
#         desc = soup.xpath('//div[@class="BbCode"]/p/text()')
#         return '\n'.join(desc)

# def quit(update: Update, context: CallbackContext) -> None:
#     context.bot.send_message(chat_id=update.effective_chat.id, text="До свидания!")

# def main() -> None:
#     updater = Updater(TOKEN=TELEGRAM_BOT_TOKEN, use_context=True)
#     dp = updater.dispatcher
#     dp.add_handler(CommandHandler("start", start))
#     dp.add_handler(CommandHandler("news", news))
#     dp.add_handler(CommandHandler("quit", quit))
#     updater.start_polling()
#     updater.idle()

# if __name__ == '__main__':
#     main()
