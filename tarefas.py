class Tarefas:

    def __init__(self, conn):
        self.descricao = ""
        self.datainclusao = 20230426
        self.usuarioid = 1
        self.conn = conn
        self.cursor = self.conn.cursor()


    # INSERIR
    def inserir_task(self, tarefa):
        self.cursor.execute("INSERT INTO tarefas (usuario_id, descricao, dataInclusao) VALUES (?, ?, ?);", tarefa)
        self.conn.commit()
        return "\033[1;34mTarefa cadastrada com sucesso!\033[m"
        
    # ATUALIZAR
    def atualizar_task(self, tarefa):
        self.cursor.execute("UPDATE tarefas SET descricao = ? WHERE idTarefas = ?;", tarefa)
        self.conn.commit()
        return "\033[1;34mTarefa atualizada com sucesso!\033[m"
    # CONSULTAR
    def consultar_task(self):
        self.cursor.execute("SELECT t.*, u.nomeCompleto FROM tarefas t inner join usuarios u on t.usuario_id=u.idUsuarios;")
        resultado = self.cursor.fetchall()
        if resultado:
            print("{:<3} {:<30} {:<15} {:<5} {:<30}".format("ID", "Descrição", "Data", "ID", "Nome Completo"))
            for item in range(len(resultado)):
                print("{:<3} {:<30} {:<15} {:<5} {:<30}".format(resultado[item][0], resultado[item][1], resultado[item][2], resultado[item][3], resultado[item][4]))
            input("\033[1;44mPressione <ENTER> para coninuar...\033[m")
        return "\033[1;34mConsulta realizada com sucesso!\033[m"

    def excluir_task(self, tarefa):
        self.cursor.execute("DELETE FROM tarefas WHERE idTarefas=?;", tarefa)
        self.conn.commit()
        return "\033[1;34mTarefa excluída com sucesso!\033[m"
        