class Usuarios:

    import sqlite3

    def __init__(self, conn):
        self.nomeCompleto = ""
        self.conn = conn
        self.cursor = self.conn.cursor()

    def inserir_user(self, usuario):
        self.cursor.execute("INSERT INTO usuarios (nomeCompleto) VALUES (?);", usuario)
        self.conn.commit()
        return "\033[1;34mUsuário inserido com sucesso!\033[m"

    def atualizar_user(self, usuario):
        self.cursor.execute("UPDATE usuarios SET nomeCompleto = ? WHERE idUsuarios = ?;", usuario)
        self.conn.commit()
        return "\033[1;34mUsuário atualizado com sucesso!\033[m"
        
    def consultar_user(self):
        self.cursor.execute("SELECT * FROM usuarios;")
        resultado = self.cursor.fetchall()
        if resultado:
            print("ID\tNome Completo")
            for item in range(len(resultado)):
                print(resultado[item][0], resultado[item][1])

        input("Pressione <ENTER> para coninuar...")
        return "\033[1;34mConsulta realizada com sucesso!\033[m"

    def excluir_user(self, usuario):
        self.cursor.execute("DELETE FROM usuarios WHERE idUsuarios = ?;", usuario)
        self.conn.commit()
        return "\033[1;34mUsuário excluído com sucesso!\033[m"