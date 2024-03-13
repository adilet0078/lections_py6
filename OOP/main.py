from views import CreateMixin, ReadMixin, UpdateMixin, DeleteMixin

class SmartPhones(CreateMixin, ReadMixin, UpdateMixin, DeleteMixin):
    pass

smartphones = SmartPhones()
smartphones # Initialize objects list and id attribute

print(smartphones.post(title='Redmi Note 10', description='The best phone for own price', qty=10, price=250))
print(smartphones.post(title='Redmi Note 11 Pro', description='The best phone for own price', qty=10, price=300))
print(smartphones.post(title='Redmi Note 12', description='The best phone for own price', qty=10, price=350))
print(smartphones.post(title='Redmi Note 13', description='The best phone for own price', qty=10, price=400))
print(smartphones.post(title='Redmi Note 14', description='The best phone for own price', qty=10, price=450))
print()

print(smartphones.list())
print()

print(smartphones.detail(1))
print(smartphones.detail(2))
print(smartphones.detail(3))
print(smartphones.detail(4))
print(smartphones.detail(5))
print()
print(smartphones.path(1, title = 'Redmi Note 30'))
print()
print(smartphones.detail(1))
print(smartphones.delete(12))
print(smartphones.delete(1))
print()
print()
print(smartphones.list())
































