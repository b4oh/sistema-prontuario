import pwinput
from services.user_services import autenticar_usuario, buscar_usuario_por_email
from admin_menu import menu_admin

def menu_login():
    print("\n" + "="*45)
    print("         🔐  LOGIN DO SISTEMA  🔐".center(45))
    print("="*45)
    email = input("Usuário (email): ")
    senha = pwinput.pwinput(prompt="Senha: ", mask="*")  
    print("="*45)
    print("Tentando autenticar...\n")
    if autenticar_usuario(email, senha):
        print("Bem-vindo ao sistema!")
        usuario = buscar_usuario_por_email(email)
        print("Usuário encontrado:", usuario)
        if usuario:
            usuario_id = usuario[0]
            menu_admin(usuario_id)
        else:
            print("Usuário não encontrado.")
    else:
        print("Falha no login. Tente novamente.")

menu_login()