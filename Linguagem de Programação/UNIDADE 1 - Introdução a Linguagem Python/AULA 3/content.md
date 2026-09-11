# Aula 3 — Estruturas de Repetição e Controle de Repetição

## Ponto de Partida

Avançando ainda mais em nossos estudos sobre Python, vamos conhecer, nesta aula, estruturas de repetição e de controle que são essenciais para a implementação de algoritmos.

Na intenção de simplificar tarefas repetitivas, você estudará o `for`, uma estrutura de repetição que permite percorrer uma sequência de elementos, como uma lista, e executar ações para cada item.

Já para controlar as repetições ou ter uma condição atendida, o `while` é a estrutura ideal. Nesta etapa de aprendizagem, você investigará o uso dessa ferramenta e entenderá por que sua implementação é essencial em certos algoritmos.

Para finalizar, você conhecerá as funções `range`, `break` e `continue`. Tais ferramentas também são usadas para controle de repetição. Ao final desta aula, você será capaz de definir a melhor opção a ser adotada para um determinado caso.

> Suponha, agora, que você, ainda trabalhando no cinema do estudo de caso da aula passada, precise verificar a aceitação de cinco filmes exibidos no mês. Para tanto, será necessário criar um algoritmo que seja capaz de classificar os filmes de 1 a 5 estrelas. Como posso utilizar estruturas de repetição e controle de repetição para elaborar esse algoritmo?

## Vamos Começar!

### Estrutura de repetição for

A estrutura de repetição `for`, em Python, é uma poderosa ferramenta que nos permite realizar ações repetitivas de maneira controlada (Manzano; Oliveira, 2019). Em um loop `for`, especificamos um conjunto de elementos (por exemplo, uma lista ou uma sequência) e, em seguida, o código é executado para cada elemento desse conjunto. Tal estrutura é especialmente útil quando sabemos previamente quantas vezes queremos repetir uma ação ou quando temos uma coleção de itens a serem processados.

Confira, a seguir, o exemplo simples de um loop `for` que itera por uma lista de números e imprime cada número:

```python
numeros = [1, 2, 3, 4, 5]

for numero in numeros:
    print(numero)
```

Nesse exemplo, a variável 'numero' assume o valor de cada elemento da lista 'numeros' em sequência, e o bloco de código dentro do loop é executado para cada valor. Isso resultará na impressão dos números de 1 a 5.

```text
1
2
3
4
5
```

O loop `for` é uma ferramenta eficaz para automatizar tarefas repetitivas e processar coleções de dados de modo eficiente.

### Estrutura de repetição while

O comando `while` é uma ferramenta muito importante na programação Python, sendo usado para criar estruturas de repetição quando o número de repetições não é conhecido antecipadamente. Ele permite que um bloco de código seja executado repetidamente enquanto uma condição especificada for verdadeira. Isso torna o `while` ideal para situações em que a execução deve continuar até que uma condição específica seja atendida.

Acompanhe, a seguir, um exemplo simples de uso do `while` para verificar se um número inserido pelo usuário é par ou ímpar e encerrar o programa quando o número zero for inserido:

```python
1 numero = int(input()
2
3 while numero != 0:
4     if numero % 2 == 0:
5         print()
6     else:
7         print()
8     numero = int(input())
```

Nesse caso, o bloco de código dentro do `while` é executado repetidamente enquanto a condição `numero != 0` for verdadeira. Isso permite que o programa solicite ao usuário números repetidamente até que o número zero seja inserido, encerrando o programa. O `while` é uma ferramenta valiosa para lidar com situações em que a iteração é necessária, mas o número de repetições não é conhecido com antecedência.

## Siga em Frente...

### Controle de repetição: range, break e continue

A função `range()`, em Python, é uma ferramenta útil para criar sequências numéricas que podem ser usadas em estruturas de repetição, como o comando `for`. Ela oferece flexibilidade ao especificar os limites e o incremento da sequência.

**Método 1 – Repetição por quantidade**

No primeiro método, você pode passar um único argumento para `range()`, que representa a quantidade de vezes em que o loop deve ser repetido. Por exemplo, `range(5)` cria uma sequência que se inicia em 0 e vai até 4, realizando 5 iterações.

```python
for x in range(5):
    print(x)

#a saída será:
```

```text
0
1
2
3
4
```

**Método 2 – Limites inicial e superior**

No segundo método, você pode fornecer dois argumentos para `range()`. O primeiro argumento representa o início das repetições e o segundo, o limite superior (não incluso) do valor da variável de controle. Por exemplo, `range(2, 7)` cria uma sequência que se inicia em 2 e vai até 6, realizando 5 iterações.

```python
for y in range(2, 7):
    print(y)

#a saída será:
```

```text
2
3
4
5
6
```

**Método 3 – Com incremento**

No terceiro método, você pode passar três argumentos para `range()`. O primeiro argumento é o início das repetições, o segundo é o limite superior (não incluso) e o terceiro argumento representa o incremento entre cada iteração. Por exemplo, `range(1, 11, 2)` cria uma sequência que começa em 1, vai até 10 e incrementa de 2 em 2, resultando nas iterações de 1, 3, 5, 7 e 9.

```python
for z in range(1, 11, 2):
    print(z)
#a saída será:
```

```text
1
3
5
7
9
```

Além de controlar iterações com base na sequência de números ou condições específicas, Python oferece dois comandos eficientes para influenciar o fluxo de execução em estruturas de repetição: `break` e `continue`. Vamos entender como esses comandos funcionam e analisar alguns exemplos práticos.

O comando `break` é usado para interromper a execução de uma estrutura de repetição quando uma determinada condição é atendida. Essencialmente, esse comando permite sair do loop antes que ele seja concluído. Isso é útil quando você deseja encerrar um loop prematuramente com base em algum critério.

Suponha que desejemos encontrar o primeiro número par em uma sequência e interromper a iteração assim que o acharmos:

```python
for numero in range(1, 11):
    if numero % 2 == 0:
        print(, numero)
        break
#a saída será:
```

```text
O primeiro número par encontrado é: 2
```

Nesse exemplo, o loop `for` itera de 1 a 10, mas, assim que encontra o primeiro número par (2), o comando `break` é acionado. Desse modo, interrompe-se a execução do loop.

O comando `continue` é usado para pular a iteração atual em uma estrutura de repetição e continuar com a próxima iteração. Isso é vantajoso quando você deseja ignorar uma iteração com base em uma condição, mas quer continuar com o restante do loop.

Vamos considerar um loop que imprime todos os números de 1 a 10, exceto o número 5:

```python
for numero in range(1, 11):
    if numero == 5:
        continue
    print(numero)
#a saída será:
```

```text
1
2
3
4
6
7
8
9
10
```

Nesse caso, quando o número é igual a 5, o comando `continue` é acionado, fazendo com que a iteração atual seja abandonada. A execução continua com o próximo número.

Em resumo, o `break` e o `continue` são comandos úteis para controlar o fluxo em estruturas de repetição, permitindo interromper loops antecipadamente com `break` e pular iterações específicas com `continue`, com base em condições específicas. Essas ferramentas adicionam flexibilidade ao controle de repetições em Python.

## Vamos Exercitar?

Vamos pensar na solução do problema apresentado no início desta aula. Precisamos criar um programa que seja capaz de percorrer todos os filmes (Filme 1, Filme 2, Filme 3, Filme 4 e Filme 5) e de atribuir a cada um deles uma nota de 1 a 5. Repare que é importante sempre disponibilizar uma forma de a pessoa encerrar o programa, caso queira.

```python
filmes = [, , , , ]

print()
print()
print()

for filme in filmes:
    while True:
        classificacao = input(f{filme}' de 1 a 5? (ou 0 para parar): ")
        if classificacao == '0':
            print(f{filme}' interrompida.")
            break # Encerra o loop interno com "break"
        classificacao = int(classificacao)
        if classificacao < 1 or classificacao > 5:
            print()
        else:
            print(f{filme}' com {classificacao} estrelas.\n")
            break # Sai do loop interno

    print()
```

Nessa solução, utilizamos "while True:", que é uma técnica comum para criar loops em que a condição de parada pode variar ou não é conhecida, como acontece nesse exemplo, visto que o usuário pode parar a classificação escolhendo 0 ou encerrá-la depois de classificar todos os cinco filmes.

Gostou dessa solução? Espero que sim! Rode esse código no colab, faça modificações e "brinque" com ele. Lembre-se de que a prática é extremamente importante para alcançar melhorias.

## Saiba mais

1. Para entender como funciona a aplicação de processos automatizados, leia o texto *Robotic process automation e a auditoria financeira: modern framework*, que utiliza algoritmos para automação e inteligência artificial. Note que já aprendemos sobre Python, porém existem outras linguagens semelhantes que também são adotadas para a automação. Para acessar o conteúdo sugerido, clique no link disponível a seguir.
   > CALÇADA, L. I. S. **Robotic process automation e a auditoria financeira: modern framework**. 2020. 52 f. Dissertação (Mestrado em Gestão de Sistemas de Informação) – Instituto Superior de Economia e Gestão, Universidade de Lisboa, Lisboa, 2020.

2. Uma leitura interessante para quem está começando a programar em Python é a do livro *Começando a programar em Python para leigos*.
   > MUELLER, J. P. **Começando a programar em Python para leigos**. Rio de Janeiro: Alta Books, 2020. E-book.

3. Outra dica para estudo e aprofundamento sobre esse tema é o livro *Use a cabeça! Python*.
   > BARRY, P. **Use a Cabeça! Python**. 2. ed. Rio de Janeiro: Alta Books, 2018. E-book.

## Referências

- BARRY, P. Use a Cabeça! Python. 2. ed. Rio de Janeiro: Alta Books, 2018. E-book. Disponível em: https://integrada.minhabiblioteca.com.br/#/books/9786555207842. Acesso em: 12 out. 2023.
- CALÇADA, L. I. S. Robotic process automation e a auditoria financeira: modern framework. 2020. 52 f. Dissertação (Mestrado em Gestão de Sistemas de Informação) – Instituto Superior de Economia e Gestão, Universidade de Lisboa, Lisboa, 2020. Disponível em: https://www.repository.utl.pt/bitstream/10400.5/20874/1/DM-LISC-2020.pdf. Acesso em: 12 out. 2023.
- GOOGLE COLAB. Página inicial, [s. d.]. Disponível em: https://colab.research.google.com/. Acesso em: 12 out. 2023.
- MANZANO, J. A. N. G.; OLIVEIRA, J. F. de. Algoritmos: lógica para desenvolvimento de programação de computadores. 29. ed. São Paulo: Érica, 2019.
- MUELLER, J. P. Começando a programar em Python para leigos. Rio de Janeiro: Alta Books, 2020. E-book. Disponível em: https://integrada.minhabiblioteca.com.br/#/books/9786555202298. Acesso em: 12 out. 2023.
