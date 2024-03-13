# JSON - JavaScript Object Notation 
# Единый текстовый формат данных, был создан для хранение и перердачи данных между сервисами, проектами 
# <filename>.json # файл в формате JSON
# {
#     "id" : 1,
#     "name" : "John",
#     "age" : 30
# } -----# это JSON объект

# Процессы JSON
# 1. Сериализация данных в JSON
# 2. Десериализация данных из JSON(конвертация)

# Сериализация данных в JSON -Это перевод из Python в JSON формат
# Десериализация данных из JSON - Это перевод из JSON в Python формат

# dump -  записывает  данные в файл  формате JSON
# dumps - записывает данные  в текст формате JSON  

# Десериализация (чтение данных из JSON) - это процесс перевода данных из JSON в Python dict

# load - функция которая загружает данные из файла в формате JSON
# loads -  функция которая загружает данные из текстового файла в формате JSON

# --------------------------------------------------------------------------------------
# процесс сериализации

# import json

# data = {
#     "name": "John",
#     "age": 30,
#     "city": "New York",
#     "hasChildren": None,
#     "wife": False,
#     "status": True
# }

# # print(data, type(data))
# json_text = json.dumps(data)
# print()
# print(json_text, type(json_text))

# import json

# data = {
#     "name": "John",
#     "age": 30,
#     "city": "New York",
#     "hasChildren": None,
#     "wife": False,
#     "status": True
# }

# print(data, type(data))
# with open("data.json", "w") as file:
#     json.dump(data, file, indent= 4)


# --------------------------------------------------------------------------------------
# процесс десериализации

# import json

# with open("data.json", "r") as file:
#     json_data = file.read()

# print(json_data, type(json_data))

# data = json.loads(json_data)
# print(data, type(data))

# import json

# with open("data.json", "r") as file:
#     dict = json.load(file)

# print(dict, type(dict))

