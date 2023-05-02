class Usuarios:

    import sqlite3

    def __init__(self, conn):
        self.nomeCompleto = ""
        self.conn = conn
        self.cursor = self.conn.cursor()

    def inserir_user(self, usuario):
        self.cursor.execute("INSERT INTO usuarios (nomeCompleto) VALUES (?);", usuario)
        self.conn.commit()
        return "Usuário inserido com sucesso!"

    def atualizar_user(self, usuario):
        self.cursor.execute("UPDATE usuarios SET nomeCompleto = ? WHERE idUsuarios = ?;", usuario)
        self.conn.commit()
        return "Usuário atualizado com sucesso!"
        
    def consultar_user(self):
        self.cursor.execute("SELECT * FROM usuarios;")
        resultado = self.cursor.fetchall()
        if resultado:
            print("ID\tNome Completo")
            for item in range(len(resultado)):
                print(resultado[item][0], resultado[item][1])

        input("Pressione <ENTER> para coninuar...")
        return "Consulta realizada"

    def excluir_user(self, usuario):
        self.cursor.execute("DELETE FROM usuarios WHERE idUsuarios = ?;", usuario)
        self.conn.commit()
        return "Usuário excluído com sucesso!"