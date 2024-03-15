# import peewee
# from models import Category, Product
# import random

# def add_category(name):
#     try:
#         obj = Category(title=name.lower().strip())
#         obj.save()
#         print(f"Категория {name} добавлена.")
#     except( peewee.IntegrityError, peewee.IntegrityError):
#         print(f"Категория {name.lower().strip()} уже существует.")
# # add_category("laptops")
# # add_category("    pc   ")
# # add_category("Sony Playstation")
# # add_category("Tablets")
# # add_category("earphones")
# # add_category("smartphones")
# def add_product(name, price, cotegory_name ):
#     category_name = cotegory_name.lower().strip()
#     try:
#         category = Category.get(title=category_name)
#         print(category, category.title, category.created_at,' !!!!!')
#     except peewee.DoesNotExist:
#         print(f'Категория {category_name} не существует.')
#     else:
#         obj = Product(title=name.lower().strip(), price=price, category_id=category.id)
#         obj.save()
#         print(f"Товар {name} добавлен.")

# # add_product("Sony Playstation 5", 1000, "laptops")
# add_product("Xiaomi Redmi Note 10", 300, "smartphones")
# add_product("Samsung Galaxy S21", 500, "smartphones")
# add_product("Apple MacBook Air", 1000, "laptops")
# add_product("Samsung Galaxy S21", 500, "smartphones")
# add_product("Apple MacBook Air", 1000, "laptops")
