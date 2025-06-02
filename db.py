import psycopg2

def criar_conexao():
   try:
       conn = psycopg2.connect(
           dbname='prontuario',
           user='postgres',
           password= 'post',
           host= 'localhost',
           port= '5432'
       )
       print("Conexão realizada com sucesso!")
       return conn
   except Exception as e:
       print(f"Erro ao conectar com o banco de dados: {e}")
       return None


def criar_prontuario(paciente, diagnostico, tratamento, usuario_id):
    if not paciente.strip() or not diagnostico.strip() or not tratamento.strip():
        print("Nenhum campo pode ficar em branco!")
        return
    conn = criar_conexao()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO prontuarios (paciente, diagnostico, tratamento, usuario_id) VALUES (%s, %s, %s, %s)",
                (paciente, diagnostico, tratamento, usuario_id)
            )
            conn.commit()
            print("Prontuário criado com sucesso!")
        except Exception as e:
            print(f"Erro ao criar prontuário: {e}")
        finally:
            cursor.close()
            conn.close()

def atualizar_prontuario(prontuario_id, paciente, diagnostico, tratamento):
    if not paciente.strip() or not diagnostico.strip() or not tratamento.strip():
        print("Nenhum campo pode ficar em branco!")
        return
    conn = criar_conexao()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE prontuarios
                SET paciente = %s, diagnostico = %s, tratamento = %s
                WHERE id = %s
            """, (paciente, diagnostico, tratamento, prontuario_id))
            conn.commit()
            print("Prontuário atualizado com sucesso!")
        except Exception as e:
            print(f"Erro ao atualizar prontuário: {e}")
        finally:
            cursor.close()
            conn.close()

def listar_prontuarios():
    conn = criar_conexao()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM prontuarios")
    prontuarios = cursor.fetchall()
    cursor.close()
    conn.close()
    return prontuarios

def buscar_prontuario_por_id(prontuario_id):
    conn = criar_conexao()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM prontuarios WHERE id = %s", (prontuario_id,))
    prontuario = cursor.fetchone()
    cursor.close()
    conn.close()
    return prontuario

def deletar_prontuario(prontuario_id):
    conn = criar_conexao()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM prontuarios WHERE id = %s", (prontuario_id,))
    conn.commit()
    cursor.close()
    conn.close()

def buscar_prontuarios_por_nome(parte_nome):
    conn = criar_conexao()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM prontuarios WHERE paciente ILIKE %s ORDER BY paciente ASC",
                (f"%{parte_nome}%",)
            )
            prontuarios = cursor.fetchall()
            for p in prontuarios:
                print(f"ID: {p[0]}, Paciente: {p[1]}, Diagnóstico: {p[2]}, Tratamento: {p[3]}")
            return prontuarios
        except Exception as e:
            print(f"Erro ao buscar prontuários: {e}")
            return []
        finally:
            cursor.close()
            conn.close()

def listar_usuarios_com_prontuarios():
    conn = criar_conexao()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT u.id, u.email, p.id, p.paciente, p.diagnostico, p.tratamento
                FROM usuarios u
                INNER JOIN prontuarios p ON p.usuario_id = u.id
                ORDER BY u.email ASC
            """)
            resultados = cursor.fetchall()
            for reg in resultados:
                print(f"Usuário ID: {reg[0]}, Email: {reg[1]}, Prontuário ID: {reg[2]}, Paciente: {reg[3]}, Diagnóstico: {reg[4]}, Tratamento: {reg[5]}")
            return resultados
        except Exception as e:
            print(f"Erro ao listar usuários com prontuários: {e}")
            return []
        finally:
            cursor.close()
            conn.close()