
# Задача 1: "Dollar"

#     Цель: Создать функцию dollarize, преобразующую числа в долларовый формат, и класс MoneyFmt для управления денежными суммами.
#     Описание:
#         Функция dollarize должна принимать дробное число и возвращать строку, представляющую сумму в долларовом формате.
#         Класс MoneyFmt использует внутренний атрибут amount для хранения денежной суммы и предоставляет методы для обновления суммы, возвращения ее как строки в долларовом формате и как исходного числового значения.
#         Пример использования:
#         # cash = MoneyFmt(12345678.021) 
#         # print(cash) -- выводит "$12,345,678.02" 
#         # cash.update(100000.4567) 
#         # print(cash) -- выводит "$100,000.46" 
#         # cash.update(-0.3) 
#         # print(cash) -- выводит "-$0.30" 
#         # repr(cash) -- выводит -0.3 

# class MoneyFmt:
#     def __init__(self, amount):
#         self.amount = amount
    
#     def update(self, new_amount):
#         self.amount = new_amount
    
#     def __repr__(self):
#         return str(self.amount)
    
#     def __str__(self):
#         return self.dollarize()

#     def dollarize(self):
#         if self.amount >= 0:
#             return '${:,.2f}'.format(self.amount)
#         else:
#             return '-${:,.2f}'.format(abs(self.amount))

# # Пример использования:
# cash = MoneyFmt(12345678.021) 
# print(cash) # Выводит "$12,345,678.02" 
# cash.update(100000.4567) 
# print(cash) # Выводит "$100,000.46" 
# cash.update(-0.3) 
# print(cash) # Выводит "-$0.30" 
# print(repr(cash)) # Выводит -0.3



# Задача 2: "Велосипед"

#     Цель: Реализовать класс Bike, моделирующий велосипед с различными атрибутами и методами управления.
#     Описание:
#         Класс должен содержать атрибуты для стоимости, производителя, модели, года выпуска, состояния, цены продажи и статуса продажи.
#         Методы должны позволять устанавливать цену продажи, учитывая минимальную прибыль, обслуживать велосипед, изменяя его состояние и стоимость ремонта, и продавать велосипед, изменяя его статус и рассчитывая прибыль.

# class Bike:
#     def __init__(self, manufacturer, model, year, condition, cost_price):
#         self.manufacturer = manufacturer
#         self.model = model
#         self.year = year
#         self.condition = condition
#         self.cost_price = cost_price
#         self.sale_price = None
#         self.status = "Available"
#         self.profit = 0

#     def set_sale_price(self, minimum_profit):
#         """
#         Устанавливает цену продажи с учетом минимальной прибыли.

#         Args:
#             minimum_profit (float): Минимальная желаемая прибыль.
#         """
#         self.sale_price = self.cost_price + minimum_profit

#     def maintain_bike(self, new_condition, repair_cost):
#         """
#         Обслуживает велосипед, изменяя его состояние и стоимость ремонта.

#         Args:
#             new_condition (str): Новое состояние велосипеда.
#             repair_cost (float): Стоимость ремонтных работ.
#         """
#         self.condition = new_condition
#         self.cost_price += repair_cost

#     def sell_bike(self, selling_price):
#         """
#         Продает велосипед, изменяя его статус и рассчитывая прибыль.

#         Args:
#             selling_price (float): Цена, по которой продается велосипед.
#         """
#         self.status = "Sold"
#         self.profit = selling_price - self.cost_price

# # Пример использования:
# bike = Bike("Trek", "FX 2", 2022, "Good", 500)
# print(f"Cost Price: ${bike.cost_price}")

# bike.set_sale_price(100)  # Минимальная прибыль $100
# print(f"Sale Price: ${bike.sale_price}")

# bike.maintain_bike("Excellent", 50)  # Улучшаем состояние и тратим $50 на ремонт
# print(f"Condition: {bike.condition}, Cost Price after Maintenance: ${bike.cost_price}")

# bike.sell_bike(750)  # Продаем велосипед за $750
# print(f"Status: {bike.status}, Profit: ${bike.profit}")



# Задача 3: "Герой"

#     Цель: Разработать программу, имитирующую взаимодействие между солдатами и героями в контексте игры-стратегии.
#     Описание:
#         Необходимо создать классы для солдат и героев, каждый с уникальным номером и принадлежностью к команде.
#         Солдаты могут "следовать" за героями своей команды, а герои могут повышать свой уровень.
#         В программе должны генерироваться солдаты для двух команд, после чего сравнивается количество солдат в каждой команде, и у героя команды с большим числом солдат повышается уровень.

# class Soldier:
#     def __init__(self, number, team):
#         self.number = number
#         self.team = team
#         self.hero = None
    
#     def follow_hero(self, hero):
#         """
#         Assigns the hero for the soldier to follow.

#         Args:
#             hero (Hero): The hero for the soldier to follow.
#         """
#         self.hero = hero
    
#     def __str__(self):
#         return f"Soldier {self.number} of Team {self.team}"


# class Hero:
#     def __init__(self, number, team):
#         self.number = number
#         self.team = team
#         self.level = 1
    
#     def level_up(self):
#         """Increases the level of the hero."""
#         self.level += 1
    
#     def __str__(self):
#         return f"Hero {self.number} of Team {self.team} (Level {self.level})"


# def generate_soldiers(team, num_soldiers):
#     """Generates soldiers for a given team."""
#     return [Soldier(i+1, team) for i in range(num_soldiers)]


# def compare_teams(team1, team2):
#     """Compares the number of soldiers in two teams and levels up the hero of the team with more soldiers."""
#     if len(team1) > len(team2):
#         team1_hero.level_up()
#         print(f"Team {team1_hero.team} Hero has leveled up!")
#     elif len(team1) < len(team2):
#         team2_hero.level_up()
#         print(f"Team {team2_hero.team} Hero has leveled up!")


# # Generate soldiers for two teams
# team1_soldiers = generate_soldiers(1, 5)
# team2_soldiers = generate_soldiers(2, 7)

# # Assign heroes for each team
# team1_hero = Hero(1, 1)
# team2_hero = Hero(2, 2)

# # Assign heroes for soldiers to follow
# for soldier in team1_soldiers:
#     soldier.follow_hero(team1_hero)

# for soldier in team2_soldiers:
#     soldier.follow_hero(team2_hero)

# # Compare the number of soldiers in each team and level up the hero accordingly
# compare_teams(team1_soldiers, team2_soldiers)

# # Output the state of soldiers and heroes after leveling up
# print("Team 1 Soldiers:")
# for soldier in team1_soldiers:
#     print(soldier)

# print("\nTeam 2 Soldiers:")
# for soldier in team2_soldiers:
#     print(soldier)

# print("\nTeam 1 Hero:")
# print(team1_hero)

# print("\nTeam 2 Hero:")
# print(team2_hero)
