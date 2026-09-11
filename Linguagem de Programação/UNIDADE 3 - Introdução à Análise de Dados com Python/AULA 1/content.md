# Aula 1 — Bancos de Dados e CRUD com Python e SQLite

## Ponto de Partida

Python é uma linguagem de programação amplamente utilizada para interagir com sistemas de gerenciamento de banco de dados (SGBD) por meio de bibliotecas como a `sqlite3`. Essa biblioteca permite a criação, leitura, atualização e exclusão de dados em bancos de dados SQL, seguindo o modelo **CRUD** (Create, Read, Update, Delete). Com a Python, nós, desenvolvedores, podemos desenvolver aplicativos que se comunicam de forma eficaz com bancos de dados relacionais, proporcionando flexibilidade e escalabilidade para nossas aplicações.

O modelo CRUD consiste em uma abordagem fundamental para operações de banco de dados. Nesse contexto, "Create" envolve a inserção de novos registros, "Read" refere-se à recuperação de informações, "Update" possibilita a modificação de registros existentes e "Delete" diz respeito à exclusão de dados. Python simplifica a implementação dessas operações CRUD, fazendo desse modelo uma escolha popular para desenvolvedores que desejam criar aplicativos com funcionalidades de banco de dados eficientes e robustas.

> **Desafio da aula:** suponha que você precise criar uma tabela de contatos para a comunicação da empresa em que trabalha. Nessa tabela, a seção "Contatos" deve armazenar informações de contatos, incluindo nome, e-mail e número de telefone.

## Vamos Começar!

### Linguagem de consulta estruturada – SQL

A linguagem **SQL** (Structured Query Language) desempenha um papel fundamental na comunicação com bancos de dados relacionais. Ela foi inicialmente estabelecida como um padrão pelo American National Standards Institute (ANSI) em 1986 e passou por várias revisões desde então. Embora diferentes fornecedores de softwares de banco de dados, como Oracle e Microsoft, tenham adaptado o SQL com suas extensões e modificações exclusivas, ainda existe um núcleo comum de comandos SQL que é padrão em todos os sistemas.

As instruções em SQL podem ser agrupadas em três categorias principais:

1. **DDL** (Data Definition Language – Linguagem de Definição de Dados): essas instruções se concentram na estrutura do banco de dados, permitindo a criação, modificação e exclusão de bancos de dados e tabelas. Alguns comandos incluem `CREATE` (para criar tabelas), `ALTER` (para modificar a estrutura) e `DROP` (para excluir tabelas ou bancos de dados).
2. **DML** (Data Manipulation Language – Linguagem de Manipulação de Dados): as instruções DML são usadas para recuperar, atualizar, inserir e excluir dados no banco de dados. Comandos comuns incluem `SELECT` (para recuperar dados), `INSERT` (para adicionar novos registros), `UPDATE` (para modificar registros existentes) e `DELETE` (para excluir registros).
3. **DCL** (Data Control Language – Linguagem de Controle de Dados): o DCL lida com a segurança e a autorização de acesso aos dados no banco de dados. Comandos como `GRANT` (para conceder privilégios) e `REVOKE` (para revogar privilégios) são usados para garantir que apenas usuários autorizados possam acessar e modificar os dados.

Além dessas categorias, o SQL também oferece funcionalidades avançadas, como agregações, junções, subconsultas e transações, as quais viabilizam consultas complexas e a manipulação eficaz de dados. A flexibilidade do SQL o torna uma linguagem poderosa para trabalhar com bancos de dados relacionais, independentemente do sistema de gerenciamento de banco de dados (SGBD) específico em uso. Embora possa haver variações nas implementações de SQL de diferentes fornecedores, a base comum permite que os desenvolvedores escrevam consultas portáteis que funcionam em várias plataformas de banco de dados.

### Conexão com banco de dados

Quando desenvolvemos uma aplicação em uma linguagem de programação que precisa interagir com um Sistema Gerenciador de Banco de Dados Relacional (RDBMS), é essencial estabelecer uma conexão entre esses dois processos distintos. Depois que a conexão é estabelecida, podemos enviar comandos SQL para realizar operações no banco de dados. Para viabilizar essa comunicação entre a linguagem de programação e o RDBMS, fazemos uso de tecnologias como **Open Database Connectivity (ODBC)** e **Java Database Connectivity (JDBC)**.

Tanto o ODBC quanto o JDBC oferecem uma maneira padronizada de os programadores acessarem os recursos do banco de dados a partir de uma Interface de Programação de Aplicativos (API). Uma das grandes vantagens dessas tecnologias é a possibilidade de que uma aplicação acesse diferentes Sistemas Gerenciadores de Banco de Dados sem a necessidade de recompilar o código. Isso se torna viável porque a comunicação direta com o RDBMS é realizada por meio de um software específico, chamado "driver", responsável por traduzir as chamadas ODBC e JDBC para a linguagem compreendida pelo RDBMS.

No contexto de Python, para se comunicar com um RDBMS, podemos usar bibliotecas específicas que incorporam os drivers de fornecedores. Isso permite a conexão e a execução de comandos SQL no banco de dados. O **PEP 249** (Python Database API Specification v2.0) estabelece regras que os fornecedores devem seguir ao criar módulos para acessar bancos de dados. Um dos princípios é o de que todos os módulos precisam implementar um método chamado `connect(parameters...)` para conceber a conexão com o banco. Isso facilita a alteração do banco de dados, pois apenas os parâmetros de conexão precisam ser ajustados, sem a necessidade de modificar o código.

O **SQLite** é uma poderosa biblioteca de banco de dados escrita em linguagem C que oferece um mecanismo de banco de dados SQL completo, embora compacto, e de alta confiabilidade. Diferentemente da maioria dos sistemas de gerenciamento de bancos de dados SQL, o SQLite opera sem a necessidade de um servidor separado. Em vez disso, ele lê e escreve diretamente em arquivos de disco. Isso significa que um banco de dados completo, contendo tabelas, índices, triggers e visualizações, é armazenado em um único arquivo no sistema de arquivos. Para os desenvolvedores que utilizam Python, a linguagem possui um módulo integrado chamado `sqlite3`, o qual permite a interação com o mecanismo do banco de dados SQLite.

Vamos criar um banco de dados! Faremos nossa implementação no Google Colab.

```python
import sqlite3

# 1. Conectar ao banco de dados (ou criar um novo)
conn = sqlite3.connect('exemplo.db')

# 2. Criar um objeto cursor
cursor = conn.cursor()

# 3. Definir o comando SQL para criar a tabela
create_table = '''
CREATE TABLE IF NOT EXISTS Produtos (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    preco REAL NOT NULL,
    estoque INTEGER
);
'''

# 4. Executar o comando SQL para criar a tabela
cursor.execute(create_table)

# 5. Confirmar as alterações (commit)
conn.commit()

# 6. Fechar a conexão com o banco de dados
conn.close()
```

1. Importamos o módulo `sqlite3` e conectamos (ou criamos) um banco de dados chamado "exemplo.db".
2. Criamos um objeto cursor que nos permite executar comandos SQL.
3. Definimos o comando SQL para criar a tabela "Produtos" com campos para "id", "nome", "preco" e "estoque".
4. Executamos o comando SQL usando o cursor.
5. Confirmamos as alterações no banco de dados com `commit()`.
6. Por fim, fechamos a conexão com o banco de dados.

O comando `CREATE TABLE` é um exemplo de DDL (Data Definition Language, ou Linguagem de Definição de Dados), pois possibilita a definição de uma nova estrutura de banco de dados.

## Siga em Frente...

### CRUD – CREATE, READ, UPDATE, DELETE

Podemos inserir informações (create), ler (read), atualizar (update) e apagar (delete). Os passos necessários para efetuar uma das operações do CRUD são sempre os mesmos: (i) estabelecer a conexão com um banco; (ii) criar um cursor e executar o comando; (iii) gravar a operação; (iv) fechar o cursor e a conexão.

Vamos criar um exemplo no qual haverá a inserção de um novo produto na tabela "Produtos". Suponhamos que você deseje adicionar um novo produto com nome, preço e quantidade em estoque.

```python
import sqlite3

# Conectando ao banco de dados
conn = sqlite3.connect('exemplo.db')
cursor = conn.cursor()

# Dados do novo produto
novo_produto = ('Camiseta', 19.99, 50)

# Comando SQL para inserir o novo produto na tabela
inserir_produto = 'INSERT INTO Produtos (nome, preco, estoque) VALUES (?, ?, ?)'

# Executando o comando SQL para inserção
cursor.execute(inserir_produto, novo_produto)

# Confirmando as alterações
conn.commit()

# Fechando a conexão
conn.close()
```

Confira, a seguir, um exemplo de como você pode recuperar todos os produtos da tabela "Produtos" e exibi-los:

```python
import sqlite3

# Conectando ao banco de dados
conn = sqlite3.connect('exemplo.db')
cursor = conn.cursor()

# Comando SQL para selecionar todos os produtos
selecionar_produtos = 'SELECT * FROM Produtos'

# Executando o comando SQL
cursor.execute(selecionar_produtos)

# Obtendo todos os registros e exibindo-os
produtos = cursor.fetchall()
for produto in produtos:
    print(produto)

# Fechando a conexão
conn.close()
```

Acompanhe, agora, um exemplo de como atualizar o preço de um produto específico na tabela "Produtos":

```python
import sqlite3

# Conectando ao banco de dados
conn = sqlite3.connect('exemplo.db')
cursor = conn.cursor()

# Novo preço e ID do produto a ser atualizado
novo_preco = 24.99
produto_id = 1  # Suponha que queiramos atualizar o produto com ID 1

# Comando SQL para atualizar o preço do produto
atualizar_preco = 'UPDATE Produtos SET preco = ? WHERE id = ?'

# Executando o comando SQL de atualização
cursor.execute(atualizar_preco, (novo_preco, produto_id))

# Confirmando as alterações
conn.commit()

# Fechando a conexão
conn.close()
```

Observe, a seguir, um exemplo de como excluir um produto da tabela "Produtos" com base no seu ID:

```python
import sqlite3

# Conectando ao banco de dados
conn = sqlite3.connect('exemplo.db')
cursor = conn.cursor()

# ID do produto a ser excluído
produto_id = 2  # Suponha que queiramos excluir o produto com ID 2

# Comando SQL para excluir o produto
excluir_produto = 'DELETE FROM Produtos WHERE id = ?'

# Executando o comando SQL de exclusão
cursor.execute(excluir_produto, (produto_id,))

# Confirmando as alterações
conn.commit()

# Fechando a conexão
conn.close()
```

É importante lembrar que esses são exemplos simplificados. Em uma aplicação real, talvez você precise adicionar tratamento de erros, validação de dados e outros recursos extras. Por isso é essencial sempre praticar e analisar cada vez mais exemplos para compreender tais conceitos.

## Vamos Exercitar?

Vamos pensar no problema apresentado no início desta aula! O objetivo é criar a tabela "Contatos" para armazenar informações de contatos, incluindo nome, e-mail e número de telefone. Vamos ao código!

```python
import sqlite3

# CREATE (Criação da tabela e inserção de dados de exemplo)
conn = sqlite3.connect('contatos.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Contatos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    email TEXT,
    telefone TEXT
)
''')

dados_exemplo = [
    ('João', 'joao@email.com', '123-456-7890'),
    ('Maria', 'maria@email.com', '987-654-3210'),
    ('Carlos', 'carlos@email.com', '555-555-5555')
]

cursor.executemany('INSERT INTO Contatos (nome, email, telefone) VALUES (?, ?, ?)', dados_exemplo)
conn.commit()

# READ (Leitura e exibição dos contatos)
cursor.execute('SELECT * FROM Contatos')
contatos = cursor.fetchall()
print('Contatos:')
for contato in contatos:
    print(contato)

# UPDATE (Atualização do número de telefone do contato com ID 2)
novo_telefone = '999-999-9999'
contato_id = 2

cursor.execute('UPDATE Contatos SET telefone = ? WHERE id = ?', (novo_telefone, contato_id))
conn.commit()

# DELETE (Exclusão do contato com ID 1)
contato_id_para_excluir = 1

cursor.execute('DELETE FROM Contatos WHERE id = ?', (contato_id_para_excluir,))
conn.commit()

# Fechando a conexão
conn.close()
```

Nesse código, criamos uma tabela de contatos que permitiu a você praticar as operações CREATE, READ, UPDATE e DELETE em um cenário mais simples.

Espero que tenha gostado da solução! Lembre-se: a prática é importante! Mude alguma parte desse código e diversifique seu conhecimento!

## Saiba mais

1. Para conhecer mais detalhes sobre SQL, faça a leitura do livro *Linguagem SQL: fundamentos e práticas*, cujo link de acesso está disponível a seguir.
   > CARDOSO, V.; CARDOSO, G. **Linguagem SQL: fundamentos e práticas**. São Paulo: Saraiva, 2013.

2. Como mencionado anteriormente, uma leitura interessante para quem está começando a programar em Python é a do livro *Python 3: conceitos e aplicações: uma abordagem didática*.
   > BANIN, S. L. **Python 3: conceitos e aplicações: uma abordagem didática**. São Paulo: Érica, 2018. E-book.

3. Também encorajo você a conhecer o livro *Banco de dados: projetos e implementação*, que apresenta conceitos e aplicações de bancos de dados.
   > MACHADO, F. N. R. **Banco de dados: projeto e implementação**. 3. ed. Sa~o Paulo: E´rica, 2014.

## Referências

- BANIN, S. L. Python 3: conceitos e aplicações: uma abordagem didática. São Paulo: Érica, 2018. E-book. Disponível em: https://integrada.minhabiblioteca.com.br/books/9788536530253. Acesso em: 21 out. 2023.
- CARDOSO, V.; CARDOSO, G. Linguagem SQL: fundamentos e práticas. São Paulo: Saraiva, 2013.
- LEMBURG, M. PEP 249 - Python database API specification v.2.0. Python Enhancement Proposals, 12 abr. 1999. Disponível em: https://peps.python.org/pep-0249/#description. Acesso em: 31 out. 2023.
- MACHADO, F. N. R. Banco de dados: projeto e implementac¸a~o. 3. ed. Sa~o Paulo: E´rica, 2014.
- MANZANO, J. A. N. G.; OLIVEIRA, J. F. de. Algoritmos: lógica para desenvolvimento de programação de computadores. 29. ed. São Paulo: Érica, 2019.
- SQLITE3 – DB-API 2.0 interface for SQLite databases. Python 3.12.2 Documentation, [s. d.]. Disponível em: https://docs.python.org/3/library/sqlite3.html#module-sqlite3. Acesso em: 31 out. 2023.
