import sqlite3

conn = sqlite3.connect('new_db.db')

cursor = conn.cursor()

cursor.execute("""CREATE TABLE COMPETITION (COMPETITION_ID INT, COMPETITION_NAME CHAR(30),WORLD_RECORD CHAR(30),
               #SET_DATE VARCHAR(20))""")
cursor.execute("""CREATE TABLE RESULT (COMPETITION_ID INT, SPORTSMAN_ID INT, RESULT VARCHAR(20),CITY VARCHAR(20),
              # HOLD_DATE CHAR(20))""")
cursor.execute("""CREATE TABLE SPORTSMAN (SPORTSMAN_ID INT, SPORTSMAN_NAME CHAR(30), RANK VARCHAR(10),
               #YEAR_OF_BIRTH CHAR(20),
               #PERSONAL_RECORD VARCHAR(30),
               #COUNTRY CHAR(20))""")
conn.commit()

cursor.execute("""INSERT INTO COMPETITION VALUES
               (1,'Соревнование1', 'Саня', '12.02.2020'),
               (2,'Чемпионат России по бегу', 'Вася Пупкин', '31.10.2019'),
               (3,'Чемпионат мира по стрельбе', 'Валерий Cтрелецкий', '20.05.2010'),
               (4,'Кубок России', 'Сергей Сергеев', '13.05.2010'),
               (5, 'Гонки', 'Петр Петров', '14.05.2010')
               """)
cursor.execute("""INSERT INTO RESULT VALUES
               (1,15, '10 секунд', 'г.Москва', '12.02.2020'),
               (2,24, '10 секунд', 'г.Сочи', '31.10.2019'),
               (3,35, '3-е место', 'г.Самара', '20.05.2010'),
               (4,12, '2-ое место', 'г.Санкт-Петербург', '13.05.2010'),
               (5,7, '56 секунд', 'г.Сочи', '14.05.2010')
                """)
cursor.execute("""INSERT INTO SPORTSMAN VALUES
               (15, 'Саня', '2', '1991', '20 секунд', 'Россия'),
               (24, 'Вася Пупкин', '3', '1990', '3 часа', 'Россия'),
               (35, 'Валерий Cтрелецкий', '3', '1990', '30 секунд', 'Россия'),
               (12, 'Сергей Сергеев', '2', '1993', '40 секунд', 'Россия'),
               (7, 'Петр Петров', '1', '1992', '35 секунд', 'Россия')
               """)
conn.commit()

cursor.execute("SELECT * FROM COMPETITION")
competition_select_results = cursor.fetchall()
print(competition_select_results)

cursor.execute("SELECT * FROM SPORTSMAN")
sportsman_select_results = cursor.fetchall()
print(sportsman_select_results)

cursor.execute("SELECT COMPETITION_NAME, WORLD_RECORD FROM COMPETITION")
records_select_results = cursor.fetchall()
print(records_select_results)

cursor.execute("SELECT SPORTSMAN_NAME FROM SPORTSMAN WHERE YEAR_OF_BIRTH = '1990'")
sportsman_name_select_results = cursor.fetchall()
print(sportsman_name_select_results)

cursor.execute("""SELECT COMPETITION_NAME, WORLD_RECORD FROM COMPETITION 
               WHERE SET_DATE BETWEEN '12.05.2010' AND '15.05.2010'""")
records_select_results_between_dates = cursor.fetchall()
print(records_select_results_between_dates)

cursor.execute("""SELECT HOLD_DATE FROM RESULT 
               WHERE CITY = 'г.Москва' AND RESULT = '10 секунд'""")
date_select_results = cursor.fetchall()
print(date_select_results)

cursor.execute("""SELECT SPORTSMAN_NAME FROM SPORTSMAN
               WHERE PERSONAL_RECORD < '25 секунд'""")
personal_record_select_result = cursor.fetchall()
print(personal_record_select_result)

conn.close()
