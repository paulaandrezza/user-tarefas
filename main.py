import schema
import usuarios
import tarefas

def menu():
    print(22 * "*")
    print("*** Menu de Opções ***")
    print(22 * "*")
    print("1. Manter Tarefas\n2. Manter Usuários\n3. Sair")
    selecao = int(input("Selecione uma opção: "))
    return selecao


def submenu(tabela):
    print(22 * "*")
    print(f"*** Menu de {tabela} ***")
    print(22 * "*")
    print(f"0. Retornar ao menu principal.\n1. Inserir {tabela}\n2. Atualizar {tabela}\n3. Consultar{tabela}\n4. Excluir {tabela}")
    selecaosub = int(input("Selecione a opção: "))
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
    print("Iniciando Teste de tarefas...")
    banco = input("Informe o nome do banco: ")
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
            print("Opção inválida!")
            opcao = menu()
            limpar()
            continue

        opcaosub = submenu(tabela)
        limpar()
        while opcaosub != 0:
            
            if opcaosub == 1:
                print(f"Inserir {tabela}")
                if tabela == "usuarios":
                    nome = input("Informe o nome completo: ")
                    usuario = (nome, )
                    user.inserir_user(usuario)                
                else:
                    pass
            elif opcaosub == 2:
                print(f"Atualizar {tabela}")
                if tabela == "usuarios":
                    user.consultar_user()
                    nome = input("Informe o nome completo: ")
                    usuarioid = int(input("Indique o id do usuário: "))
                    usuario = (nome, usuarioid)
                    user.atualizar_user(usuario) 
                else:
                    pass
            elif opcaosub == 3: 
                print(f"Consultar {tabela}")
                if tabela == "usuarios":
                    user.consultar_user()
                else:
                    task.consultar_task()
            elif opcaosub == 4:
                print(f"Excluir {tabela}")
                if tabela == "usuarios":
                    user.consultar_user()
                    usuarioid = int(input("Indique o id do usuário: "))
                    usuario = (usuarioid, )
                    user.excluir_user(usuario) 
                else:
                    pass
            else:
                print("Opção inválida!")
                opcaosub = submenu(tabela)
                limpar()

            limpar()
            opcaosub = submenu(tabela) 
            limpar()
        opcao = menu()
        limpar()
    

    