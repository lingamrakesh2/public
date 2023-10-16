import sqlite3 as sq
import os

path = 'C:\\Users\\lingamr\\Desktop\\new_f'
database_name  = 'My_Private.DB'

db_path =  os.path.join(path,database_name)
# print(db_path)
if os.path.exists(db_path):
    os.remove(db_path)
connection = sq.connect(db_path)

cursor = connection.cursor()


cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS my_own_data (
        name TEXT,
        city TEXT,
        Age INTEGER )
''')

cursor.execute('INSERT INTO my_own_data (name, city, Age) VALUES ("rakesh_lingam", "Kurnool", 24), ("Lingam_Rakesh", "Nandyal", 24)')

connection.commit()

cursor.execute('SELECT name,city,Age From my_own_data')


data_lines = cursor.fetchall()

new_list = []
for i in data_lines:
    new_list.append(i)
    
print('My dataBase:')
print(new_list)


