# PostgreSQL - система управления базами данных(СУБД/DBMS)
# Это ряд програм и инструментов позваляющих создовать базу данных ,управлять ею и манипулировать данными внутри (CRUD)
# Postgres - сама база данных , она объектно реляционная, то есть данные хранятся в виде таблиц, и таблицы имеют связи между собой
# SQL (Structured Query language) - декларативный язык структириванных запросов ,он применяется для создание и получения данных при помощи запросов в база данных(БД)
# -----------------------------------------------------------
# команда для входа в БД через юзера postgres:
# sudo -u postgres psql

# команда для выхода в своего юзера  
# psql

# создание суперюзер
# CREAT ROLE "username" SUPERUSER LOGIN PASSWORD '1'

# изменение пароля  
# ALTER USER "username" with password "1"

# создание БД
#  CREAT DATABASE "name"
# \l список всез бд

# \du -все юзеры  

# \c "name" - команда для подключение к бд

#\dt - все таблицы (нужно подключиться к бд заранее)
 
# \d "name" - подробная информация про таблицу (нужно подключиться к бд заранее)
 
# psql -u "username" -d "dbname" -подключаемся под выбранным username к dbname

# ----------------------------------------------------------------------------
# Типы полей в Postgres 

# Numeric types (числовые типы )
# a. smallint (2 bytes) -> -32767 to 32767
# b. integer(4 bytes) -> -2.147... to 2.147
# c. bigint(8 bytes) -> ...

# d. real(4 bytes) -> число с плавающей точкой, вещественное
# f. serial(4 bytes) -> integer, auto-increment

# Character types(символьные типы(строковые)):
# a. varchar (кол-во символов) -> если мы укажем 50 символов, а заполним только 10, то остальные будут свободны. Макс 255

# b. char(кол-во символов) -> если укажем 50 символов,а заполним только 10, то остальные будут заполнены пробелом 

#  c. text()-> неограниченное кол-во символов 

# Boolen Type
    #  a. boolean(1 bytes) -> true/false

#  date -> календарная дата (год.месяц.день)

# location -> координатная точка (x, y) - (245, -12) 

# enumerate types:
# ("a", "b", "c")
#  CREATE TYPE "any name" AS ENUM ('Happy', 'Sad', "Mad");

# ------------------------------------------------------
# Команда для добавления данных в таблицу
# INSERT INTO <tablename> [(columns)] VALUES (data), (data);

# Команда для обновления данных
# UPDATE <table> SET <column> = <new_value> WHERE <column> = <value>;

# Команда для удаления данных
# DELETE FROM <table> WHERE <column> = <value>;


# команда для получение данных  
# SELECT (columns) * FROM "table";


# ORDER BY : Позваляет нам сортировать выводящие данные по убыванию или возрастанию. ASC(по возрастанию) DESC(по убыванию)
# Синтаксис:  SELECT <row>  FROM <tablename> ORDER BY <row> [ASC|DESC] 
# WHERE : Используется для фильтрации данных по полям. Будут выводится только те данные, которые соответствуют условию оператора WHERE.
# BETWEEN: Используется для фильтрации данных по диапазону.
# Синтаксис:  SELECT <row>  FROM <tablename> WHERE <row> = <value>(чему либо)

# AND  ОПРЕАТОР и , для фильтрации данных по нескольким условиям.
# IN: WHERE <row> IN (<value>, <value>, ...)
#  LIMIT : Ограничение количества выводимых строк.

# LIKE : Выводить данные, которые соответствуют шаблону. 
# Синтаксис:  SELECT <row>  FROM <tablename> WHERE <row> LIKE <value>
# ILIKE : Выводить данные, которые соответствуют шаблону. Чувственный регистр.
#  Синтаксис:  SELECT <row>  FROM <tablename> WHERE <row> ILIKE <value>

# GROUP BY : Группировка данных. Разделяет данные которые мы получаем в SELECT ,при этом группируя по определенному признаку. И теперь для каждой группы можно использовать функцию

# HAVING : Для фильтрации данных по группам. СТАВИТЬ WHEREЮ . ставит условия для фильтрации данных по группам.
# ----------в тандеме 
#  агпегатные функции: COUNT(), SUM(), AVG(), MIN(), MAX()
#  Экспрорт бд (дамп)
# pg_dump -U postgres -W -f "filename" "database_name"
# import database
# -u <psql username> -d <database name> -f "filename"

# 𐌋𐌀𐌂𐌊 𐌁ᚳ𐌠𐌂ᛊ / Jack Blice, [2024/3/11 11:32]
# Ограничения:
# 1) NOT NULL - обязательно к заполнению
# 2) UNIQUE - будут хранится только уникальные данные
# 3) CHECK -> CHECK age > -1 - ограничение проверки на условие
# 4) PRIMARY KEY(для установки идентификатора данных в таблице)
# 5) FOREIGN KEY(для установки связей между таблицами)
# 6) ON DELETE - для установки поведения при удалении данных которые были связаны
# --------------------------------------------------------------------------------------------------------------------------
# JOIN: выборка данных из двуъ таблиц, соединение таблиц

# LEFT JOIN: выборка будет содержать все строки из левой таблицы

# RIGHT JOIN: выборка будет содержать все строки из правой таблицы

# SELECT p1.title, p1.price, p1.quantity, p1.price * o1.quantity as total_sum FROM product p1, orders o1 WHERE p1.id = o1.product_id;
#  - Запрос сразу в две таблицы

# 𐌋𐌀𐌂𐌊 𐌁ᚳ𐌠𐌂ᛊ / Jack Blice, [2024/3/11 11:33]
# тут есть ошибки:
# SELECT p1.title, p1.price, p1.quantity, p1.price * o1.quantity as total_sum FROM product p1 JOIN orders o1 WHERE p1.id = o1.product_id;

# Экспорт бд(дамп):
# pg_dump -U <username> -d 'dbname' > 'file.sql'

# импорт:
# psql -U <username> -d 'dbname' -f <filename>


##---------------##---------------##---------------##---------------##---------------##---------------
                                    # Группировка

# SELECT count(product_name), c.category_name FROM products as p, categories as c WHERE p.category_id = c.category_id GROUP BY c.category_name;





# JOIN: выборка данных из двух таблицб соединение таблиц, соединение таблиц

# LEFT JOIN: выборка будет содержать все строки из левой таблицы

# RIGHT JOIN: выборка будет содержать все таблицы из правой таблицы

# SELECT p1.title, p1.price, o1.quality, p1.price * o1.quality as total_sum FROM product p1, orders o1 WHEREp1.id = o1.product_id; - Запрос сразу после в де таблицы

# SELECT p1.title, p1.price, o1.quality, p1.price * o1.quality as total_sum FROM product p1 JOIN orders ON p1.id = o1.product_id;
# ----------------------------------------------------------------------------------------------

