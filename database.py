import sqlite3

def create_table():
    print("Verificando ou criando a tabela...")
    # Conectar ao banco de dados
    conn = sqlite3.connect("SistemaDeusuarios.db")
    cursor = conn.cursor()
    
    # Criar a tabela, caso ela não exista
    query = """
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        senha TEXT NOT NULL
    )
    """
    cursor.execute(query)
    conn.commit()
    conn.close()
