import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

apaga_tabela = DROP TABLE database

cursor.execute(apaga_tabela)

connection.commit()
connection.close()