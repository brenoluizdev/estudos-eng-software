# Roteiro de Estudos — Linguagem de Programação (Python)

Lista de todos os tópicos ensinados nas 4 unidades (20 aulas) desta disciplina, gerada a partir da
leitura de todos os `content.md`. Marque `[x]` conforme for dominando cada ponto.

---

## Unidade 1 — Introdução à Linguagem Python

### Aula 1 — Introdução à Linguagem Python
- [ ] O que é Python, história (Guido van Rossum) e por que a linguagem é tão usada
- [ ] PEP 8 (guia de estilo de código Python) e código "pythonic"
- [ ] Interpretador Python, IDEs (PyCharm, VSCode) e Python Anaconda
- [ ] Jupyter Notebook e Google Colab
- [ ] Variáveis: conceito e alocação em memória
- [ ] Tipos de dados básicos: `int`, `str`, `float`, `bool` e inferência automática de tipo (`type()`)
- [ ] Entrada e saída: `input()` e `print()`
- [ ] Formatação de string: formatadores de caracteres (`%`) e f-strings (PEP 498)

### Aula 2 — Operadores Relacionais, Estruturas Lógicas e Condicionais
- [ ] Operadores relacionais (`==`, `!=`, `>`, `<`, `>=`, `<=`)
- [ ] Estruturas lógicas / operadores booleanos (`and`, `or`, `not`)
- [ ] Estruturas condicionais `if`, `elif`, `else`

### Aula 3 — Estruturas de Repetição e Controle de Repetição
- [ ] Estrutura de repetição `for`
- [ ] Estrutura de repetição `while`
- [ ] `range()`
- [ ] Controle de repetição: `break` e `continue`

### Aula 4 — Funções em Python: Built-in, Definidas pelo Usuário e Lambda
- [ ] Funções built-in (ex.: `len()`)
- [ ] Funções definidas pelo usuário: parâmetros, `return`
- [ ] Funções anônimas (`lambda`)

### Aula 5 — Revisão da Unidade + Estudo de Caso
- [ ] Revisão de variáveis, tipos, condicionais, repetição e funções
- [ ] Estudo de caso: calculadora de desconto (validação de percentual, condicionais aninhadas)

---

## Unidade 2 — Explorando Recursos do Python

### Aula 1 — Sequências, Listas e Tuplas em Python
- [ ] Objetos do tipo sequência (conceito geral)
- [ ] Listas: criação, indexação, métodos, mutabilidade
- [ ] Tuplas: criação, imutabilidade, diferença para listas

### Aula 2 — Sets, Dicionários e Arrays NumPy em Python
- [ ] Objetos do tipo `set`: criação, adição/remoção de elementos, verificação de pertencimento
- [ ] Dicionários (`mapping`): criação por atribuição, por pares chave:valor, por lista de tuplas, por `zip()`
- [ ] Arrays NumPy: criação, operações matemáticas, indexação

### Aula 3 — Orientação a Objetos: Classes e Herança em Python
- [ ] Conceitos de orientação a objetos (classe, objeto/instância, atributo, método)
- [ ] Definição de classes em Python (`__init__`, métodos, atributos de instância)
- [ ] Herança entre classes (classe-pai / classe-filha)
- [ ] Benefícios da herança e sobrescrita de métodos

### Aula 4 — Módulos, Bibliotecas e Visualização de Dados com Matplotlib
- [ ] Diferença entre módulo e biblioteca
- [ ] Formas de importar um módulo (`import`, `from ... import`, `as`)
- [ ] Classificação dos módulos: built-in, de terceiros e próprios
- [ ] Matplotlib: gráfico de linha e gráfico de barras, rótulos e título

### Aula 5 — Revisão da Unidade + Estudo de Caso
- [ ] Revisão de listas, tuplas, sets, dicionários, NumPy, POO e Matplotlib
- [ ] Estudo de caso: catalogação de livros (classe `Livro`, funções para gerenciar biblioteca, gráfico de livros por ano)

---

## Unidade 3 — Introdução à Análise de Dados com Python

### Aula 1 — Bancos de Dados e CRUD com Python e SQLite
- [ ] Linguagem de consulta estruturada (SQL): DDL, DML, DCL
- [ ] Conexão com banco de dados via `sqlite3` (conectar, cursor, criar tabela, commit, fechar conexão)
- [ ] CRUD completo: CREATE, READ, UPDATE, DELETE

### Aula 2 — Introdução à Biblioteca pandas: Series e Leitura de Dados
- [ ] O que é a biblioteca `pandas` e para que serve
- [ ] `Series`: criação a partir de lista e de dicionário
- [ ] Leitura de dados estruturados com pandas (ex.: `read_html`)

### Aula 3 — Leitura, Transformação e Extração de Dados com pandas
- [ ] Métodos de leitura/escrita do pandas (`read_csv`, `read_json`, `read_excel`, `read_fwf`, `to_pickle` etc.)
- [ ] Captura e transformação de dados (`drop_duplicates`, criação de colunas)
- [ ] Extração de informações com `loc` e filtragem por máscara booleana

### Aula 4 — Visualização de Dados com Matplotlib, pandas e Seaborn
- [ ] Matplotlib aplicado a dados (revisão)
- [ ] Método `.plot()` do pandas e seus parâmetros (`kind='bar'`, `'pie'`, `'line'` etc.)
- [ ] Biblioteca Seaborn (`sns.set`, gráficos estatísticos)

### Aula 5 — Revisão da Unidade + Estudo de Caso
- [ ] Revisão de SQL/SQLite, pandas e visualização de dados
- [ ] Estudo de caso: CRUD de funcionários em banco SQLite (conectar, criar tabela, inserir, consultar, atualizar, deletar)

---

## Unidade 4 — Aplicações com Python

### Aula 1 — Desenvolvimento de Sistemas Web com Python
- [ ] Visão geral do desenvolvimento de sistemas para a web
- [ ] Diferença entre front-end e back-end
- [ ] Gerar/exibir HTML a partir de Python (primeiras páginas web)

### Aula 2 — Desenvolvimento Mobile com Python e KivyMD
- [ ] Introdução ao desenvolvimento mobile com Python
- [ ] Framework KivyMD (Material Design Components for Kivy) e instalação
- [ ] Widgets e organização de telas com `MDTabs`

### Aula 3 — Testes em Python: Assertions, Doctests e Unittest
- [ ] `assert` (assertions)
- [ ] Doctests (testes embutidos em docstrings)
- [ ] Módulo `unittest` (`TestCase`, `assertEqual`, `if __name__ == '__main__':`)

### Aula 4 — Machine Learning e a Biblioteca TensorFlow
- [ ] Teoria geral de machine learning
- [ ] Tipos de treinamento: supervisionado, não supervisionado e por reforço
- [ ] TensorFlow: modelo de regressão linear, autoencoder e aprendizado por reforço (`gym`)

### Aula 5 — Revisão da Unidade + Estudo de Caso
- [ ] Revisão de web, mobile, testes e machine learning
- [ ] Estudo de caso: classificação de dígitos escritos à mão com TensorFlow

---

## Prática complementar

- [ ] Revisar os quizzes já respondidos em [`EXERCICIOS DAS UNIDADES/`](EXERCICIOS%20DAS%20UNIDADES) (um arquivo por unidade, com gabarito comentado)
- [ ] Pedir simulados de revisão por unidade à IA (ver [`../AGENTS.md`](../AGENTS.md) para como isso funciona)

> Quer que este roteiro também tenha vídeos recomendados por tópico (como o de Fundamentos de Cálculo
> Aplicado)? É só pedir — nesta primeira versão ficou só a lista de conteúdos.
