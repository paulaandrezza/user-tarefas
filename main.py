from datetime import date

import schema
import tarefas
import usuarios


def menu():
    print("\033[1;44;1m" + 22 * "*")
    print("*** Menu de Opções ***")
    print(22 * "*" + "\033[m")
    print("\033[1;36m1. Manter Tarefas\n2. Manter Usuários\n3. Sair\033[m")
    selecao = int(input("\033[1;46mSelecione uma opção:\033[m "))
    return selecao


def submenu(tabela):
    print("\033[1;44;1m" + 24 * "*")
    print(f"*** Menu de {tabela} ***")
    print(24 * "*" + "\033[m")
    print(f"\033[1;36m0. Retornar ao menu principal.\n1. Inserir {tabela}\n2. Atualizar {tabela}\n3. Consultar {tabela}\n4. Excluir {tabela}\033[m")
    selecaosub = int(input("\033[1;46mSelecione a opção:\033[m "))
    return selecaosub


def limpar():
    # Importar o módulo os do sistema operacional
    import os
    # Importar um módulo par aguardar um tempo em segundos passados como parametro
    from time import sleep

    def screen_clear():
        #Linux ou Mac
        if os.name == 'posix':
            _ = os.system('clear')
        else:
            # Windows
            _ = os.system('cls')
            
    sleep(1)
    screen_clear()
    
    
#A variável __name__ representa o nome do módulo.
#Entretanto, quando o módulo é executado por si só como um programa,
#__name__ é definida para __main__. Diferente de quando o módulo
#é importado, no qual o valor fica de fato igual ao nome do módulo.

if __name__ == '__main__':
    limpar()
    print("\033[0;32mIniciando Teste de tarefas...\033[m")
    banco = input("\033[1;36mInforme o nome do banco:\033[m ")
    conn = schema.criar_banco(banco)

    limpar()
    opcao = menu()
    limpar()
    while opcao != 3:
        if opcao == 1:
            tabela = "tarefas"
            task = tarefas.Tarefas(conn)
        elif opcao == 2:
            tabela = "usuarios"
            user = usuarios.Usuarios(conn)
        else:
            print("\033[1;41mOpção inválida!\033[m")
            opcao = menu()
            limpar()
            continue

        opcaosub = submenu(tabela)
        limpar()
        while opcaosub != 0:

            # INSERIR
            if opcaosub == 1:
                print(f"Inserir {tabela}")
                if tabela == "usuarios":
                    nome = input("Informe o nome completo: ")
                    usuario = (nome, )
                    print(user.inserir_user(usuario))            
                else:
                    usuario_id = input("Informe o id do usuário para qual deseja inserir: ")
                    descricao = input("Informe a descrição da tarefa: ")
                    data = date.today()
                    tarefa = (usuario_id, descricao, data, )
                    print(task.inserir_task(tarefa))
                    input("Pressione <ENTER> para coninuar...")
            # ATUALIZAR
            elif opcaosub == 2:
                print(f"Atualizar {tabela}")
                if tabela == "usuarios":
                    user.consultar_user()
                    nome = input("Informe o nome completo: ")
                    usuarioid = int(input("Indique o id do usuário: "))
                    usuario = (nome, usuarioid)
                    print(user.atualizar_user(usuario))
                else:
                    task.consultar_task()
                    idTarefas = input("Informe o ID da tarefa que deseja atualizar: ")
                    descricao = input("Infome a nova descrição: ")
                    tarefas = (descricao, idTarefas, )
                    print(task.atualizar_task(tarefas))
                    limpar()
                    task.consultar_task()
            # CONSULTAR
            elif opcaosub == 3: 
                print(f"Consultar {tabela}")
                if tabela == "usuarios":
                    print(user.consultar_user())
                else:
                    print(task.consultar_task())
            #EXCLUIR
            elif opcaosub == 4:
                print(f"Excluir {tabela}")
                if tabela == "usuarios":
                    user.consultar_user()
                    usuarioid = int(input("Indique o id do usuário: "))
                    usuario = (usuarioid, )
                    print(user.excluir_user(usuario))
                else:
                    task.consultar_task()
                    tarefa = input("Informe o id da tarefa que deseja excluir: ")
                    tarefa = (tarefa, )
                    print(task.excluir_task(tarefa))
            else:
                print("\033[1;41mOpção inválida!\033[m")
                opcaosub = submenu(tabela)
                limpar()

            limpar()
            opcaosub = submenu(tabela) 
            limpar()
        opcao = menu()
        limpar()
    

    