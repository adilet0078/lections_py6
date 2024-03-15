from models import Product, Category

def get_all_categories():
    return Category.select(Category.id, Category.title)

def get_all_products():
    return Product.select()

categories = get_all_categories()
# print(categories)
print("All categories on database:")
for category in categories:
    print(f"id: {category.id}, title: {category.title}")
    print(category.title) #id

print()
products = get_all_products()
print("All products on database:")
for x in products:
    print(f"ID: {x.id}, Title: {x.title}, Price: {x.price}, Category: {x.category_id.title}")
