import sqlalchemy

engine = sqlalchemy.create_engine('postgresql://bd_hw4:pass@localhost:5432/bd_hw4')
connection = engine.connect()

# название и год выхода альбомов, вышедших в 2018 году;
case1 = connection.execute('''
    SELECT title, year
    FROM album
    WHERE year = 2018;
    ''').fetchall()
print(case1)

# название и продолжительность самого длительного трека;
case2 = connection.execute('''
    SELECT title, duration
    FROM track
    ORDER BY duration DESC
    LIMIT 1;
    ''').fetchall()
print(case2)

# название треков, продолжительность которых не менее 3,5 минуты;
case3 = connection.execute('''
    SELECT title
    FROM track
    WHERE duration >= 210;
    ''').fetchall()
print(case3)

# названия сборников, вышедших в период с 2018 по 2020 год включительно;
case4 = connection.execute('''
    SELECT title 
    FROM collection 
    WHERE 2018 <= year AND year <= 2020;
    ''').fetchall()
print(case4)

# исполнители, чье имя состоит из 1 слова;
case5 = connection.execute('''
    SELECT name
    FROM executor
    WHERE NOT name LIKE '%% %%';
    ''').fetchall()
print(case5)

# название треков, которые содержат слово "мой"/"my".
case6 = connection.execute('''
    SELECT title FROM track WHERE title iLIKE 'my %%'
    OR title iLIKE '%% my'
    OR title iLIKE '%% my %%'
    OR title iLIKE 'мой %%'
    OR title iLIKE '%% мой'
    OR title iLIKE '%% мой %%';
    ''').fetchall()
print(case6)