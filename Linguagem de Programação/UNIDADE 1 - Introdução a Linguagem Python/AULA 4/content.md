# Aula 4 — Funções em Python: Built-in, Definidas pelo Usuário e Lambda

## Ponto de Partida

Python é uma linguagem de programação de alto nível amplamente usada na indústria de tecnologia. Nesta aula, você começará a entender por que a Python é tão popular e como pode ser utilizada em diversas aplicações.

Você conhecerá as ferramentas necessárias para dar início à programação em Python, o que inclui a instalação do Python em seu computador e a seleção de um ambiente de desenvolvimento adequado.

As variáveis são fundamentais na programação, pois permitem armazenar e manipular dados. Durante esta etapa de estudos, você aprenderá a criar variáveis e descobrirá os diferentes tipos de dados disponíveis em Python.

> Você se lembra da nossa primeira aula, quando pedi a ajuda da Python para calcular a média e mostrar a situação dos alunos? Vamos melhorar nosso cálculo com os conhecimentos de hoje!

## Vamos Começar!

### Funções built-in em Python

Desde o momento em que iniciamos nossa jornada na programação com a simples linha de código "print("hello world")", já estávamos explorando **funções**. O que é uma função? No contexto de Python, pense em funções como ferramentas prontas para uso. Elas são como blocos de construção pré-instalados, incorporados ao coração da linguagem Python, sem a necessidade de instalação adicional. A Python oferece uma ampla variedade de funções embutidas que podem ser utilizadas em suas tarefas de programação.

No site python constam todas as funções prontas existentes em Python. Acredito que seja muito importante você acessar essa página e conhecer as funções. Já utilizamos algumas delas em nossos estudos, como a função `print`, que exibe objeto no formato de texto.

Outra função que exploramos foi a `int`, que retorna um objeto inteiro a partir de um número ou string. Também usamos a função `range`, que nada mais é do que um tipo de sequência imutável.

Confira, a seguir, o exemplo que utiliza a função built-in `len()` para calcular o comprimento de uma lista e, em seguida, imprime o resultado com comentários explicativos:

```python
# Cria uma lista de números
numeros = [1, 2, 3, 4, 5]

# Usa a função len() para calcular o comprimento da lista
comprimento = len(numeros)

# Imprime o comprimento da lista
print(, comprimento)
```

Nesse caso, criamos uma lista chamada "números", com cinco elementos. Em seguida, usamos a função `len()` para calcular o comprimento dessa lista e armazenamos o resultado na variável "comprimento". Por fim, imprimimos o valor do comprimento com uma mensagem explicativa.

```text
O comprimento da lista é: 5
```

Como já foi mencionado, é interessante que você faça mais testes e aplicações das funções, na intenção de praticar o conhecimento estudado.

### Função definida pelo usuário (com retorno e parâmetro)

O repertório de 70 funções built-in (pré-construídas) da Python torna a vida do programador mais fácil. No entanto, cada problema é singular e frequentemente requer abordagens específicas. É nesse contexto que surge a necessidade de criar nossas próprias funções. Tais funções são pedaços de código que executam ações definidas por nós, os desenvolvedores. Temos o controle sobre o nome da função, os dados que ela recebe e o resultado que produz. Isso nos permite personalizar soluções para atender às demandas específicas de nossos projetos.

Acompanhe o exemplo de uma função que calcula a soma de dois números:

```python
# Definindo uma função chamada "soma"
def soma(a, b):
    resultado = a + b
    return resultado

# Chamando a função e armazenando o resultado em uma variável
resultado_soma = soma(5, 3)

# Imprimindo o resultado
print(, resultado_soma)

#resultado
```

```text
A soma de 5 e 3 é: 8
```

Nesse exemplo, definimos uma função chamada "soma", que aceita dois argumentos: `a` e `b`. Dentro da função, realizamos a operação de adição entre esses dois números e retornamos o resultado. Em seguida, chamamos a função com os valores 5 e 3, e armazenamos o resultado retornado em uma variável chamada "resultado_soma". Por fim, imprimimos o resultado.

Outro exemplo interessante de ser observado é a criação de uma função para definir se um número é par:

```python
# Definindo uma função chamada "e_par"
def e_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
```

Repare que definimos a função e utilizamos o operador `%`, que, em Python, é conhecido como operador de módulo ou operador de resto. Ele é usado para calcular o resto da divisão de um número pelo outro. Em uma expressão como `a % b`, o operador `%` retorna o valor do resto quando `a` é dividido por `b`.

Sendo assim, se um número é dividido por 2 e tem resto zero, então esse número é par.

Vamos testar essa função para dois valores: 123.120 e 1.355.989.

```python
# Testando a função
numero = 123120

if e_par(numero):
    print(f{numero} é um número par.")
else:
    print(f{numero} não é um número par.")

#resultado: 123120 é um número par.
```

```python
# Testando a função
numero = 1355989

if e_par(numero):
    print(f{numero} é um número par.")
else:
    print(f{numero} não é um número par.")

#resultado 1355989 não é um número par.
```

Note que a função retornou que o primeiro número é par e o segundo, não. Nesses exemplos, percebemos como é feita uma função definida por nós. Agora, faça testes e utilize sua imaginação para criar funções.

## Siga em Frente...

### Funções anônimas em Python

Dentro do universo das funções em Python, existe um recurso poderoso chamado "expressão **lambda**". As expressões lambda são usadas para criar funções anônimas, o que significa que elas não têm um nome definido com `def`. Tais funções são úteis quando você precisa de uma ação simples que será utilizada apenas uma vez. Para saber mais detalhes sobre esse recurso, acesse: python (Python 3.12.2 Documentation, [s. d.]b).

Confira um exemplo:

```python
soma = lambda a, b: a + b

resultado = soma(3, 4)

print(resultado) # Isso imprimirá 7

#resultado: 7
```

Nesse exemplo, criamos uma expressão lambda que realiza a adição de dois números: `a` e `b`. Não atribuímos um nome à função, mas podemos usá-la como qualquer outra. Portanto, expressões lambda são úteis em situações nas quais precisamos de uma função pequena e simples para uma tarefa específica.

Até agora, conhecemos as funções prontas do Python e descobrimos como podemos desenvolver nossas próprias funções, seja de forma mais visual (quando utilizamos `def`), seja de forma anônima (usando `lambda`).

## Vamos Exercitar?

Já sabemos como calcular médias. Vamos, a partir de agora, dar um upgrade no primeiro código com o qual trabalhamos utilizando o conhecimento obtido nesta aula.

```python
# Lista de notas dos estudantes
notas = [7.5, 8.0, 6.5, 9.0, 7.0]

# Função regular para calcular a média
def calcular_media(notas):
    total = sum(notas)
    media = total / len(notas)
    return media

# Função lambda para arredondar a média para duas casas decimais
arredondar_media = lambda media: round(media, 2)

# Calcular a média
media = calcular_media(notas)
media_arredondada = arredondar_media(media)

# Verificar se os estudantes foram aprovados
situacao = if media_arredondada >= 7 else

# Resultados
print(, notas)
print(, media_arredondada)
print(, situacao)
```

Esse código calcula a média das notas dos estudantes, arredonda o resultado e determina se eles foram aprovados ou reprovados com base na média.

Trata-se, portanto, de um exemplo prático de uso de funções e estruturas condicionais, já que utilizamos funções prontas como `sum`, `len` e `round`, e criamos funções definidas e anônimas.

Elaboramos, na primeira aula, um código simples para calcular a média. Agora, no final desta unidade de aprendizagem, conseguimos criar nossas próprias funções e utilizar muitas ferramentas de Python!

Você se sentirá cada vez mais preparado para criar algoritmos mais robustos e aplicá-los a diversas realidades. Lembre-se de sempre praticar!

## Saiba mais

1. Uma leitura interessante para quem está começando a programar em Python é a do livro *Começando a programar em Python para leigos*.
   > MUELLER, J. P. **Começando a programar em Python para leigos**. Rio de Janeiro: Alta Books, 2020. E-book.

2. Outra dica para estudo e aprofundamento sobre esse tema é o livro *Use a cabeça! Python*.
   > BARRY, P. **Use a Cabeça! Python**. 2. ed. Rio de Janeiro: Alta Books, 2018. E-book.

3. Para saber mais detalhes sobre a aplicação da linguagem Python, sugiro a leitura do texto *Normalização de dados textuais com Python*.
   > TURKEL, J.; CRYMBLE, A. **Normalização de dados textuais com Python**. The Programming Historian, 17 jul. 2012.

## Referências

- 6. EXPRESSIONS. Python 3.12.2 Documentation, [s. d.]b. Disponível em: https://docs.python.org/3/reference/expressions.html#lambda. Acesso em: 12 out. 2023.
- BARRY, P. Use a Cabeça! Python. 2. ed. Rio de Janeiro: Alta Books, 2018. E-book. Disponível em: https://integrada.minhabiblioteca.com.br/#/books/9786555207842. Acesso em: 12 out. 2023.
- BUILT-IN Functions. Python 3.12.2 Documentation, [s. d.]a. Disponível em: https://docs.python.org/3/library/functions.html. Acesso em: 12 out. 2023.
- MUELLER, J. P. Começando a programar em Python para leigos. Rio de Janeiro: Alta Books, 2020. E-book. Disponível em: https://integrada.minhabiblioteca.com.br/#/books/9786555202298. Acesso em: 12 out. 2023.
- TURKEL, J.; CRYMBLE, A. Normalização de dados textuais com Python. The Programming Historian, 17 jul. 2012. Disponível em: https://programminghistorian.org/pt/licoes/normalizacao-dados-textuais-python. Acesso em: 12 out. 2023.
