# Aula 2 — Sets, Dicionários e Arrays NumPy em Python

## Ponto de Partida

Dando continuidade à nossa aprendizagem, nesta aula vamos aprofundar nossos conhecimentos sobre estruturas de objetos em Python.

O primeiro objeto a ser estudado é o do tipo **set** em Python. Um conjunto, ou set, é uma estrutura de dados que representa uma coleção de elementos únicos, sem repetição. Nesse sentido, descobriremos como criar, modificar e realizar operações com conjuntos.

O segundo objeto analisado será o do tipo mapping, com foco voltado ao **dicionário (dict)** em Python. Dicionários são estruturas que associam chaves a valores, permitindo o armazenamento e a recuperação eficiente de informações. Saberemos como criar dicionários, adicionar itens e efetuar operações de busca.

O terceiro objeto é do tipo array **NumPy**. O NumPy é uma biblioteca essencial para a computação científica em Python, fornecendo recursos avançados para manipular arrays multidimensionais. Entenderemos como criar, realizar operações e acessar elementos em arrays NumPy.

> Para estimular a compreensão desses conteúdos, suponha que você esteja gerenciando um evento científico para o qual participantes de diferentes regiões do mundo se inscreveram. Cada participante concedeu informações sobre sua localização, afiliação a instituições de pesquisa e áreas de interesse. O objetivo é desenvolver análises sobre a distribuição geográfica dos participantes, suas afiliações e as áreas de interesse predominantes. Como podemos utilizar os conhecimentos desta aula para resolver esse caso?

## Vamos Começar!

### Objetos do tipo set

A palavra "set", em Python, nos conduz diretamente à essência de uma estrutura de dados que se assemelha a conjuntos matemáticos. Os objetos do tipo "set" habilitam operações de conjuntos, como união, interseção, diferença e muitas outras. Essa estrutura é especialmente útil para realizar testes de associação e eliminar valores duplicados em uma sequência (PSF, 2020).

Além das operações familiares que já conhecemos para sequências, como `len(s)`, `x in s` e `x not in s`, os conjuntos oferecem funcionalidades adicionais.

Podemos agregar um novo elemento a um conjunto usando `add(valor)` e remover elementos com `remove(valor)`. Para explorar a lista completa de funções disponíveis, acesse: python.

Em Python, existem duas formas principais de criar objetos do tipo "set":

- Usando um par de chaves e elementos separados por vírgulas, por exemplo: `set1 = {'a', 'b', 'c'}`.
- Usando o construtor de tipo `set(iterable)` com um objeto iterável, como uma lista, uma tupla ou mesmo uma sequência de caracteres (string).

Confira, a seguir, um exemplo de criação de conjuntos:

```python
# Criando um conjunto vazio
meu_conjunto = set()

# Adicionando elementos ao conjunto
meu_conjunto.add(10)
meu_conjunto.add(20)
meu_conjunto.add(30)

# Imprimindo o conjunto
print("Conjunto após adicionar elementos:", meu_conjunto)

# Verificando se um elemento está no conjunto
elemento = 20

if elemento in meu_conjunto:
    print(f"{elemento} está no conjunto.")
else:
    print(f"{elemento} não está no conjunto.")

# Removendo um elemento do conjunto
meu_conjunto.remove(20)

# Imprimindo o conjunto atualizado
print("Conjunto após remover o elemento 20:", meu_conjunto)
```

Nesse código, criamos um conjunto vazio, chamado meu_conjunto, e adicionamos elementos a ele usando o método `add()`. Em seguida, verificamos se um elemento específico está no conjunto utilizando a instrução `in`. Por fim, removemos um elemento com o método `remove()` e imprimimos o conjunto atualizado. Conjuntos são úteis para armazenar valores únicos e efetuar operações de pertencimento.

### Objetos do tipo mapping

As estruturas de dados que estabelecem uma relação entre chaves e valores são conhecidas como objetos do tipo **mapping**. Em Python, o principal objeto que atende a essa propriedade é o dicionário, representado pelo tipo `dict`. Dicionários são mutáveis, o que significa que podemos modificar o valor associado a uma chave existente ou adicionar novas chaves.

Podemos criar dicionários em Python das seguintes maneiras:

- Usando um par de chaves para denotar um dicionário vazio: `dicionario1 = {}`.
- Usando pares de elementos na forma "chave: valor" separados por vírgulas: `dicionario2 = {'um': 1, 'dois': 2, 'três': 3}`.
- Usando o construtor de tipo `dict()`.

Observe, a seguir, alguns exemplos desses diferentes modos de criar um dicionário:

```python
# Exemplo 1 - Criação de um dicionário vazio, seguido de atribuição de chaves e valores
dici_1 = {}
dici_1['nome'] = "Maria"
dici_1['idade'] = 25

# Exemplo 2 - Criação de um dicionário com pares chave: valor
dici_2 = {'nome': 'Maria', 'idade': 25}

# Exemplo 3 - Criação de um dicionário com uma lista de tuplas representando pares chave: valor
dici_3 = dict([('nome', "Maria"), ('idade', 25)])

# Exemplo 4 - Criação de um dicionário usando a função built-in zip() e duas listas, uma para as chaves e outra para os valores
dici_4 = dict(zip(['nome', 'idade'], ["Maria", 25]))

# Teste se todas as construções resultam em objetos iguais
print(dici_1 == dici_2 == dici_3 == dici_4) # Deve imprimir True
print(dici_1)

#Resultado:
```

```text
True
{'nome': 'Maria', 'idade': 25}
```

Mostramos quatro maneiras distintas de criar dicionários e atribuir valores a eles. Para acessar um valor em um dicionário, use a notação `nome_dicionario[chave]`. Já para atribuir um novo valor, utilize `nome_dicionario[chave] = novo_valor`. Dicionários são úteis para armazenar informações associadas por chaves exclusivas.

## Siga em Frente...

### Objetos do tipo array NumPy

As estruturas de dados em Python abrangem uma ampla variedade de objetos e bibliotecas, cada qual projetado para funções específicas. Um recurso poderoso que se destaca nesse contexto é a biblioteca **NumPy**, desenvolvida para suportar a computação científica com Python. NumPy oferece uma vasta gama de funcionalidades, incluindo arrays multidimensionais e funções sofisticadas. Além disso, disponibiliza ferramentas para integração com código em C/C++ e Fortran, bem como recursos essenciais de álgebra linear, transformada de Fourier e geração de números aleatórios.

Para começar a utilizar o NumPy, é necessário instalá-lo no ambiente Python. Você pode fazer isso facilmente com o comando `pip install numpy`. Em plataformas como o Anaconda ou Google Colab, o NumPy já está incluído. Depois de instalado, você deve importar a biblioteca em seu projeto usando o comando `import numpy` sempre que quiser aproveitar seus recursos vantajosos.

A biblioteca NumPy é particularmente valiosa para cientistas de dados e desenvolvedores de soluções de inteligência artificial, pois permite lidar de maneira eficiente com matrizes de dados complexas e realizar operações avançadas. Se você estiver interessado em aprender mais sobre o NumPy, é interessante verificar a documentação completa dessa biblioteca em numpy.

Confira o código a seguir:

```python
# Importe a biblioteca NumPy
import numpy as np

# Crie um array NumPy de números inteiros
my_array = np.array([1, 2, 3, 4, 5])

# Imprima o array
print("Array original:")
print(my_array)

# Realize operações matemáticas com o array
squared_array = my_array ** 2 # Eleva cada elemento ao quadrado
sum_of_elements = np.sum(my_array) # Calcula a soma de todos os elementos

# Imprima os resultados
print("\nArray ao quadrado:")
print(squared_array)
print("\nSoma dos elementos:")
print(sum_of_elements)

# Acesse elementos do array
element_at_index_2 = my_array[2] # Acessa o elemento no índice 2
print("\nElemento no índice 2:", element_at_index_2)

#Resultado
```

```text
Array original:
[1 2 3 4 5]
Array ao quadrado:
[1 4 9 16 25]
Soma dos elementos:
15
Elemento no índice 2: 3
```

Nesse código, importamos o NumPy como np, criamos um array NumPy chamado my_array, realizamos operações matemáticas nele e acessamos elementos por índice. O NumPy oferece uma maneira eficiente de trabalhar com matrizes e executar operações em massa.

## Vamos Exercitar?

Agora, vamos colocar em prática o que aprendemos nesta aula para resolver nosso problema inicial. Como podemos usar conjuntos (sets) para identificar as diferentes regiões dos participantes do evento científico, dicionários para categorizar suas afiliações e arrays NumPy para analisar as áreas de interesse?

```python
# Importe as bibliotecas necessárias
import numpy as np

# Dados dos participantes
participantes = [
    {
        "nome": "Alice",
        "localizacao": "EUA",
        "afiliacao": "Universidade A",
        "interesses": ["Física", "Astronomia"]
    },
    {
        "nome": "Bob",
        "localizacao": "Brasil",
        "afiliacao": "Instituto B",
        "interesses": ["Biologia", "Astronomia"]
    },
    {
        "nome": "Charlie",
        "localizacao": "Índia",
        "afiliacao": "Instituto C",
        "interesses": ["Química", "Engenharia"]
    }
    # Adicione mais participantes conforme necessário
]

# Usando sets para identificar diferentes regiões dos participantes
regioes = set(participante["localizacao"] for participante in participantes)

# Usando um dicionário para categorizar afiliações
afiliacoes = {}

for participante in participantes:
    afiliacao = participante["afiliacao"]
    if afiliacao not in afiliacoes:
        afiliacoes[afiliacao] = []
    afiliacoes[afiliacao].append(participante["nome"])

# Usando NumPy para analisar áreas de interesse
areas_de_interesse = np.array([interesse for participante in participantes for interesse in participante["interesses"]])
interesses_unicos, contagem = np.unique(areas_de_interesse, return_counts=True)
area_mais_popular = interesses_unicos[np.argmax(contagem)]

# Resultados
print("Regiões dos participantes:", regioes)
print("Afiliações dos participantes:")
for afiliacao, nomes in afiliacoes.items():
    print(f"{afiliacao}: {', '.join(nomes)}")

print("Área de interesse mais popular:", area_mais_popular)

#Resultado:
```

```text
Regiões dos participantes: {'Índia', 'EUA', 'Brasil'}
Afiliações dos participantes:
Universidade A: Alice
Instituto B: Bob
Instituto C: Charlie
Área de interesse mais popular: Astronomia
```

Esse código usa conjuntos para identificar as diferentes regiões dos participantes, um dicionário para categorizar suas afiliações e o NumPy para avaliar as áreas de interesse. Os resultados são exibidos no final do código.

Gostou dessa solução? Espero que sim! Já estamos avançando bastante em nossa trajetória de estudos, desta vez utilizando bibliotecas do Python. Faça mudanças no código e pratique!

## Saiba mais

1. Para entender mais detalhes sobre o uso do NumPy, sugiro a leitura do artigo *Os principais setores de emprego na Mesorregião do Sul/Sudoeste de Minas: uma análise multivariada*, que exibe uma análise empírica quantitativa cujo objetivo foi verificar como se comportam os índices de empregabilidade utilizando Pyhton.
   > PAPANDRÉA, P. J.; PEREIRA, A. de S.; PAIVA, A. P. de. **Os principais setores de emprego na Mesorregião do Sul/Sudoeste de Minas: uma análise multivariada**. Produção Online, Florianópolis, SC, v. 22, n. 4, p. 3528-3554, 2022.

2. Para exercitar os conhecimentos aprendidos nesta aula, faça a leitura do livro *Python 3: conceitos e aplicações: uma abordagem didática*.
   > BANIN, S. L. **Python 3: conceitos e aplicações: uma abordagem didática**. São Paulo: Érica, 2018. E-book.

3. Outra dica para estudo e aprofundamento sobre esse tema é o livro *Use a cabeça! Python*.
   > BARRY, P. **Use a Cabeça! Python**. 2. ed. Rio de Janeiro: Alta Books, 2018. E-book.

## Referências

- BARRY, P. Use a Cabeça! Python. 2. ed. Rio de Janeiro: Alta Books, 2018. E-book. Disponível em: https://integrada.minhabiblioteca.com.br/#/books/9786555207842. Acesso em: 12 out. 2023.
- MANZANO, J. A. N. G.; OLIVEIRA, J. F. de. Algoritmos: lógica para desenvolvimento de programação de computadores. 29. ed. São Paulo: Érica, 2019.
- NUMPY. Página inicial, [s. d.]. Disponível em: https://numpy.org/. Acesso em: 21 out. 2023.
- PAPANDRÉA, P. J.; PEREIRA, A. de S.; PAIVA, A. P. de. Os principais setores de emprego na Mesorregião do Sul/Sudoeste de Minas: uma análise multivariada. Produção Online, Florianópolis, SC, v. 22, n. 4, p. 3528-3554, 2022. Disponível em: https://www.producaoonline.org.br/rpo/article/view/4716/2242. Acesso em: 21 out. 2023.
- TIPOS embutidos. Python 3.12.2 Documentation, [s. d.]. Disponível em: https://docs.python.org/pt-br/3/library/stdtypes.html. Acesso em: 21 out. 2023.
