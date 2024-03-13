

# Дана база данных произведений Шекспира, в которой содержатся следующие таблицы: character - герои произведений, work - произведения, chapter главы произведений,

 

# paragraph - параграфы, wordform слова, встречающиеся в произведениях

 

# Напишите следующие запросы:

 

# 1. Найдите 10 самых часто встречающихся слов.
# SELECT wordform, COUNT(*) AS word_count
# FROM wordform
# GROUP BY wordform
# ORDER BY word_count DESC
# LIMIT 10;

 

# 2. Найдите все слова, которые начинаются с буквы 'а', регистр не должен иметь значения.

# SELECT wordform
# FROM wordform
# WHERE LOWER(SUBSTR(wordform, 1, 1)) = 'a';


# 3. Найдите все произведения, которые относятся к жанру 'p'.
# SELECT *
# FROM work
# WHERE genre = 'p'; 

# 4. Найдите среднее количество параграфов в произведения жанра 'т'.
# SELECT AVG(paragraph_count) AS average_paragraph_count
# FROM (
#     SELECT w.title, COUNT(p.id) AS paragraph_count
#     FROM work w
#     JOIN chapter c ON w.id = c.work_id
#     JOIN paragraph p ON c.id = p.chapter_id
#     WHERE w.genre = 'т'
#     GROUP BY w.title
# ) AS subquery;

 

# 5. Выведите все произведения, в которых количество слов выше среднего.
# SELECT *
# FROM work
# WHERE word_count > (
#     SELECT AVG(word_count) AS average_word_count
#     FROM (
#         SELECT w.id, COUNT(wf.id) AS word_count
#         FROM work w
#         JOIN chapter c ON w.id = c.work_id
#         JOIN paragraph p ON c.id = p.chapter_id
#         JOIN wordform wf ON p.id = wf.paragraph_id
#         GROUP BY w.id
#     ) AS subquery
# );

 

# 6. Выведите имя героя, количество его реплик, и произведение, в котором этот герой встречается.
# SELECT c.name AS character_name, COUNT(*) AS dialogue_count, w.title AS work_title
# FROM character c
# JOIN paragraph p ON c.id = p.character_id
# JOIN chapter ch ON p.chapter_id = ch.id
# JOIN work w ON ch.work_id = w.id
# GROUP BY c.name, w.title;

 

# 7. Выведите среднее количество реплик героев в произведении 'Romeo and Juliet'.
# SELECT AVG(dialogue_count) AS average_dialogue_count
# FROM (
#     SELECT COUNT(*) AS dialogue_count
#     FROM character c
#     JOIN paragraph p ON c.id = p.character_id
#     JOIN chapter ch ON p.chapter_id = ch.id
#     JOIN work w ON ch.work_id = w.id
#     WHERE w.title = 'Romeo and Juliet'
#     GROUP BY c.id
# ) AS subquery;


# 8. Выведите общее количество слов в каждой из секций в таблице paragraph.
# SELECT p.section, COUNT(wf.id) AS word_count
# FROM paragraph p
# JOIN wordform wf ON p.id = wf.paragraph_id
# GROUP BY p.section;


# 9. Выведите всех героев, которые имеют от 15 до 30 реплик.
# SELECT c.name AS character_name, COUNT(*) AS dialogue_count
# FROM character c
# JOIN paragraph p ON c.id = p.character_id
# GROUP BY c.name
# HAVING COUNT(*) BETWEEN 15 AND 30;

 

# 10. Выведите все произведения, которые были написаны в 17 веке
# SELECT *
# FROM work
# WHERE year_written BETWEEN 1600 AND 1700;

 

# 11. Найдите все произведения, которые имею в полном названии слово 'the'

# SELECT *
# FROM work
# WHERE title LIKE '%the%';


# 12. Выведите все уникальные секции в paragraph.
# SELECT DISTINCT section
# FROM paragraph;

 

# 13. Для каждой главы выведите: id, описание и название произведения, к которой относится данная глава.
# SELECT ch.id AS chapter_id, ch.description, w.title AS work_title
# FROM chapter ch
# JOIN work w ON ch.work_id = w.id;

 

# 14. Для каждого параграфа выведите: номер параграфа, имя героя, и количество реплик героя
# SELECT p.id AS paragraph_id, c.name AS character_name, COUNT(*) AS dialogue_count
# FROM paragraph p
# JOIN character c ON p.character_id = c.id
# GROUP BY p.id, c.name;

 

# 15. Для каждого параграфа выведите: номер параграфа, название произведения и год выхода этого произведения.
# SELECT p.id AS paragraph_id, w.title AS work_title, w.year_published
# FROM paragraph p
# JOIN chapter ch ON p.chapter_id = ch.id
# JOIN work w ON ch.work_id = w.id;
