# 🛡️ Sistema de Gerenciamento de Prontuários e Usuários

Este projeto é um sistema de gerenciamento de usuários e prontuários médicos, com autenticação segura, menus interativos e integração com banco de dados PostgreSQL.

---

## ✨ Funcionalidades

- **Login seguro** com senha criptografada (bcrypt) e senha mascarada com asteriscos.
- **Menu administrativo** com navegação clara e padronizada.
- **CRUD completo** para usuários e prontuários.
- **Consultas avançadas** usando INNER JOIN, LIKE e ORDER BY.
- **Associação de prontuários a usuários**.
- **Mensagens e menus amigáveis** com emojis e layout organizado.

---

## 📁 Estrutura dos Arquivos

```
prontuarioEletronico/
│
├── main.py                # Tela de login e entrada do sistema
├── admin_menu.py          # Menus de administração, usuários e prontuários
├── user_services.py       # Funções de manipulação de usuários
├── db.py                  # Funções de acesso ao banco de dados (PostgreSQL)
├── venv/                  # Ambiente virtual Python (opcional)
└── ...                    # Outros arquivos do projeto
```

---

## 🛠️ Pré-requisitos

- Python 3.8+
- PostgreSQL
- Bibliotecas Python:
  - psycopg2
  - bcrypt
  - pwinput

---

## 🚀 Instalação

1. **Clone o repositório ou copie os arquivos para sua máquina.**

2. **Crie e ative um ambiente virtual (opcional, mas recomendado):**
   ```sh
   python -m venv venv
   venv\Scripts\activate  # Windows
   ```

3. **Instale as dependências:**
   ```sh
   pip install psycopg2 bcrypt pwinput
   ```

4. **Configure o banco de dados PostgreSQL:**

   - Crie um banco chamado `prontuario`.
   - Crie as tabelas necessárias:

     ```sql
     CREATE TABLE usuarios (
         id SERIAL PRIMARY KEY,
         email VARCHAR(100) UNIQUE NOT NULL,
         password VARCHAR(200) NOT NULL
     );

     CREATE TABLE prontuarios (
         id SERIAL PRIMARY KEY,
         paciente VARCHAR(100) NOT NULL,
         diagnostico TEXT NOT NULL,
         tratamento TEXT NOT NULL,
         usuario_id INTEGER REFERENCES usuarios(id)
     );
     ```

5. **(Opcional) Insira dados de teste:**

   ```sql
   INSERT INTO usuarios (email, password) VALUES
   ('admin@admin.com', '<hash_bcrypt_da_senha>');
   ```

---

## 💻 Como usar

1. **Execute o sistema:**
   ```sh
   python main.py
   ```

2. **Faça login com um usuário cadastrado.**

3. **Navegue pelos menus:**
   - **Usuários:** listar, criar, atualizar, deletar.
   - **Prontuários:** criar, listar, buscar por nome/ID, atualizar, deletar, listar usuários com prontuários (INNER JOIN).

---

## 📝 Exemplos de Consultas SQL

- **INNER JOIN:**  
  Lista todos os usuários e seus prontuários:
  ```sql
  SELECT u.id, u.email, p.id, p.paciente, p.diagnostico, p.tratamento
  FROM usuarios u
  INNER JOIN prontuarios p ON p.usuario_id = u.id
  ORDER BY u.email ASC;
  ```

- **LIKE + ORDER BY:**  
  Busca prontuários por parte do nome do paciente:
  ```sql
  SELECT * FROM prontuarios WHERE paciente ILIKE '%ana%' ORDER BY paciente ASC;
  ```

---

## 🔒 Segurança

- As senhas são armazenadas com hash bcrypt.
- O campo de senha no login é mascarado com asteriscos (usando pwinput).

---




