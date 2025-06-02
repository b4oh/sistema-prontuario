from user_services import (
    criar_usuario,
    listar_usuarios,
    atualizar_usuario,
    deletar_usuario
)
from db import (
    criar_prontuario, listar_prontuarios, buscar_prontuario_por_id,
    atualizar_prontuario, deletar_prontuario, buscar_prontuarios_por_nome,
    listar_usuarios_com_prontuarios
)

def menu_admin(usuario_id):
    while True:
        print("\n" + "="*45)
        print("         🛡️  MENU ADMINISTRADOR 🛡️".center(45))
        print("="*45)
        print(" [1] Usuários")
        print(" [2] Prontuários")
        print(" [0] Sair")
        print("="*45)
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            menu_usuarios()
        elif opcao == "2":
            menu_prontuarios(usuario_id)
        elif opcao == "0":
            print("Saindo do menu admin.")
            break
        else:
            print("Opção inválida.")

def menu_usuarios():
    while True:
        print("\n" + "-"*45)
        print("           👤  MENU USUÁRIOS 👤".center(45))
        print("-"*45)
        print(" [1] Listar usuários")
        print(" [2] Criar usuário")
        print(" [3] Atualizar usuário")
        print(" [4] Deletar usuário")
        print(" [0] Voltar")
        print("-"*45)
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_usuarios()
        elif opcao == "2":
            email = input("Novo email: ")
            senha = input("Nova senha: ")
            criar_usuario(email, senha)
        elif opcao == "3":
            id_usuario = input("ID do usuário a atualizar: ")
            novo_email = input("Novo email: ")
            nova_senha = input("Nova senha: ")
            atualizar_usuario(id_usuario, novo_email, nova_senha)
        elif opcao == "4":
            id_usuario = input("ID do usuário a deletar: ")
            deletar_usuario(id_usuario)
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")

def menu_prontuarios(usuario_id):
    while True:
        print("\n" + "-"*45)
        print("        📋  MENU PRONTUÁRIOS 📋".center(45))
        print("-"*45)
        print(" [1] Criar prontuário")
        print(" [2] Listar prontuários")
        print(" [3] Buscar prontuários por nome")
        print(" [4] Buscar prontuário por ID")
        print(" [5] Atualizar prontuário")
        print(" [6] Deletar prontuário")
        print(" [7] Listar usuários com prontuários (INNER JOIN)")
        print(" [0] Voltar")
        print("-"*45)
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            paciente = input("Nome do paciente: ")
            diagnostico = input("Diagnóstico: ")
            tratamento = input("Tratamento: ")
            criar_prontuario(paciente, diagnostico, tratamento, usuario_id)
        elif opcao == "2":
            prontuarios = listar_prontuarios()
            if prontuarios:
                for p in prontuarios:
                    print(f"ID: {p[0]}, Paciente: {p[1]}, Diagnóstico: {p[2]}, Tratamento: {p[3]}")
            else:
                print("Nenhum prontuário encontrado.")
        elif opcao == "3":
            parte_nome = input("Digite parte do nome do paciente: ")
            buscar_prontuarios_por_nome(parte_nome)
        elif opcao == "4":
            pid = input("ID do prontuário: ")
            if pid.isdigit():
                p = buscar_prontuario_por_id(int(pid))
                if p:
                    print(f"ID: {p[0]}, Paciente: {p[1]}, Diagnóstico: {p[2]}, Tratamento: {p[3]}")
                else:
                    print("Prontuário não encontrado.")
            else:
                print("ID inválido.")
        elif opcao == "5":
            pid = input("ID do prontuário: ")
            if pid.isdigit():
                paciente = input("Novo nome do paciente: ")
                diagnostico = input("Novo diagnóstico: ")
                tratamento = input("Novo tratamento: ")
                atualizar_prontuario(int(pid), paciente, diagnostico, tratamento)
            else:
                print("ID inválido.")
        elif opcao == "6":
            pid = input("ID do prontuário: ")
            if pid.isdigit():
                deletar_prontuario(int(pid))
                print("Prontuário deletado.")
            else:
                print("ID inválido.")
        elif opcao == "7":
            listar_usuarios_com_prontuarios()
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")