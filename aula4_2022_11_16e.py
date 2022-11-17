import aula4_2022_11_16c as bd

con, cur = bd.conectar()

nome = input('Informe o nome do herói/vilão: ')
nome_civil = input('Informe o nome civil do herói/vilão (sua identidade secreta): ')
tipo_numerico = input('Tecle 1 para Herói(na) ou 2 para Vilã(o): ')

sql = ("SELECT MAX(pessoa_id) + 1 FROM pessoas")
pessoa_id = cur.execute(sql).fetchone()[0]

tipo = 'Herói(na)'
if (tipo_numerico == '2'):
  tipo = 'Vilã(o)'

sql = "SELECT grupo_id, nome FROM grupos"

cur.execute(sql)

grupos = cur.fetchall()

print('Grupos:')
for grupo in grupos:
  print(f'[ {grupo[0]} ] - {grupo[1]}')

grupo_id = int(input('Sua opção: '))

sql = f"INSERT INTO pessoas (pessoa_id, nome, nome_civil, tipo) VALUES ({pessoa_id}, '{nome}', '{nome_civil}', '{tipo}')"

cur.execute(sql)

sql = f"INSERT INTO pessoas_grupos (pessoa_id, grupo_id) VALUES ({pessoa_id}, {grupo_id})"

con.commit()
con.close()
