# Aula 1 — Introdução à Linguagem Python

## Ponto de Partida

Python é uma linguagem de programação de alto nível amplamente usada na indústria de tecnologia. Nesta aula, você começará a entender por que a Python é tão popular e como pode ser utilizada em diversas aplicações.

Você conhecerá as ferramentas necessárias para dar início à programação em Python, o que inclui a instalação do Python em seu computador e a seleção de um ambiente de desenvolvimento adequado.

As variáveis são fundamentais na programação, pois permitem armazenar e manipular dados. Durante esta etapa de estudos, você aprenderá a criar variáveis e descobrirá os diferentes tipos de dados disponíveis em Python.

> **Desafio da aula:** como professor, preciso avaliar constantemente os estudantes. Sendo assim, quero automatizar a média de notas dos alunos. É possível fazer isso utilizando Python?

## Vamos Começar!

### Introdução à linguagem Python

```python
print("hello world!")
```

```text
hello world!
```

Há uma lenda entre programadores segundo a qual se você não imprimir o "hello world" quando começar a aprender uma linguagem, não conseguirá assimilar nada sobre ela (Ciência da Computação, 2015). Para não correr tal risco, essa foi a primeira linha de comando apresentada a você dentre as muitas que aprenderá nesta disciplina.

Python é uma linguagem de programação versátil e fácil de aprender. Foi criada por **Guido van Rossum** e lançada em 1991. Guido é o principal autor da Python, embora haja muitas contribuições de outros pesquisadores (Python v3.0.1 Documentation, [s. d.]). Desde então, tornou-se uma das linguagens mais populares do mundo por causa de sua legibilidade e sintaxe simples. Você pode se perguntar: "por que escolher Python?". A resposta é clara: Python é usado em várias áreas, incluindo desenvolvimento web, automação, aprendizado de máquina e análise de dados.

De acordo com o guia de desenvolvimento para iniciantes Python (Python Wiki, 2022), trata-se de uma linguagem de programação orientada a objetos, clara e poderosa, comparável a Perl, Ruby, Scheme ou Java.

Python tem se mostrado uma linguagem muito eficiente e vem sendo amplamente adotada por profissionais na área de dados (Agarwal, 2023), destacando-se por sua sintaxe. Uma das principais filosofias de Guido van Rossum, o criador da linguagem, é que o código deve ser facilmente legível, uma vez que é lido com mais frequência do que é escrito. Isso é formalizado no **PEP 8**, o Guia de Estilo para Código Python, que estabelece as diretrizes para a formatação, organização e estruturação do código (Rossum; Warsaw; Coghlan, 2023). Seguir essas diretrizes resulta em um código que é considerado "pythonic" — ou seja, que adere aos princípios descritos no PEP 8. Essas regras abrangem elementos como a maneira com que o código é formatado, o modo pelo qual as funções são definidas e organizadas, a forma de aplicação da indentação e outros aspectos relacionados à sintaxe do código Python.

Já conseguiu entender por que o Python é tão usado e cada vez mais aplicado a todo tipo de programação? O próximo passo é saber como obtemos o Python, e é isso o que estudaremos a seguir!

### Ferramentas e interpretadores

Agora que temos um entendimento básico sobre essa linguagem essencial e sabemos que existe um conjunto de regras definido pelo PEP 8 para escrever o código Python de maneira consistente, a próxima pergunta que naturalmente surge é: onde exatamente escrevemos esses códigos em Python e de que forma visualizamos os resultados? A implementação de códigos em Python pode ser realizada em uma variedade de ambientes, seja no seu próprio computador ou em ambientes baseados na nuvem. No entanto, independentemente da escolha do ambiente, um elemento essencial nesse contexto é o uso de um **interpretador Python** para executar seus códigos.

O passo a passo para a instalação do interpretador Python está disponível no site oficial dessa linguagem, tanto para Windows (Python Brasil, 2019), quanto para outros sistemas operacionais (Python Brasil, 2023; Python Brasil, 2016).

Após a instalação, podemos utilizar o prompt de comando para fazer alguns testes e até mesmo programar com Python por lá. Porém aconselho utilizar uma **Integrated Development Environment (IDE)**, isto é, um Ambiente de Desenvolvimento Integrado. Existem várias IDEs que podem ser utilizadas e que são ótimas, como o **PyCharm** (JetBrains, 2010) e o **Visual Studio Code (VSCode)** (Microsoft, [s. d.]).

Outra ferramenta que se destaca nesse cenário é o **Python Anaconda** (Anaconda, [s. d.]), que possui diversos recursos Python, sendo composta por bibliotecas e IDEs. O diferencial é o **Jupyter Notebook**, um ambiente de computação iterativa que permite a criação de documentos de notebook que incluem código ativo, gráficos, textos narrativos, etc. Outra vantagem do Jupyter Notebook é a capacidade de funcionar em um navegador de internet. No endereço jupyter, você pode experimentar a ferramenta sem precisar de instalação.

A ferramenta que indico como meio de trabalho para esta disciplina é o **Google Colab**, pois essa plataforma possibilita que qualquer pessoa escreva e execute código Python a partir do navegador. O Colab é um servidor de Notebook Jupyter hospedado que não requer configuração para ser utilizado. Como é baseado no projeto de código aberto, permite que você use e compartilhe os Notebooks Jupyter com outros usuários sem precisar baixar, instalar ou executar nada.

Vamos nessa! Para usar o Colab, acesse: colab.

Fazendo uma pequena retrospectiva, é possível afirmar que já temos um entendimento básico do Python e de onde programar. Agora vamos praticar!

## Siga em Frente...

### Variáveis e tipos de dados

O fluxo de um algoritmo é a entrada, o processamento e a saída. Note que, para que o processamento ocorra, é necessário armazenar os valores da entrada, por exemplo. Assim surge o conceito de **variável**, que nada mais é do que um espaço alocado na memória RAM.

O interpretador Python consegue estabelecer o tipo de dado da variável observando seu valor. Confira alguns exemplos:

```python
x = 10
nome = 'aluno'
nota = 8.75
fez_inscricao = True
```

Observe que `x` é um número inteiro, `nome` é uma string, `nota` é um número decimal e `fez_inscricao` é um booleano. Será que Python é capaz de definir o tipo de variável somente com base no valor fornecido em cada variável?

Utilizaremos a função `print()` e `type()`.

```python
print(type(x))
print(type(nome))
print(type(nota))
print(type(fez_inscricao))
```

```text
<class 'int'>
<class 'str'>
<class 'float'>
<class 'bool'>
```

Como esperado, o Python acertou todos os tipos de variáveis. Note, também, que em Python tudo é objeto. Sendo assim, os tipos de dados aparecem com a palavra "class", que é uma classe.

Já conseguimos criar uma variável. Que tal melhorar o famoso "hello world"? Para isso, usaremos a função `input()`, que faz a leitura de um valor digitado.

```python
nome = input()
print(nome)
```

```text
Digite um nome: Estudante Querido
Estudante Querido
```

Ao executar o comando input, surge o campo para digitar o que será capturado – no nosso caso, "Estudante Querido". Logo após, a função `print()` mostra a variável `nome`. Vamos melhorar nosso "hello world"!

Existem muitas formas de imprimir textos e variáveis em Python. Usaremos formatadores de caracteres (igual em C) e a f-string.

```python
# formatadores de caracteres
print("Olá, %s, bem-vindo à disciplina de programação. Parabéns pelo seu primeiro hello world" % (nome))
```

```text
Olá, Estudante Querido, bem-vindo à disciplina de programação. Parabéns pelo seu primeiro hello world
```

```python
# f-string
print(f{nome}, bem-vindo à disciplina de programação. Parabéns pelo seu primeiro hello world")
```

```text
Olá, Estudante Querido, bem-vindo à disciplina de programação. Parabéns pelo seu primeiro hello world
```

De acordo com o PEP 498 (Smith, [s. d.]), a melhor opção é utilizar "f-string". Sendo assim, usaremos esse recurso em nossas aulas.

Esta etapa de aprendizagem consistiu em uma introdução básica do Python, suas respectivas ferramentas e alguns exemplos de uso. O objetivo desta aula era mostrar como surgiu a linguagem Python, onde conseguimos usá-la e como esse processo deve ser feito. Para concluir, a intenção final era deixar você curioso para aprender mais. Espero que isso tenha acontecido!

## Vamos Exercitar?

Você se lembra da minha pergunta inicial? É possível utilizar Python para automatizar as médias dos meus alunos? Depois de tudo o que vimos nesta aula, a resposta é sim!

```python
Nota_1 = int(input())
Nota_2 = int(input())
Nota_3 = int(input())
Nota_4 = int(input())

# observe que utilizamos a função int(), pois, sem ela, o Python entenderia que as notas seriam String

# condição para a aprovação do aluno.
if media >= 6:
    situacao =
else:
    situacao =

# dadas as notas, mostramos a média final e a situação do aluno.
print(f{media})
print(f{situacao})
```

Repare que utilizei duas funções condicionais:

- **`if >= 6`** (se a nota for maior ou igual a 6): aluno aprovado.
- **`else`** (se a nota for menor do que 6): aluno reprovado.

Essas funções são essenciais na programação. Estudaremos mais situações nas quais elas são aplicadas no decorrer desta disciplina.

Gostou dessa solução? Espero que sim! Agora, quero que você fique ainda mais curioso para aprender Python!

## Saiba mais

1. Uma leitura interessante para quem está começando a programar em Python é a do livro *Começando a programar em Python para leigos*, cujo link de acesso está disponível a seguir.
   > MUELLER, J. P. **Começando a programar em Python para leigos**. Rio de Janeiro: Alta Books, 2020. E-book.

2. Outra dica para estudo e aprofundamento sobre esse tema é o livro *Use a cabeça! Python*.
   > BARRY, P. **Use a Cabeça! Python**. 2. ed. Rio de Janeiro: Alta Books, 2018. E-book.

3. Para a aplicação e o conhecimento sobre o uso da linguagem Python no mercado financeiro, recomendo a leitura do livro *Python e mercado financeiro: programação para estudantes, investidores e analistas*.
   > CAETANO, M. A. L. **Python e mercado financeiro: programação para estudantes, investidores e analistas**. São Paulo: Blucher, 2021. E-book.

4. Por fim, também encorajo você a navegar pelos seguintes sites: python, jupyter e colab.

## Referências

- A ORIGEM do "Hello World". Ciência da Computação, 2015. Disponível em: https://cienciacomputacao.com.br/curiosidade/a-origem-do-hello-world/. Acesso em: 12 out. 2023.
- AGARWAL, A. From C to Python, and everything... LinkedIn, 2023. Disponível em: https://www.linkedin.com/feed/update/urn:li:activity:7056881167563702272/. Acesso em: 12 out. 2023.
- ANACONDA. Página inicial, [s. d.]. Disponível em: https://www.anaconda.com/. Acesso em: 12 out. 2023.
- BARRY, P. Use a Cabeça! Python. 2. ed. Rio de Janeiro: Alta Books, 2018. E-book. Disponível em: https://integrada.minhabiblioteca.com.br/#/books/9786555207842. Acesso em: 12 out. 2023.
- BEGINNER'S Guide. Python Wiki, 22 nov. 2022. Disponível em: https://wiki.python.org/moin/BeginnersGuide/Overview. Acesso em: 12 out. 2023.
- CAETANO, M. A. L. Python e mercado financeiro: programação para estudantes, investidores e analistas. São Paulo: Blucher, 2021. E-book. Disponível em: https://integrada.minhabiblioteca.com.br/#/books/9786555062410. Acesso em: 12 out. 2023.
- GOOGLE COLAB. Página inicial, [s. d.]. Disponível em: https://colab.research.google.com/. Acesso em: 12 out. 2023.
- HISTORY and license. Python v3.0.1 Documentation, [s. d.]. Disponível em: https://docs.python.org/3.0/license.html. Acesso em: 12 out. 2023.
- INSTALANDO o Python 3 no Linux. Python Brasil, 27 jun. 2023. Disponível em: https://python.org.br/instalacao-linux/. Acesso em: 12 out. 2023.
- INSTALANDO o Python 3 no Mac OS X. Python Brasil, 1 nov. 2016. Disponível em: https://python.org.br/instalacao-mac/. Acesso em: 12 out. 2023.
- INSTALANDO o Python 3 no Windows. Python Brasil, 30 nov. 2019. Disponível em: https://python.org.br/instalacao-windows/. Acesso em: 12 out. 2023.
- MUELLER, J. P. Começando a programar em Python para leigos. Rio de Janeiro: Alta Books, 2020. E-book. Disponível em: https://integrada.minhabiblioteca.com.br/#/books/9786555202298. Acesso em: 12 out. 2023.
- PYCHARM. JetBrains, 5 fev. 2010. Disponível em: https://www.jetbrains.com/pycharm/. Acesso em: 12 out. 2023.
- ROSSUM, G. V.; WARSAW, B.; COGHLAN, A. PEP 8 – Style Guide for Python Code. Python Enhancement Proposals, 9 dez. 2023. Disponível em: https://peps.python.org/pep-0008/#introduction. Acesso em: 12 fev. 2023.
- SMITH, E. V. PEP 498 – Literal String Interpolation. Python Enhancement Proposals, [s. d.]. Disponível em: https://peps.python.org/pep-0498/. Acesso em: 12 out. 2023.
- TRY JUPYTER. Jupyter, [s. d.]. Disponível em: https://jupyter.org/try. Acesso em: 12 out. 2023.
- VISUAL Studio. Microsoft, [s. d.]. Disponível em: https://visualstudio.microsoft.com/pt-br/. Acesso em: 12 out. 2023.
