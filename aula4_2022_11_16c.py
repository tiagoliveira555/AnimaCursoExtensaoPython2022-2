import sqlite3

def conectar():
  conexao = sqlite3.connect('dc_universe.db')

  cursor = conexao.cursor()

  return conexao, cursor