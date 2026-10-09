# Aula 3 — Permutações Matemáticas

## Ponto de Partida

Olá, estudante! Nesta aula, você terá a oportunidade de explorar assuntos relacionados a permutações matemáticas.

Nesta unidade, você aprenderá o que são permutações matemáticas e como utilizá-las tanto na matemática como em diversas áreas como:

- **Análise de algoritmos**: em ciência da computação, as permutações são frequentemente usadas em algoritmos que envolvem a ordenação de elementos. Algoritmos de ordenação como o Quicksort e o Mergesort dependem de permutações para funcionar.
- **Códigos e criptografia**: na área de segurança da informação, as permutações são usadas na criação de códigos secretos e na criptografia, em que a ordem dos elementos é fundamental para proteger informações.
- **Engenharia e design**: em engenharia, as permutações são usadas para organizar componentes em sistemas complexos, como circuitos eletrônicos, redes de comunicação e design de produtos. A ordem dos componentes é crítica em muitos casos.

Nesta aula, será introduzido assuntos relacionados às permutações matemáticas, às fórmulas e aos exemplos de aplicações. Esta seção abordará alguns princípios matemáticos relacionados à lógica. Você pode já ter se deparado com problemas do tipo:

- Suponha que você queira criar todas as permutações possíveis das letras A, B e C. Como você faria isso?
- Se você tem uma lista de cinco músicas e deseja organizá-las em uma ordem específica em uma playlist. Como representar todas as maneiras possíveis de organizar essas músicas?

Esses problemas, além do raciocínio lógico, envolvem noções de listagem, contagem e agrupamentos, noções estas que teremos oportunidade de conhecer um pouco melhor nesta seção e ajudarão você a resolver seu terceiro desafio.

> Para motivar sua aprendizagem, imagine que você coordena uma equipe de ciclistas. Suponha que essa equipe, que consiste em quatro ciclistas identificados como A, B, C e D esteja participando de uma corrida. Eles chegam a uma interseção com quatro caminhos numerados de 1 a 4. Cada ciclista deve escolher um caminho diferente na interseção. Como você faria para projetar todas as maneiras diferentes que a equipe pode escolher cada caminho?

Aproveite ao máximo a oportunidade de praticar o estudo relacionado às permutações matemáticas. Esses conceitos são de suma importância para profissionais que desenvolvem sistemas de software utilizando diferentes linguagens de programação e algoritmos, permitindo que executem suas funções técnicas de forma eficaz e alcancem resultados profissionais excepcionais.

Bons estudos!

---

## Vamos Começar!

### Permutações

**Permutações matemáticas** são arranjos de elementos de um conjunto em uma ordem específica. Em outras palavras, as permutações representam todas as diferentes maneiras de organizar os elementos do conjunto, em que a ordem dos elementos é fundamental.

O número de permutações de um conjunto de n elementos é denotado como "P(n)" ou "n!" (lê-se "n fatorial") e é calculado como o produto de todos os números inteiros positivos de 1 a n.

A fórmula geral para calcular o número de permutações de n elementos é:

$$P(n) = n!$$

Por exemplo, se você tem um conjunto de três elementos {A, B, C}, o número de permutações possíveis é 3! (3 fatoriais), que é igual a 3 x 2 x 1 = 6 permutações:

| 1 | 2 | 3 | 4 | 5 | 6 |
|:---:|:---:|:---:|:---:|:---:|:---:|
| ABC | ACB | BAC | BCA | CAB | CBA |

As permutações são amplamente usadas em problemas de contagem, estatísticas, combinatorial, teoria das probabilidades e diversas outras aplicações em matemática, ciência, engenharia e outras áreas. Elas são uma ferramenta fundamental para lidar com situações em que a ordem dos elementos é crítica.

---

## Siga em Frente...

### Exemplos de permutações

#### Exemplo 01

> Quantos anagramas podem ser formados com as letras da palavra BRASIL?

Como anagrama é permutação, então, aplicando a fórmula da permutação:

**Solução:**

$$P_n = n! \qquad P_6 = 6! \qquad P_6 = 6 \cdot 5 \cdot 4 \cdot 3 \cdot 2 \cdot 1 = 720$$

#### Exemplo 02

> Quantas permutações distintas podem ser formadas usando todas as letras da palavra "MATE"?

**Solução:**

Uma permutação é uma organização ordenada dos elementos. Neste caso, queremos organizar as letras da palavra "MATE".

A palavra "MATE" contém quatro letras, então temos n = 4 elementos para organizar. Vamos calcular o número de permutações:

1. Começamos com quatro opções para a primeira posição. Podemos escolher qualquer uma das quatro letras: M, A, T ou E.
2. Para a segunda posição, agora restam três letras, pois já usamos uma na primeira posição. Portanto, temos três opções.
3. Na terceira posição, restam duas letras, pois já usamos duas nas posições anteriores. Temos duas opções.
4. Finalmente, na quarta posição, a última letra é automaticamente definida, já que as outras três letras foram usadas nas posições anteriores.

Agora, podemos multiplicar o número de opções em cada posição para obter o número total de permutações:

| 1ª posição | 2ª posição | 3ª posição | 4ª posição | Total |
|:---:|:---:|:---:|:---:|:---:|
| 4 | × 3 | × 2 | × 1 | **= 24 permutações** |

Portanto, existem **24 permutações** distintas que podem ser formadas usando todas as letras da palavra "MATE." Isso significa que há 24 maneiras diferentes de organizar essas quatro letras em uma ordem específica.

#### Exemplo 03

> Suponha que você tenha cinco livros diferentes (A, B, C, D, E) em uma prateleira e deseja organizá-los em uma ordem específica. Quantas maneiras diferentes você pode realizar essa organização?

**Solução:**

Este é um problema de permutação, no qual queremos calcular o número de maneiras de organizar os cinco livros em uma ordem específica.

1. Começamos com cinco opções para a primeira posição na prateleira. Podemos escolher qualquer um dos cinco livros.
2. Para a segunda posição, restam quatro livros, pois já usamos um na primeira posição. Portanto, temos quatro opções.
3. Na terceira posição, restam três livros, já que usamos dois nas posições anteriores. Temos três opções.
4. Para a quarta posição, restam dois livros, pois já usamos três nas posições anteriores. Temos dois opções.
5. Finalmente, para a quinta posição, o último livro é automaticamente definido, já que os outros quatro foram usados nas posições anteriores.

Agora, multiplicamos o número de opções em cada posição para obter o número total de permutações:

| 1ª posição | 2ª posição | 3ª posição | 4ª posição | 5ª posição | Total |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 5 | × 4 | × 3 | × 2 | × 1 | **= 120 maneiras diferentes** |

Portanto, existem **120 maneiras** diferentes de organizar os cinco livros em uma ordem específica na prateleira. Cada permutação representa uma configuração única dos livros.

---

## Vamos Exercitar?

Você se lembra que na situação-problema, você coordena uma equipe de ciclistas que participará de uma corrida.

> Suponha que a equipe de ciclistas, que consiste em quatro ciclistas identificados como A, B, C e D esteja participando de uma corrida. Eles chegam a uma interseção com quatro caminhos numerados de 1 a 4. Cada ciclista deve escolher um caminho diferente na interseção. Quantas maneiras diferentes a equipe pode escolher os caminhos?

**Solução:**

Este é um problema de permutação, em que estamos organizando os quatro ciclistas em ordem nos quatro caminhos. Como a ordem é importante, usamos permutações.

1. Primeiro, escolhemos um caminho para o ciclista A. Temos quatro opções (caminhos 1, 2, 3 e 4).
2. Depois, escolhemos um caminho para o ciclista B, que não seja o mesmo que o escolhido para o ciclista A. Temos três opções restantes.
3. Em seguida, escolhemos um caminho para o ciclista C, que não seja o mesmo que os caminhos escolhidos para A e B. Restam duas opções.
4. Finalmente, o último caminho é automaticamente atribuído ao ciclista D.

Portanto, o número total de maneiras diferentes de a equipe escolher os caminhos é:

| Ciclista A | Ciclista B | Ciclista C | Ciclista D | Total |
|:---:|:---:|:---:|:---:|:---:|
| 4 | × 3 | × 2 | × 1 | **= 24 maneiras diferentes** |

Assim, existem **24 maneiras** diferentes para a equipe escolher os caminhos na interseção. Cada permutação representa uma configuração única em que os ciclistas escolhem os caminhos.

---

## Saiba mais

Permutações matemáticas desempenham um papel fundamental em muitos campos da matemática, ciência, engenharia e em diversas aplicações do mundo real. A seguir, algumas indicações para um estudo profundo sobre o tema.

1. > LUSTOSA, D. **Raciocínio lógico-matemático para concursos públicos: teoria e prática**. (Série Provas & Concursos). Grupo GEN, 2023.

2. > ARAUJO, L. M. M. et al. **Fundamentos de matemática**. Grupo A, 2018.

## Referências

- ARAUJO, L. M. M. et al. Fundamentos de matemática. Grupo A, 2018.
- LUSTOSA, D. Raciocínio lógico-matemático para concursos públicos: teoria e prática. (Série Provas & Concursos). Grupo GEN, 2023.
- QUILELLI, P. Raciocínio lógico matemático para concursos. 3. ed. Editora Saraiva, 2015.
- ROSEN, K. H. Matemática discreta e suas aplicações. Grupo A, 2010.
