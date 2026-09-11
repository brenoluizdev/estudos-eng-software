# Aula 1 — Sequências, Listas e Tuplas em Python

## Ponto de Partida

Em Python, a premissa fundamental é a de que tudo gira em torno de objetos. De acordo com a Python Software Foundation (PSF), todos os dados em um programa Python são representados por objetos ou pela relação entre objetos. Conheceremos, nesta aula, três estruturas de dados: **sequência**, **lista** e **tuplas**.

Sequências são estruturas de dados que nos permitem armazenar coleções ordenadas de informações. As listas consistem em uma forma fundamental de objetos do tipo sequência e são mutáveis, o que significa que nesse caso podemos adicionar, remover e alterar elementos. Já as tuplas são praticamente semelhantes às listas, mas com uma diferença crucial: elas são imutáveis. Isso significa que, uma vez criadas, as tuplas não podem ser alteradas.

> Para contextualizar sua aprendizagem, imagine a seguinte situação: você está gerenciando a lista de convidados de uma festa e a lista de pessoas que confirmaram a presença no evento. Você deseja identificar as pessoas que ainda não confirmaram presença, a fim de convidá-las novamente.

## Vamos Começar!

### Objetos do tipo sequência

Os objetos do tipo sequência são como coleções versáteis que podem armazenar vários valores. Eles servem para organizar dados em uma ordem específica e são indexados por números inteiros não negativos. O primeiro elemento da sequência é acessado pelo índice `0`, o segundo, pelo índice `1`, e assim por diante, até o último elemento, que está na posição `n - 1`, onde `n` representa a capacidade de armazenamento da sequência. O grupo de estruturas de dados que se encaixam nessa categoria compartilha algumas operações comuns. Observe o Quadro 1, a seguir.

| Operação | Resultado |
|---|---|
| `x in s` | True caso um item de s seja igual a x, senão false. |
| `s + t` | Concatenação de s e t. |
| `n * s` | Adiciona s a si mesmo n vezes. |
| `s[i]` | Acessa o valor guardado na posição i da sequência. |
| `s[i:j]` | Acessa os valores da posição i até j. |
| `s[i:j:k]` | Acessa os valores da posição i até j, com passo k. |
| `len(s)` | Comprimento de s. |
| `min(s)` | Menor valor de s. |
| `max(s)` | Maior valor de s. |
| `s.count(x)` | Número total de ocorrência de x em s. |

*Quadro 1 | Operações em comum dos objetos do tipo sequência. Fonte: adaptado de PSF.*

Um texto, representado por objetos da classe `str` (strings), é uma forma de sequência. Essas strings oferecem uma variedade de operações, como as descritas no Quadro 1, apresentado anteriormente. No entanto, é importante notar que as strings são objetos imutáveis, o que significa que não é possível modificar seu conteúdo atribuindo um novo valor a uma posição específica. Vamos, agora, experimentar algumas dessas operações. Confira o código a seguir.

```python
texto = "Explorando a diversidade de linguagens de programação com Pyhton."

print(f"Tamanho do texto = {len(texto2)}")
print(f"Python in texto = {'Python' in texto2}")
print(f"Quantidade de e no texto = {texto2.count('e')}")
print(f"As 5 primeiras letras são: {texto2[:5]}")

#resultado
```

```text
Tamanho do texto = 62
Python in texto = False
Quantidade de e no texto = 6
As 5 primeiras letras são: Explo
```

Na primeira demonstração, exploramos várias operações que podem ser aplicadas a sequências. A função `len()` revela o tamanho da sequência, enquanto o operador `in` permite verificar a presença de um valor na sequência. Com o operador `count`, é possível determinar quantas vezes um valor específico aparece na sequência. Além disso, usando a notação de colchetes, podem-se extrair partes específicas da sequência, como demonstrado na linha 6, onde solicitamos a exibição dos elementos da posição 0 até 5, excluindo o valor na posição 6.

A classe `str` (strings) vai além das operações listadas no Quadro 1, sugerindo uma série de outros métodos úteis. O site da Python Software Foundation (PSF) contém uma lista completa dessas funções para objetos `str`.

### Listas

As **listas** são estruturas de dados em Python conhecidas por sua mutabilidade, o que significa que você pode adicionar ou remover elementos conforme necessário. São estruturas indexadas, ou seja, cada elemento tem uma posição, começando em 0.

Considere o código a seguir, no qual criamos uma lista chamada "cores" e, em seguida, usamos uma estrutura de repetição para imprimir cada elemento junto com seu índice. Observe a função `index`, que retorna à posição de um valor na lista.

```python
cores = ['vermelho', 'azul', 'verde', 'amarelo', 'roxo']

for cor in cores:
    print(f'Posição = {cores.index(cor)}, cor = {cor}')

#resultado
```

```text
Posição = 0, cor = vermelho
Posição = 1, cor = azul
Posição = 2, cor = verde
Posição = 3, cor = amarelo
Posição = 4, cor = roxo
```

As **list comprehensions**, ou listcomps, são uma abordagem pythônica para criar listas com base em objetos iteráveis. Essa técnica é especialmente útil quando você deseja transformar ou filtrar as informações de uma sequência existente para construir uma nova sequência com as informações desejadas. Para ilustrar essa técnica, vamos considerar um exemplo no qual temos uma lista de palavras e queremos convertê-las em letras minúsculas. Acompanhe o código a seguir:

```python
linguagens = ["Python", "Java", "JavaScript", "C", "C#", "C++", "Swift", "Go", "Kotlin"]

print("Antes da listcomp = ", linguagens)

linguagens = [item.lower() for item in linguagens]

print("\nDepois da listcomp = ", linguagens)

#resultado
```

```text
Antes da listcomp = ['Python', 'Java', 'JavaScript', 'C', 'C#', 'C++', 'Swift', 'Go', 'Kotlin']
Depois da listcomp = ['python', 'java', 'javascript', 'c', 'c#', 'c++', 'swift', 'go', 'kotlin']
```

No exemplo apresentado anteriormente, criamos a lista "linguagens", que contém várias linguagens de programação. Em seguida, aplicamos uma list comprehension. No interior dos colchetes, utilizamos a variável "item" para representar cada elemento da lista original. Com a expressão "item.lower()", transformamos cada elemento em minúsculas e substituímos os valores originais na mesma variável "linguagens". Por fim, imprimimos a lista antes e depois da aplicação da list comprehension.

Agora, vamos explorar as funções `map()` e `filter()` em Python, que são usadas para manipular listas e aplicar transformações ou filtragens a elementos iteráveis. Primeiro, vou apresentar exemplos diferentes para cada função.

Suponha que você tenha uma lista de preços em dólares e deseje convertê-los para reais usando uma taxa de câmbio fixa:

```python
precos_em_dolares = [100, 50, 75, 120]
taxa_de_cambio = 5.25

precos_em_reais = list(map(lambda x: x * taxa_de_cambio, precos_em_dolares))
print(precos_em_reais)

#Resultado: [525.0, 262.5, 393.75, 630.0]
```

Nesse caso, usamos a função `map()` para aplicar uma função `lambda` que multiplica cada preço em dólares pela taxa de câmbio. Depois, convertemos o resultado em uma lista. O resultado será uma lista com os preços em reais.

Agora, imagine que você tenha uma lista de números e queira filtrar apenas os números pares:

```python
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))
print(numeros_pares)

#Resultado: [2, 4, 6, 8, 10]
```

Nesse exemplo, usamos a função `filter()` com uma função `lambda` que verifica se um número é par (resto da divisão por 2 igual a 0) e, em seguida, convertemos o resultado em uma lista. O resultado será uma lista contendo apenas os números pares.

## Siga em Frente...

### Tuplas

As **tuplas** são estruturas de dados pertencentes ao grupo de objetos do tipo sequência em Python. A principal distinção entre listas e tuplas é o fato de que as listas são mutáveis, permitindo a atribuição de valores a posições específicas, enquanto as tuplas são objetos imutáveis.

Você pode criar tuplas em Python de três maneiras:

- Usando um par de parênteses para denotar uma tupla vazia: `tupla1 = ()`.
- Usando um par de parênteses e elementos separados por vírgulas: `tupla2 = ('a', 'b', 'c')`.
- Usando o construtor de tipo `tuple()`.

Confira, a seguir, um exemplo no qual criamos uma tupla chamada "vogais" e, posteriormente, usamos uma estrutura de repetição para imprimir cada elemento da tupla, juntamente com sua posição:

```python
vogais = ('a', 'e', 'i', 'o', 'u')

print(f"Tipo do objeto vogais = {type(vogais)}")

for p, x in enumerate(vogais):
    print(f"Posição = {p}, valor = {x}")

#Resultado:
```

```text
Tipo do objeto vogais = <class 'tuple'>
Posição = 0, valor = a
Posição = 1, valor = e
Posição = 2, valor = i
Posição = 3, valor = o
Posição = 4, valor = u
```

Nesse exemplo, utilizamos a função `enumerate()` para obter tanto a posição quanto o valor de cada elemento na tupla. É importante observar que as tuplas são imutáveis, o que significa que, uma vez criadas, não é possível alterar seu conteúdo. Isso as torna úteis em situações nas quais a ordem dos elementos deve permanecer inalterada. Além disso, as tuplas têm um papel fundamental em várias operações em Python, como no desempacotamento de valores e no retorno múltiplo de funções.

## Vamos Exercitar?

Vamos, agora, colocar em prática o que aprendemos pensando no problema apresentado no início desta aula. Cada venda é registrada como uma tupla com os seguintes elementos: data da venda, nome do produto, quantidade vendida e preço unitário. Essas tuplas são armazenadas em uma lista chamada registros_de_vendas. Além disso, você recebeu uma lista de produtos que precisam ser reabastecidos no estoque, chamada produtos_a_reabastecer. Também é preciso acompanhar o total de vendas de cada produto. Para fazer isso, você deve criar um dicionário chamado total_de_vendas_por_produto, no qual as chaves são os nomes dos produtos, e os valores são os totais de vendas para cada um. Vamos ao código!

```python
# Tupla de convidados
convidados = ("Alice", "Bob", "Carol", "David", "Eve")

# Lista de confirmações
confirmados = ["Bob", "David"]

# Identificar quem ainda não confirmou
nao_confirmados = [convidado for convidado in convidados if convidado not in confirmados]

# Exibir os convidados que ainda não confirmaram
print("Convidados que ainda não confirmaram:")
for pessoa in nao_confirmados:
    print(pessoa)

# Enviar lembretes aos não confirmados
print("\nEnviando lembretes para os convidados que ainda não confirmaram.")

#Resultado:
```

```text
Convidados que ainda não confirmaram:
Alice
Carol
Eve
Enviando lembretes para os convidados que ainda não confirmaram.
```

Nesse código, temos uma tupla de convidados e uma lista de pessoas que confirmaram. Usamos tupla, lista e uma compreensão de lista (list comprehension) para identificar as pessoas que ainda não confirmaram. Em seguida, exibimos os nomes dessas pessoas e, opcionalmente, podemos enviar lembretes a elas. Essa situação utiliza objetos do tipo sequência (listas e tuplas) para resolver um problema prático.

Espero que você tenha gostado da solução. Lembre-se: a prática é importante! Mude alguma parte desse código e diversifique seu conhecimento!

## Saiba mais

1. Para exercitar os conhecimentos aprendidos nesta aula, faça a leitura do livro *Python 3: conceitos e aplicações: uma abordagem didática*, cujo link de acesso está disponível a seguir.
   > BANIN, S. L. **Python 3: conceitos e aplicações: uma abordagem didática**. São Paulo: Érica, 2018. E-book.

2. Como mencionado anteriormente, uma leitura interessante para quem está começando a programar em Python é a do livro *Começando a programar em Python para leigos*.
   > MUELLER, J. P. **Começando a programar em Python para leigos**. Rio de Janeiro: Alta Books, 2020. E-book.

3. Também encorajo você a navegar pelo site Python, que contém documentações e definições sobre as ferramentas de Python.

## Referências

- 5. ESTRUTURAS de dados. Python 3.12.2 Documentation, 9 dez. 2019. Disponível em: https://docs.python.org/pt-br/3/tutorial/datastructures.html. Acesso em: 21 out. 2023.
- BANIN, S. L. Python 3: conceitos e aplicações: uma abordagem didática. São Paulo: Érica, 2018. E-book. Disponível em: https://integrada.minhabiblioteca.com.br/books/9788536530253. Acesso em: 21 out. 2023.
- BARRY, P. Use a Cabeça! Python. 2. ed. Rio de Janeiro: Alta Books, 2018. E-book. Disponível em: https://integrada.minhabiblioteca.com.br/#/books/9786555207842. Acesso em: 12 out. 2023.
- MANZANO, J. A. N. G.; OLIVEIRA, J. F. de. Algoritmos: lógica para desenvolvimento de programação de computadores. 29. ed. São Paulo: Érica, 2019.
- MUELLER, J. P. Começando a programar em Python para leigos. Rio de Janeiro: Alta Books, 2020. E-book. Disponível em: https://integrada.minhabiblioteca.com.br/#/books/9786555202298. Acesso em: 21 out. 2023.
- PSF landing. Python Software Foundation, 12 dez. 2023. Disponível em: https://www.python.org/psf-landing/. Acesso em: 21 fev. 2024.
