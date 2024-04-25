import pymysql
import os

host = 'localhost'
user = 'root'
password = '123456'
db = 'db_name'

conn = pymysql.connect(host=host, user=user, password=password, db=db)
cursor = conn.cursor()

cursor.execute('show tables')
tables = cursor.fetchall()

dir_path = './output/compress_tables'
file_path = os.path.join(dir_path, f'{db}.sql')
os.makedirs(dir_path, exist_ok=True)
if os.path.exists(file_path):
    os.remove(file_path)    

with open(file_path, 'a') as f:
    for table in tables:
        row = f'alter table {db}.{table[0]} row_format=compressed;'
        print(row)
        f.write(row + '\n')

cursor.close()
conn.close()