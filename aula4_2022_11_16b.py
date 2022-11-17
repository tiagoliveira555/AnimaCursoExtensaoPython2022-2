import sqlite3

con = sqlite3.connect('dc_universe.db')

cursor = con.cursor()

sql = "INSERT INTO pessoas (pessoa_id, nome, nome_civil, tipo) VALUES (12, 'The Flash', 'Barry Allen', 'Herói(na)')"

cursor.execute(sql)

con.commit()

sql = "SELECT * FROM pessoas"

pessoas = cursor.execute(sql)

for pessoa in pessoas:
  print(pessoa)
