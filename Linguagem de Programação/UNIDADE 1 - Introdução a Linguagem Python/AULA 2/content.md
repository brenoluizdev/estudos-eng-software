# Aula 2 — Operadores Relacionais, Estruturas Lógicas e Condicionais

## Ponto de Partida

Dando continuidade ao nosso aprendizado sobre Python, nesta aula vamos conhecer três conceitos fundamentais para a implementação de algoritmos.

O primeiro deles consiste em uma ferramenta de comparação: os **operadores relacionais**. Eles nos permitem avaliar relações entre valores, respondendo a perguntas como: "é maior que?", "é igual a?" ou "é diferente de?".

O segundo conceito é o de **estruturas lógicas**, que são como peças de quebra-cabeça responsáveis por unir condições para criar critérios mais complexos. São elas que nos possibilitam tomar decisões mais elaboradas, combinando várias comparações.

Já com o terceiro conceito, de **estruturas condicionais**, dizemos ao programa o que fazer com base na seguinte condição: "se isso for verdade, aja assim; caso contrário, faça aquilo".

> A partir desse conhecimento, faremos uma aplicação dos conceitos mencionados por meio de um estudo de caso. Suponha que você trabalhe em uma empresa que cuida de cinemas. Em uma reunião com a diretoria, foi solicitada a implementação de um sistema de autoatendimento. Como se trata de algo novo na rede, você será responsável por elaborar um protótipo simples. A diretoria quer que o projeto a ser desenvolvido seja baseado na idade dos clientes e contenha a informação de disponibilidade de ingressos.

Vamos nessa?

## Vamos Começar!

### Operadores relacionais

Na programação, a criação de algoritmos para resolver problemas envolve a capacidade de tomar decisões. Tais decisões são guiadas por uma técnica chamada "estrutura condicional" (Manzano; Oliveira, 2019). Pode-se entendê-la como a escolha de um caminho em uma cidade. Da mesma forma que ao dirigir na cidade você precisa decidir em quais ruas seguir para chegar ao seu destino, em um programa é necessário definir qual parte do código será executada em um determinado momento.

Nesse contexto, temos, na programação, os operadores relacionais (Quadro 1), que são usados para fazer comparações.

| Operação | Significado |
| --- | --- |
| `<` | Estritamente menor que |
| `<=` | Menor ou igual que |
| `>` | Estritamente maior que |
| `>=` | Maior ou igual que |
| `==` | Igual |
| `!=` | Diferente |
| `is` | Identidade do objeto |
| `is not` | Negação da identidade do objeto |

*Quadro 1 | Operadores relacionais. Fonte: adaptado de Python 3.12.2 Documentation ([s. d.]).*

Lembre-se de que já utilizamos um operador desse tipo na primeira aula quando estabelecemos a condição de que a média fosse maior ou igual a 6 para que o aluno recebesse a aprovação. A partir de agora, utilizaremos cada vez mais esses operadores para criar códigos mais robustos.

### Estruturas lógicas

Além dos operadores relacionais, que comparam valores, também utilizamos **operadores booleanos** para construir decisões mais complexas em programação. Os operadores booleanos ajudam a combinar diferentes condições e a orientar o fluxo do programa de acordo com a lógica desejada.

**Operador "E" (`and`)**

O operador "E" (`and`) permite a realização da operação lógica "E". Isso significa que, ao usar a expressão `(a and b)`, o resultado será "Verdadeiro" somente quando ambos os argumentos, "a" e "b", forem verdadeiros. Caso contrário, o resultado será "Falso".

**Operador "OU" (`or`)**

O operador "OU" (`or`) realiza a operação lógica "OU". Ao utilizar a expressão `(a or b)`, o resultado será "Verdadeiro" se pelo menos um dos argumentos, "a" ou "b", for verdadeiro. A expressão será "Falsa" apenas quando ambos os argumentos forem falsos.

**Operador "NÃO" (`not`)**

O operador "NÃO" (`not`) é responsável por inverter o valor do argumento. Ao aplicarmos a expressão `(not a)`, ela transformará "Verdadeiro" em "Falso", e vice-versa. Ou seja, se o argumento for verdadeiro, a operação o tornará falso, e, se for falso, a operação o tornará verdadeiro.

Esses operadores booleanos são essenciais para a criação de estruturas de decisão mais sofisticadas, pois possibilitam que os programas lidem com uma variedade de situações e critérios lógicos. São usados para controlar o fluxo de execução com base em condições complexas e, assim, tornam viável a elaboração de programas que tomam decisões de acordo com critérios específicos.

## Siga em Frente...

### Estruturas condicionais if, else e elif

No dia a dia, temos muitas escolhas a fazer, regras a seguir. Pense em você mesmo dirigindo. Se o semáforo está verde, você pode seguir; caso contrário, deve parar, pois está vermelho (desconsideraremos o amarelo por ora).

Esse contexto se relaciona com a estrutura `if... else` da seguinte maneira:

- A condição "se o semáforo estiver verde" é satisfeita (verdadeira), então você segue em frente (`if`).
- A condição "se o semáforo estiver vermelho" não é satisfeita (falsa), então você para (`else`).

Nese exemplo, assim como acontece na programação, se uma condição é atendida, o fluxo de execução segue um caminho (verdadeiro); caso contrário, segue outro caminho (falso). Os comandos `if` e `else` são como bifurcações em uma estrada, orientando o fluxo do programa com base nas condições estabelecidas.

O comando `elif`, em Python, é uma abreviação de "else if", sendo usado em estruturas condicionais para avaliar múltiplas condições em sequência. É frequentemente utilizado após um bloco `if` e antes de um bloco `else`. A ideia por trás do `elif` é permitir que você verifique várias condições em ordem e, quando uma delas for verdadeira, o bloco de código associado a essa condição será executado.

Confira, a seguir, uma explicação mais detalhada sobre o `elif`:

- **Avaliação em sequência**: quando um bloco `if` é usado, a condição é avaliada. Se a condição for verdadeira, o bloco de código dentro desse `if` é executado. No entanto, em muitos cenários, você deseja avaliar uma série de condições em sequência, e o `elif` permite esse processo.
- **Verificação múltipla**: após o bloco `if`, você pode usar um ou mais blocos `elif`, cada um com sua própria condição. O Python avalia essas condições em ordem, do topo para baixo. Assim que uma condição for verdadeira, o bloco de código associado a essa condição será executado e as condições subsequentes serão ignoradas.
- **Flexibilidade**: o `elif` é flexível porque permite que você trate de múltiplos casos sem precisar aninhar uma série de blocos `if`. Isso torna o código mais legível e eficiente.

Para resumir o que analisamos até agora, imagine que estejamos construindo uma máquina de venda automática de refrigerantes.

Os operadores relacionais são como os sensores que verificam se você inseriu a moeda correta ou não. Eles nos ajudam a determinar se a condição foi atendida (por exemplo: "a moeda é maior ou igual a R$1,00?").

As estruturas lógicas podem ser comparadas às engrenagens dessa máquina. Elas nos permitem combinar vários sensores para fazer verificações complexas (por exemplo: "se a moeda é maior ou igual a R$1,00 e o refrigerante está disponível, então a máquina entrega um refrigerante").

As estruturas condicionais são como as instruções para a máquina, pois nos permitem dizer o que a máquina deve fazer com base nas verificações. Se a máquina detectar que a moeda é suficiente (usando operadores relacionais e estruturas lógicas), ela seguirá as instruções para entregar o refrigerante. Caso contrário, talvez exiba uma mensagem de erro.

Então, assim como um engenheiro monta uma máquina de venda automática usando diferentes peças e sensores para tomar decisões, nós montamos nossos programas utilizando operadores relacionais, estruturas lógicas e estruturas condicionais para controlar o fluxo e a lógica do código.

Sendo assim, vamos verificar o exemplo de código a seguir. Fique à vontade para pensar, criar e executar códigos utilizando as regras apresentadas nesta aula.

```python
idade = 25

if idade < 18:
    print("Menor de idade")
elif idade >= 18 and idade < 65:
    print("Adulto")
else:
    print("Idoso")
```

No exemplo anterior, usamos os três tipos de ferramentas que conhecemos durante esta etapa de aprendizagem. Repare na estrutura do `if`, `elif` e `else`. Ao final, definimos o que será feito com ":". Além disso, utilizamos operadores relacionais e o `and` para combinar duas condições.

Nesta aula, aprendemos sobre três tipos de ferramentas essenciais para criar algoritmos em Python. Com base nesse novo conhecimento, você já se tornará capaz de produzir algoritmos mais elaborados. A prática é vital para aprender cada vez mais, então espero que você pratique bastante!

## Vamos Exercitar?

Agora, vamos colocar em prática um algoritmo de recomendação para um cinema, baseando-se na idade do cliente. Suponha que tenhamos três filmes por semana, cada um com uma faixa etária específica. O primeiro é direcionado para menores de 12 anos; o segundo, para maiores ou iguais a 12 anos e menores de 18; por fim, o terceiro filme é recomendado para maiores ou iguais a 18 anos. Outro ponto solicitado pela diretoria do cinema diz respeito à disponibilidade de ingressos. Vamos para o código!

```python
# Bem-vindo à Máquina de Venda Automática de Ingressos de Cinema!

# Solicita a idade do cliente
idade = int(input("Por favor, digite sua idade: "))

# Verifica a idade para sugestão de filmes
if idade < 12:
    print("Recomendamos o filme infantil FILME 1.")
elif 12 <= idade < 18:
    print("Recomendamos o filme adolescente FILME 2.")
else:
    print("Recomendamos o emocionante FILME 3.")

# Verifica a disponibilidade de ingressos
quantidade_ingressos = 10 # Suponha que haja 10 ingressos disponíveis

if quantidade_ingressos > 0:
    print("Ingressos estão disponíveis. Divirta-se no cinema!")
else:
    print("Desculpe, todos os ingressos estão esgotados para hoje.")
```

Rode esse código no seu Google Colab e faça testes, substitua a disponibilidade de ingresso, insira idades diferentes... Enfim, "brinque" com ele.

Gostou dessa solução? Espero que sim! Esta é a nossa segunda aula e já construímos um modelo de recomendação. Vamos seguir cada vez mais fundo nesse mundo de Python!

## Saiba mais

1. Para descobrir mais detalhes sobre sistemas de recomendação, é interessante que você leia o artigo *Arquitetura de sistemas de recomendação para apoio ao vendedor no uso de sistemas de força de vendas em empresa com grande portfólio de produtos*, que mostra algumas aplicações e explica como funciona a utilização de tais modelos. Para acessar o conteúdo sugerido, clique no link disponível a seguir.
   > OHASHI, F. K. et al. Arquitetura de sistemas de recomendação para apoio ao vendedor no uso de sistemas de força de vendas em empresa com grande portfólio de produtos. Revista Ibérica de Sistemas e Tecnologias de Informação, Lousada, n. 42, p. 46-61, jun. 2021.

2. Uma leitura interessante para quem está começando a programar em Python é a do livro *Começando a programar em Python para leigos*.
   > MUELLER, J. P. **Começando a programar em Python para leigos**. Rio de Janeiro: Alta Books, 2020. E-book.

3. Outra dica para estudo e aprofundamento sobre esse tema é o livro *Use a cabeça! Python*.
   > BARRY, P. **Use a Cabeça! Python**. 2. ed. Rio de Janeiro: Alta Books, 2018. E-book.

## Referências

- BARRY, P. Use a Cabeça! Python. 2. ed. Rio de Janeiro: Alta Books, 2018. E-book. Disponível em: https://integrada.minhabiblioteca.com.br/#/books/9786555207842. Acesso em: 12 out. 2023.
- BUILT-IN Types. Python 3.12.2 Documentation, [s. d.]. Disponível em: https://docs.python.org/3/library/stdtypes.html. Acesso em: 14 out. 2023.
- MANZANO, J. A. N. G.; OLIVEIRA, J. F. de. Algoritmos: lógica para desenvolvimento de programação de computadores. 29. ed. São Paulo: Érica, 2019.
- MUELLER, J. P. Começando a programar em Python para leigos. Rio de Janeiro: Alta Books, 2020. E-book. Disponível em: https://integrada.minhabiblioteca.com.br/#/books/9786555202298. Acesso em: 12 out. 2023.
- OHASHI, F. K. et al. Arquitetura de sistemas de recomendação para apoio ao vendedor no uso de sistemas de força de vendas em empresa com grande portfólio de produtos. Revista Ibérica de Sistemas e Tecnologias de Informação, Lousada, n. 42, p. 46-61, jun. 2021. Disponível em: https://scielo.pt/pdf/rist/n42/1646-9895-rist-42-46.pdf. Acesso em: 14 out. 2023.
