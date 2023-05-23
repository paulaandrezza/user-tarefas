import sqlite3
from sqlite3 import Error


def criar_banco(banco):
    
    # Definindo variavel com a conexao com o BD.
    conn = sqlite3.connect(banco)
    # Definindo cursor para manipular dados do BD.
    c = conn.cursor()

    try:
        c.execute("""
            CREATE TABLE IF NOT EXISTS "usuarios" ("idUsuarios" INTEGER NOT NULL, "nomeCompleto" TEXT NOT NULL UNIQUE, PRIMARY KEY("idUsuarios" AUTOINCREMENT));
        """)
        
        c.execute("""
            CREATE TABLE IF NOT EXISTS "tarefas" ("idTarefas" INTEGER NOT NULL, "descricao" TEXT NOT NULL, "dataInclusao" TEXT NOT NULL, "usuario_id" INTEGER NOT NULL, PRIMARY KEY("idTarefas" AUTOINCREMENT), FOREIGN KEY("usuario_id") REFERENCES "usuarios"("idUsuarios"));
        """)

        print("Tabelas criadas com sucesso!")
        return conn
    
    except Error as e:
        print(e)