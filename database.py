import sqlite3
from datetime import date

def conectar():
  banco = sqlite3.connect('clima.db')
  cursor = banco.cursor()
  conexao = (banco, cursor)
  return conexao

def criar_tabela():
  try:
    banco, cursor = conectar()
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS clima (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cidade TEXT,
            temperatura REAL,
            descricao TEXT,
            umidade INTEGER,
            data_consulta TEXT
        )
    ''')
    banco.commit()
  except sqlite3.Error as erro:
    print(f'Erro ao criar tabela: {erro}')
  finally:
    banco.close()

def adicionar_registro(cidade, temperatura, descricao, umidade, data_consulta=date.today()):
  try:
    banco, cursor = conectar()
    cursor.execute(
            "INSERT INTO clima (cidade, temperatura, descricao, umidade, data_consulta) VALUES (?, ?, ?, ?, ?)",
            (cidade, temperatura, descricao, umidade, data_consulta)
        )
    banco.commit()

  except sqlite3.Error as erro:
    print(f'Erro: {erro} ao inserir registro.')
  
  finally:
    banco.close()

def listar_registros():
  try:
    banco, cursor = conectar()
    cursor.execute("SELECT * FROM clima")
    registros = cursor.fetchall()
    
    if not registros:
      print('Nenhum registro foi encontrado.')
      return
    
    print('\nRegistros salvos:')
    print('-'*100)
    
    for registro in registros:
      print(f"ID: {registro[0]} | Cidade: {registro[1]} | Temp: {registro[2]}°C | "
            f"Clima: {registro[3]} | Umidade: {registro[4]}% | Data: {registro[5]}")
      print('-'*100)
  
  except sqlite3.Error as erro:
    print(f'Erro ao listar registros: {erro}')
  
  finally:
    banco.close()