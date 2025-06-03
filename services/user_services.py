from services.security import criptografar, checar_password
from config.db import criar_conexao

def criar_usuario(email, password):
    if not email.strip() or not password.strip():
        print("Erro: Email e senha não podem ser vazios!")
        return

    conn = criar_conexao()
    if conn:
        try:
            cursor = conn.cursor()
            hashpassword = criptografar(password)
            query = "INSERT INTO usuarios (email, password) VALUES (%s, %s)"
            cursor.execute(query, (email, hashpassword))
            conn.commit()
            print("Usuário criado com sucesso!")
        except Exception as e:
            if "duplicate key value violates unique constraint" in str(e):
                print("Erro: Este e-mail já está cadastrado.")
            else:
                print("Erro ao criar usuário")
                print(f"Erro: {e}")
        finally:
            cursor.close()
            conn.close()


def autenticar_usuario(email, password):
    conn = criar_conexao()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT password FROM usuarios WHERE email = %s",
                (email,)
            )
            usuario = cursor.fetchone()
            if usuario and checar_password(password, usuario[0]):
                print("Login realizado com sucesso!")
                return True
            else:
                print("Email ou senha incorretos.")
                return False
        except Exception as e:
            print(f"Erro ao autenticar usuário: {e}")
            return False
        finally:
            cursor.close()
            conn.close()

def listar_usuarios():
    conn = criar_conexao()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id, email FROM usuarios")
            usuarios = cursor.fetchall()
            for usuario in usuarios:
                print(f"ID: {usuario[0]}, Email: {usuario[1]}")
            return usuarios
        except Exception as e:
            print(f"Erro ao listar usuários: {e}")
            return []
        finally:
            cursor.close()
            conn.close()

def atualizar_usuario(id_usuario, novo_username, nova_senha):
    conn = criar_conexao()
    if conn:
        try:
            cursor = conn.cursor()
            nova_senha_criptografada = criptografar(nova_senha)
            cursor.execute(
            "UPDATE usuarios SET email = %s, password = %s WHERE id = %s",
            (novo_username, nova_senha_criptografada, id_usuario)
            )

            conn.commit()
            print("Usuário atualizado com sucesso!")
        except Exception as e:
            print(f"Erro ao atualizar usuário: {e}")
        finally:
            cursor.close()
            conn.close()

def deletar_usuario(id_usuario):
    conn = criar_conexao()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM usuarios WHERE id = %s",
                (id_usuario,)
            )
            conn.commit()
            print("Usuário deletado com sucesso!")
        except Exception as e:
            print(f"Erro ao deletar usuário: {e}")
        finally:
            cursor.close()
            conn.close()

def buscar_usuario_por_email(email):
    from config.db import criar_conexao
    conn = criar_conexao()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id, email, password FROM usuarios WHERE email = %s", (email,))
            usuario = cursor.fetchone()
            return usuario
        except Exception as e:
            print(f"Erro ao buscar usuário: {e}")
            return None
        finally:
            cursor.close()
            conn.close()