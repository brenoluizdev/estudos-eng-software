# Aula 4 — Combinações Matemáticas

## Ponto de Partida

Olá, estudante! Nesta aula, você terá a oportunidade de explorar assuntos relacionados a combinações matemáticas.

Durante os estudos, você aprenderá o que são combinações matemáticas e como utilizá-las tanto na matemática como em diversas áreas como:

**Nas engenharias:**

- **Em ciência da computação**: combinações são usadas em permutações e arranjos, em que a ordem dos elementos é importante.
- **Análise de algoritmos**: em análise de algoritmos, combinações podem ser usadas para determinar a complexidade de algoritmos relacionados à seleção e combinação de elementos.

**Teoria dos jogos:**

- **Cálculo de estratégias**: em teoria dos jogos, combinações são usadas para calcular estratégias de jogadores em jogos de escolha simultânea.

Nesta aula, será introduzido assuntos relacionados às combinações matemáticas, fórmulas e aos exemplos de aplicações. Esta seção abordará alguns princípios matemáticos relacionados à lógica. Você pode já ter se deparado problemas do tipo:

- Suponha que você precise formar uma equipe de três pessoas a partir de um grupo de oito. Você pode usar combinações para determinar quantas equipes diferentes podem ser formadas.
- Quantos subconjuntos de um conjunto de cinco elementos podem ser criados? As combinações ajudam a calcular isso.

Esses problemas, além do raciocínio lógico, envolvem noções de listagem, contagem e agrupamentos, noções estas que teremos oportunidade de conhecer um pouco melhor nesta seção e ajudarão você a resolver seu terceiro desafio.

> Para motivar sua aprendizagem, suponha que você está liderando um projeto em uma empresa e precisa montar uma equipe de quatro membros a partir de um grupo de dez funcionários disponíveis. Você deseja garantir que a equipe seja diversificada e eficaz, mas a ordem dos membros não importa.

Aproveite ao máximo a oportunidade de praticar o estudo relacionado às combinações matemáticas. Esses conceitos são de suma importância para profissionais que desenvolvem sistemas de software utilizando diferentes linguagens de programação e algoritmos, permitindo que executem suas funções técnicas de forma eficaz e alcancem resultados profissionais excepcionais.

Bons estudos!

---

## Vamos Começar!

### Combinações

**Combinações matemáticas** são uma técnica de contagem usada na teoria de probabilidade e na matemática discreta para calcular o número de maneiras diferentes de escolher um subconjunto de elementos de um conjunto maior, em que a ordem dos elementos não importa. Em outras palavras, combinações se concentram em selecionar grupos de elementos sem considerar a ordem em que esses elementos são escolhidos.

A notação padrão para representar combinações é "C(n, k)", onde:

- **n** é o número total de elementos do conjunto;
- **k** é o número de elementos escolhidos.

> **Nota de revisão:** no material original, a lista após "onde:" estava vazia; as definições de n e k acima foram completadas conforme o uso feito no restante da aula.

A fórmula geral para calcular o número de combinações, "C(n, k)", é dada por:

$$C_n^k = \dfrac{n!}{k!(n-k)!}$$

Onde "n!" representa o fatorial de "n", que é o produto de todos os inteiros positivos de 1 a "n".

As combinações são usadas em várias situações da vida real, como:

- **Seleção de equipes**: ao escolher membros para equipes, comitês ou grupos de trabalho, garantindo diversidade e habilidades específicas.
- **Probabilidade**: para calcular as chances de eventos em experimentos de probabilidade, como jogos de cartas ou lançamento de dados.
- **Matemática discreta**: em problemas de contagem, como determinar quantas maneiras diferentes você pode escolher um grupo de estudantes para formar um projeto de sala de aula.
- **Estatística**: no cálculo de combinações de variáveis aleatórias em estatísticas.
- **Teoria de grafos**: em teoria dos grafos, para contar subconjuntos de vértices em um grafo.

Combinações são uma ferramenta poderosa para resolver problemas de contagem, especialmente quando a ordem dos elementos não é relevante, em contraste com as permutações, na qual a ordem é fundamental.

### Passo a passo para calcular uma combinação simples

Para calcular o total de combinações possíveis, basta realizar a substituição na fórmula e calcular os fatoriais necessários.

#### Exemplo 1

> Calcule todas as combinações possíveis de 10 elementos tomados de 4 em 4.

1. **1º Passo**: conforme ilustrado no passo 1, temos que identificar o valor de n e de k e substituir na fórmula. No caso temos n = 10 e k = 4.
2. **2º Passo**: conforme ilustrado no passo 2, precisamos realizar a simplificação do fatorial, multiplicando o numerador pelos seus antecessores até chegar ao maior fatorial do denominador. Nesse caso simplificaremos 10!, multiplicando 10 por seus antecessores até chegar a 6!, e fazendo a simplificação no numerador e no denominador.
3. **3º Passo**: conforme ilustrado no passo 2, é necessário realizar a multiplicação do numerador e calcular o fatorial do denominador, e, posteriormente, realizar a divisão.

**Resolução do Exemplo 1 (1º passo):**

$$C_n^k = \dfrac{n!}{k!(n-k)!}$$

$$C_{10}^4 = \dfrac{10!}{4!(10-4)!}$$

$$C_{10}^4 = \dfrac{10!}{4!\,6!}$$

**Resolução do Exemplo 1 (2º passo):**

$$C_{10}^4 = \dfrac{10!}{4!\,6!}$$

$$C_{10}^4 = \dfrac{10 \cdot 9 \cdot 8 \cdot 7 \cdot 6!}{4!\,6!}$$

$$C_{10}^4 = \dfrac{10 \cdot 9 \cdot 8 \cdot 7}{4!}$$

**Resolução do Exemplo 1 (3º passo):**

$$C_{10}^4 = \dfrac{10 \cdot 9 \cdot 8 \cdot 7}{4!}$$

$$C_{10}^4 = \dfrac{5040}{24}$$

$$C_{10}^4 = 210$$

Desse modo, significa que existem **210 combinações** possíveis para 10 elementos tomados de 4 em 4.

#### Exemplo 2

> Uma pizzaria oferece dez opções em seu cardápio. Eles possuem um tamanho especial chamada pizza gigante, no qual o cliente pode dividir a pizza em quatro partes, escolhendo sabores diferentes. De quantos modos uma pizza gigante pode ser formada, escolhendo quatro sabores diferentes entre as dez opções do cardápio?

**Resolução:**

Não há relevância na ordem dos sabores, por isso, é um problema de combinação.

$$C_n^p = \dfrac{n!}{p!(n-p)!}$$

$$C_{10}^4 = \dfrac{10!}{4!(10-4)!}$$

$$C_{10}^4 = \dfrac{10!}{4!\,6!} = \dfrac{10 \cdot 9 \cdot 8 \cdot 7 \cdot 6!}{4 \cdot 3 \cdot 2 \cdot 1 \cdot 6!}$$

$$C_{10}^4 = \dfrac{5040}{24} = 210$$

#### Exemplo 3

> Um trio deve ser formado por um gerente, um supervisor e um operador. De quantos modos diferentes este trio pode ser formado se há dez pessoas disponíveis para ocuparem estes cargos?

**Resolução:**

Para resolver, devemos refletir sobre a importância do ordenamento. Como há posições específicas, o ordenamento importa e utilizamos arranjo.

Pela fórmula do arranjo, temos:

$$A_n^p = \dfrac{n!}{(n-p)!} =$$

$$A_n^p = \dfrac{10!}{(10-3)!} =$$

$$A_n^p = \dfrac{10!}{7!} = \dfrac{10 \cdot 9 \cdot 8 \cdot 7!}{7!} = 720$$

> **Nota de revisão:** no material original, a fórmula do arranjo aparecia como $\dfrac{n!}{p!(n-p)!}$ — essa é a fórmula da **combinação**. A fórmula do arranjo é $\dfrac{n!}{(n-p)!}$, que é a que de fato foi usada na conta. O resultado (720) não muda.

---

## Siga em Frente...

### Diferença entre combinação, arranjo e permutação

Problemas diferentes de contagem requerem técnicas diferentes para serem solucionados. Arranjos e permutações são outras destas técnicas. O que define qual utilizar são as condições do problema a ser resolvido.

- Caso a ordem dos elementos no subconjunto formado **não seja relevante**, em que os ordenamentos diferentes produzem o mesmo resultado, utilizamos **combinação**.
- Nas situações em que o ordenamento **é relevante**, produzindo resultados diferentes, utilizamos **arranjo** ou **permutação**.

A escolha do método é determinada pelo que o problema diz, por isto, a interpretação dos enunciados e das situações-problema são fundamentais para os solucionar corretamente.

#### Permutação

Nas permutações, o número de elementos é igual ao número de posições disponíveis. Vejamos o exemplo a seguir: *Quantos modos distintos 5 pessoas podem ocupar 5 assentos diferentes?* Neste caso, o número de elementos (5) é igual ao número de posições (5). Portanto, "ABCDE" é diferente de "EBCDA", resultando em $P_5 = 5! = 120$ maneiras distintas.

#### Arranjo

Por outro lado, nos arranjos, o número de elementos é maior do que o número de posições disponíveis. Considere o exemplo a seguir: *Quantos modos distintos 10 pessoas podem ocupar 3 assentos?* Observe que o número de elementos é 10, e o número de posições é 3. Portanto, aplicamos a fórmula de arranjo, como ilustrado a seguir.

**Resolução da situação-problema dos arranjos:**

$$A_{n,k} = \dfrac{n!}{(n-k)!} =$$

$$A_{n,k} = \dfrac{10!}{(10-3)!}$$

$$A_{n,k} = \dfrac{10 \cdot 9 \cdot 8 \cdot 7!}{7!}$$

$$A_{n,k} = 10 \cdot 9 \cdot 8 = 720$$

#### Combinação

Combinações se concentram na seleção de elementos sem levar em consideração a ordem em que são selecionados. A ordem dos elementos não importa. Duas combinações com os mesmos elementos são consideradas iguais, independentemente da ordem.

Vejamos o exemplo a seguir:

> Quantos trios podemos formar de 5 pessoas diferentes?

ABC = CBA (Não). Por exemplo, a diretora solicitou que a professora realizasse a escolha de trios de alunos para realizarem uma apresentação. E neste caso, tem que ser trios de alunos diferentes e não iguais. Veja a resolução deste caso, a seguir.

**Resolução da situação-problema de combinações:**

- **Número total de pessoas (n):** 5
- **Número de pessoas no trio (k):** 3
- **Fórmula da combinação:** $C(n,k) = \dfrac{n!}{k!(n-k)!}$
- **Cálculo:** $C(5,3) = \dfrac{120}{12} = 10$

Assim, podemos formar **10 trios** diferentes de 5 pessoas.

#### Resumo

| Técnica | A ordem importa? | Fórmula |
|---|---|---|
| Permutação | Sim (nº de elementos = nº de posições) | $P_n = n!$ |
| Arranjo | Sim (nº de elementos > nº de posições) | $A_{n,k} = \dfrac{n!}{(n-k)!}$ |
| Combinação | Não | $C(n,k) = \dfrac{n!}{k!(n-k)!}$ |

Em resumo, permutações consideram a ordem dos elementos, combinações não consideram a ordem e tratam elementos idênticos como iguais, enquanto arranjos lidam com a ordem e permitem repetições. Cada um desses conceitos é útil em diferentes contextos e problemas de contagem, dependendo das restrições e dos requisitos específicos do problema em questão.

> **Nota de revisão:** o resumo acima diz que "arranjos [...] permitem repetições" — isso vale apenas para o **arranjo com repetição** ($n^p$). O **arranjo simples** ($\dfrac{n!}{(n-k)!}$), usado nos exemplos desta aula, **não** permite repetir elementos (ver Aula 2).

---

## Vamos Exercitar?

Você se lembra que na situação-problema, você está liderando um projeto em uma empresa que necessita montar uma equipe, certo?

> Suponha que você está liderando um projeto em uma empresa e precisa montar uma equipe de 4 membros a partir de um grupo de 10 funcionários disponíveis. Você deseja garantir que a equipe seja diversificada e eficaz, mas a ordem dos membros não importa.

**Solução:**

A fórmula de combinação é dada por C(n, k), onde "n" representa o número total de elementos e "k" é o número de elementos a serem selecionados.

Neste caso:

- "n" é o número total de funcionários disponíveis (10).
- "k" é o número de membros da equipe que você deseja escolher (4).

> **Nota de revisão:** a linha de "n" estava ausente no material original e foi completada com o valor do enunciado.

Usando a fórmula de combinação, você pode calcular o número de maneiras de formar a equipe diversificada e eficaz:

$$C(10, 4) = \dfrac{10!}{4!(10 - 4)!} = 210 \text{ maneiras}$$

Portanto, há **210 maneiras** diferentes de formar uma equipe de 4 membros a partir do grupo de 10 funcionários disponíveis, garantindo que a equipe seja diversificada e eficaz. Lembre-se de que a ordem dos membros na equipe não é relevante, pois estamos tratando de combinações, não permutações.

---

## Saiba mais

Combinações matemáticas desempenham um papel fundamental em muitos campos da matemática, ciência, engenharia e em diversas aplicações do mundo real. A seguir, algumas indicações para um estudo profundo sobre o tema.

1. Neste livro, no capítulo 4 é abordado de forma clara e intuitiva o tópico relacionado a combinações matemáticas.
   > GERSTING, J. L. **Fundamentos matemáticos para a ciência da computação**. Grupo GEN, 2016.

2. Este livro, aborda no capítulo 4 em análise combinatória o tópico relacionado a combinações simples, de uma maneira muito interativa.
   > QUILELLI, P. **Raciocínio lógico matemático para concursos**. 3. ed. Editora Saraiva, 2015.

## Referências

- ARAUJO, L.M. M. et al. Fundamentos de matemática. Grupo A, 2018.
- LUSTOSA, D. Raciocínio lógico-matemático para concursos públicos: teoria e prática. (Série Provas & Concursos). Grupo GEN, 2023.
- QUILELLI, P. Raciocínio lógico matemático para concursos. 3. ed. Editora Saraiva, 2015.
