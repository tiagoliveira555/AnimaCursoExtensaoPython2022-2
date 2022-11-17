import aula4_2022_11_16c as bd

con, cur = bd.conectar()

nome = input('Informe o nome do herói/vilão: ')
nome_civil = input('Informe o nome civil do herói/vilão (sua identidade secreta): ')
tipo_numerico = input('Tecle 1 para Herói(na) ou 2 para 2 para Vilã(0): ')

sql = ("SELECT MAX(pessoa_id) + 1 FROM pessoas")
pessoa_id = cur.execute(sql).fetchone()[0]

tipo = 'Herói(na)'
if (tipo_numerico == '2'):
  tipo = 'Vilã(o)'

sql = f"INSERT INTO pessoas (pessoa_id, nome, nome_civil, tipo) VALUES ({pessoa_id}, '{nome}', '{nome_civil}', '{tipo}')"

cur.execute(sql)
con.commit()
con.close()
